from sklearn.model_selection import cross_val_predict, LeaveOneOut
from sklearn.metrics import mean_squared_error, max_error, r2_score, mean_absolute_error
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split, cross_val_score
from pandas import read_excel
from pandas import DataFrame
import numpy as np
from scipy.stats import f_oneway, shapiro
from scipy.signal import savgol_filter, detrend
from preproc_NIR import osc, msc, snv, simple_moving_average, centring, var_sel
from time import time
db=read_excel('data-corn-feuille-t0.xlsx').dropna()
dref=read_excel('data-corn-feuille-16h.xlsx').dropna()
X=db.drop([db.columns[0],'Y1','Y2'],axis=1)
wl=X.columns
Xref=dref.drop([db.columns[0],'Y1','Y2'],axis=1)
#"""
X=DataFrame(savgol_filter(DataFrame(msc(X.to_numpy())),3,1,1))
X.columns=wl
#X=choosen_wl_filter("choozen_wavelengths.xlsx",X)
#"""
#Y=db['Y2']
#Y=[i-np.mean(db['Y1']) for i in db['Y1']]
Y=db['Y1']
Yref=dref['Y1']
"""
diff=DataFrame()
d1=read_excel("data-corn-epi-16h.xlsx",index_col='Unnamed: 0').dropna()
d2=read_excel("data-corn-epi-t0.xlsx",index_col='Unnamed: 0').dropna()
for i,j in zip(d1.columns,d2.columns):
    diff[i]=[abs(k-l) for k,l in zip(d1[i],d2[j])]
#diff=msc(simple_moving_average(diff,window=7).iloc[:,:-1].values)
diff=DataFrame(savgol_filter(diff,3,1,0))
#"""
#X=msc(X.iloc[:,:-1].values,np.mean(Xref.iloc[:,:-1].values,axis=0))
#"""
j=3
while True:
    #x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=j)
    #income_groups=[y_train,y_test]
    #s,p=f_oneway(*income_groups)
    r2=[]
    RMSE=[]
    for i in range(1,30,1):
        model=PLSRegression(n_components=i,scale=False)
        model.fit(x_train, y_train)
        r2.append(r2_score(model.predict(x_test),y_test))
        RMSE.append(mean_squared_error(model.predict(x_test),y_test))
    model=PLSRegression(n_components=1+RMSE.index(min(RMSE)),scale=False)
    model.fit(x_train, y_train)
    RMSECV=abs(np.mean(cross_val_score(PLSRegression(n_components=1+RMSE.index(min(RMSE))), x_train, y_train, scoring='neg_root_mean_squared_error', cv=LeaveOneOut())))
    R2CV=100*np.mean(cross_val_score(PLSRegression(n_components=1+RMSE.index(min(RMSE))), x_train, y_train, scoring='r2'))
    R2train=100*r2_score(y_train,model.predict(x_train))
    R2test=100*r2_score(y_test,model.predict(x_test))
    RMSEtrain=mean_squared_error(y_train,model.predict(x_train))
    RMSEtest=mean_squared_error(y_test,model.predict(x_test))
    if R2CV>0 and R2test>0:
        break
    j=j+1
w,p = shapiro([i-j for i,j in zip(y_test,model.predict(x_test))])
if p>0.05:
  desicion="Normal"
elif p<0.05:
  desicion="Not Normal"
print(DataFrame({
    "R² c":R2train,
    "R² CV":R2CV,
    "R² t":R2test,
    "RMSE c":RMSEtrain,
    "RMSE CV":RMSECV,
    "RMSE t":RMSEtest,
    "Quantile Shapiro":w,
    "P Shapiro":p,
    "Decision":desicion,
    "RDS":j
},index=[0]))
print((x_test.loc[x_test.index[0],]) @ model.coef_ + (np.mean(y_train) - np.dot(np.mean(x_train),model.coef_)))
cf=[i[0] for i in model.coef_]
cf.append(np.mean(y_train) - np.dot(np.mean(x_train),model.coef_)[0])
DataFrame({'C':cf}).to_excel("coefs_model_corn.xlsx")
print(model.predict([x_test.loc[x_test.index[0],]]))
#"""
"""
you should put the papers data in their right place
the epi data is good, but because of your error, the papers data seems bad
"""