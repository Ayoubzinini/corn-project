from pca import pca
from pandas import DataFrame, read_excel
from matplotlib.pyplot import show
diff=DataFrame()
d1=read_excel("data-corn-epi-16h.xlsx",index_col='Unnamed: 0')
d2=read_excel("data-corn-epi-t0.xlsx",index_col='Unnamed: 0')
for i,j in zip(d1.columns,d2.columns):
    diff[i]=[float(k-l) for k,l in zip(d1[i],d2[j])]
diff.columns=[str(i) for i in diff.columns]
model = pca(n_components=diff.shape[0])
results = model.fit_transform(diff)
fig, ax = model.biplot(SPE=False, hotellingt2=True)
show()