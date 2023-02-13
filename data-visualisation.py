from pandas import read_excel, DataFrame
from matplotlib.pyplot import plot, show, rcParams, legend, xlabel, ylabel, title, axhline, subplots
from statsmodels.multivariate.pca import PCA
from seaborn.matrix import heatmap

"""
fn=input('File name : ')
db=read_excel(fn+'.xlsx')
db.index=db['Unnamed: 0']
db=db.drop(['Unnamed: 0'],axis=1)
for i in db.index:
    plot(db.columns,db.loc[i,])
show()
#"""

#"""
diff=DataFrame()
d1=read_excel("data-corn-feuille-16h.xlsx",index_col='Unnamed: 0')
d2=read_excel("data-corn-feuille-t0.xlsx",index_col='Unnamed: 0')
for i,j in zip(d1.columns,d2.columns):
    diff[i]=[k-l for k,l in zip(d1[i],d2[j])]
#"""

"""
for i in diff.index:
    plot(diff.columns,diff.loc[i,])
    axhline(y=10, color='black', linestyle='--')
    axhline(y=17, color='green', linestyle='--')
    axhline(y=23, color='red', linestyle='--')
    title(str(i))
    show()
#"""

"""
pc = PCA(diff, ncomp=diff.shape[0], method='nipals')
#"""

"""
for i in list(DataFrame(pc.factors).columns):
    il=list(DataFrame(pc.factors).columns)
    il.remove(i)
    for j in il:
        plot(DataFrame(pc.factors)[i],DataFrame(pc.factors)[j],'x')
        xlabel(i)
        ylabel(j)
        show()
#"""

"""
heatmap(DataFrame(pc.factors).corr())
show()
#"""

"""
for i in pc.loadings.columns:
    plot(pc.loadings.index,pc.loadings[i])
    xlabel('WL')
    ylabel(i)
    show()
#"""

#"""
filtring=read_excel("spectrum-notes-feuille.xlsx")
fl1,fl2,fl3=[],[],[]
fig,ax=subplots(2,2)
for i in filtring.index:
    if filtring.loc[i,"zone"]==10:
        fl1.append(i)
    elif filtring.loc[i,"zone"]==17:
        fl2.append(i)
    elif filtring.loc[i,"zone"]==23:
        fl3.append(i)
for i in diff.iloc[fl1].index:
    ax[0,0].plot(diff.iloc[fl1].columns,diff.iloc[fl1].loc[i,])
for i in diff.iloc[fl2].index:
    ax[0,1].plot(diff.iloc[fl2].columns,diff.iloc[fl2].loc[i,])
for i in diff.iloc[fl3].index:
    ax[1,0].plot(diff.iloc[fl3].columns,diff.iloc[fl3].loc[i,])
title("Part of the spectrum")
show()
#"""
il=[]
#i=49 should be with fl3 not fl2
for i in diff.iloc[fl3].index:
    il.append(i)
    for j in il:
        plot(diff.iloc[fl3].columns,diff.iloc[fl3].loc[j,])
    title(str(i))
    show()