from pandas import read_excel, DataFrame
from matplotlib.pyplot import plot, show, rcParams, legend
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
d1=read_excel("data-corn-epi-16h.xlsx",index_col='Unnamed: 0')
d2=read_excel("data-corn-epi-t0.xlsx",index_col='Unnamed: 0')
for i,j in zip(d1.columns,d2.columns):
    diff[i]=[k-l for k,l in zip(d1[i],d2[j])]
for i in diff.index:
    plot(diff.columns,diff.loc[i,])
    show()