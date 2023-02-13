from sklearn.decomposition import FastICA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold,cross_val_predict, LeaveOneOut
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from pandas import DataFrame, read_excel, concat
from preproc_NIR import simple_moving_average, snv, msc, osc
from numpy import sqrt, log10
db=read_excel("data-corn-epi-16h.xlsx")
X=db.drop([db.columns[0],'Y1','Y2'],axis=1)
ica=FastICA(n_components=X.shape[0])
ica.fit_transform(X)
ic=DataFrame(ica.components_)
Y=db['Y1']
x_train, x_test, y_train, y_test = train_test_split(ic,Y,test_size=0.2)
icr=LinearRegression()
icr.fit(x_train,y_train)
print(DataFrame({
"R²c":r2_score(y_train,cross_val_predict(icr,x_train,y_train,cv=LeaveOneOut())),
"R²CV":r2_score(y_train,icr.predict(x_train)),
"R²t":r2_score(y_test,icr.predict(x_test)),
"RMSEc":mean_squared_error(y_train,cross_val_predict(icr,x_train,y_train,cv=LeaveOneOut())),
"RMSECV":mean_squared_error(y_train,icr.predict(x_train)),
"RMSEt":mean_squared_error(y_test,icr.predict(x_test))
},index=[0]))