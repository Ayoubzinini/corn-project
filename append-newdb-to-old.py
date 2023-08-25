from pandas import read_excel
il=list(range(64,88))
workig_l=list(range(0,64))
typr=[]
ctypr=[]
for i in il:
    workig_l.append(i)
    Xpr=read_excel("xpr.xlsx",index_col="Unnamed: 0",decimal=",").dropna()
    Xpr=Xpr.drop(['Y'],axis=1)
    Xpr=DataFrame(savgol_filter(DataFrame(msc(Xpr.to_numpy())),3,1,1))
    Xpr.columns=wl
    Xpr=Xpr[read_excel("C:/Users/hp/Downloads/corn_proj/corn_proj/choozen_wavelengths.xlsx")["choozen wavelengths values"]]
    Xpr=Xpr.loc[workig_l,:]
    print(model.predict(Xpr)[64][0]-mean(mael))
    ctypr.append(model.predict(Xpr)[64][0]-mean(mael))
    typr.append(model.predict(Xpr)[64][0])
    workig_l=list(range(0,64))
