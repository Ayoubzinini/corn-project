from pandas import read_excel, DataFrame
from matplotlib.pyplot import plot, show, rcParams, legend, xlabel, ylabel, title
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
diff=DataFrame()
d1=read_excel("data-corn-feuille-16h.xlsx",index_col='Unnamed: 0')
d2=read_excel("data-corn-feuille-t0.xlsx",index_col='Unnamed: 0')
for i,j in zip(d1.columns,d2.columns):
    diff[i]=[k-l for k,l in zip(d1[i],d2[j])]
#"""
for i in diff.index:
    plot(diff.columns,diff.loc[i,])
    print(max(diff.loc[i,])-min(diff.loc[i,]))
show()
#"""
pc = PCA(diff, ncomp=diff.shape[0], method='nipals')
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