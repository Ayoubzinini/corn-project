from sklearn.model_selection import KFold,cross_val_predict, LeaveOneOut
from sklearn.metrics import mean_squared_error, mean_squared_log_error, max_error, r2_score, mean_absolute_error
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import normalize, StandardScaler
import seaborn as sns
from pandas import read_csv, read_excel
from matplotlib.pyplot import plot, show, xlabel, ylabel, title
from pandas import DataFrame, concat
import numpy as np
from scipy.stats import f_oneway, shapiro
from scipy.signal import savgol_filter, detrend
from preproc_NIR import osc, msc, snv, simple_moving_average, centring, var_sel, pow_trans
from statsmodels.multivariate.pca import PCA
db=read_excel('data-corn-feuille-t0.xlsx').dropna()
#X=db.drop(['moisture','oil','protien'],axis=1)
X=db.drop([db.columns[0],'Y1','Y2'],axis=1)
wl=X.columns
X=DataFrame(savgol_filter(msc(X.to_numpy()),51,1,1))#
X.columns=wl
#X=X[read_excel("C:/Users/hp/Downloads/corn_proj/corn_proj/choozen_wavelengths.xlsx")["choozen wavelengths values"]]
Y=db['Y1']
rescols=["r2c","r2cv","r2t","rmsec","rmsecv","rmset"]
r2c,r2cv,r2t,rmsec,rmsecv,rmset=[],[],[],[],[],[]
j=0
while True:
  r2=[]
  RMSE=[]
  for i in range(1,30,1):
    pc = PCA(X, ncomp=i, method='nipals')
    x_train, x_test, y_train, y_test = train_test_split(DataFrame(pc.factors),Y,test_size=0.2,random_state=j)
    model=SVR(C=10, epsilon=0.1,gamma=0.0001,kernel='linear')
    model.fit(x_train, y_train)
    r2.append(r2_score(model.predict(x_test),y_test))
    RMSE.append(mean_squared_error(model.predict(x_test),y_test))
  pc = PCA(X, ncomp=1+RMSE.index(min(RMSE)), method='nipals')
  x_train, x_test, y_train, y_test = train_test_split(DataFrame(pc.factors),Y,test_size=0.2,random_state=j)
  model=SVR(C=10, epsilon=0.1,gamma=0.0001,kernel='rbf')
  model.fit(x_train, y_train)
  RMSECV=abs(np.mean(cross_val_score(SVR(C=10, epsilon=0.1,gamma=0.0001,kernel='rbf'), x_train, y_train, scoring='neg_root_mean_squared_error', cv=LeaveOneOut())))
  R2CV=100*np.mean(cross_val_score(SVR(C=10, epsilon=0.1,gamma=0.0001,kernel='rbf'), x_train, y_train, scoring='r2'))
  R2train=100*r2_score(y_train,model.predict(x_train))
  R2test=100*r2_score(y_test,model.predict(x_test))
  RMSEtrain=mean_squared_error(y_train,model.predict(x_train))
  RMSEtest=mean_squared_error(y_test,model.predict(x_test))
  if R2test>0 and R2CV>0:
    r2c.append(R2train)
    r2cv.append(R2CV)
    r2t.append(R2test)
    rmsec.append(RMSEtrain)
    rmsecv.append(RMSECV)
    rmset.append(RMSEtest)
    break
res=DataFrame({rescols[0]:r2c,rescols[1]:r2cv,rescols[2]:r2t,rescols[3]:rmsec,rescols[4]:rmsecv,rescols[5]:rmset})
print(res)
w,p = shapiro([i-j for i,j in zip(y_test,model.predict(x_test))])
if p>0.05:
  desicion="Normal"
elif p<0.05:
  desicion="Not Normal"
print('Quantile shapiro : {}\npropability shapiro : {}\ndesicion : {}'.format(w,p,desicion))