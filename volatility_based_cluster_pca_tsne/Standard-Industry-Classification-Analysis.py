import pandas as pd
import random
import sklearn.decomposition as dp
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
from sklearn.manifold import TSNE

##analysis based on volatility
vol=pd.read_excel('波动率2021.xlsx')
vol.dropna(axis=0,inplace=True)
vol.set_index("证券代码")

industry_class=pd.read_excel('industry_classification.xlsx')
vol_ind=vol.merge(industry_class,on=['证券代码'])
vol_ind.set_index("证券代码")

n=len(vol_ind)
industry=[]
for i in range(n-2):
    industry.append(vol_ind.iloc[i,14])

vol_clus=vol_ind.filter(regex="21")

#PCA analysis
pca=dp.PCA(n_components=2)
pca_vol=pca.fit_transform(vol_clus)
pc1=[]
pc2=[]
for i in range(n):
    pc1.append(pca_vol[i][0])
    pc2.append(pca_vol[i][1])
plt.figure(figsize=(4,4))
for x,y,z in zip(pc1,pc2,industry):
    plt.scatter(x,y,label=z)
plt.legend
plt.show()

#t-SNE analysis
tsne=TSNE(n_components=2,random_state=0)
vol_2d=tsne.fit_transform(vol_clus)
target_ids=range(n)
tsne1=[]
tsne2=[]
for i in range(n):
    tsne1.append(vol_2d[i][0])
    tsne2.append(vol_2d[i][1])
plt.figure(figsize=(40,40))
for x,y,z in zip(tsne1,tsne2,industry):
    plt.scatter(x,y,label=z)
plt.legend
plt.show()


##analysis based on volatility
rev=pd.read_excel('return_rate.xlsx')
rev.dropna(axis=0,inplace=True)
rev.set_index("证券代码")

industry_class=pd.read_excel('industry_classification.xlsx')
rev_ind=vol.merge(industry_class,on=['证券代码'])
rev_ind.set_index("证券代码")

n=len(vol_ind)
industry=[]
for i in range(n-2):
    industry.append(vol_ind.iloc[i,14])

rev_clus=rev_ind.filter(regex="21")

#PCA analysis
pca=dp.PCA(n_components=2)
pca_rev=pca.fit_transform(rev_clus)
pc1_rev=[]
pc2_rev=[]
for i in range(n):
    pc1_rev.append(pca_rev[i][0])
    pc2_rev.append(pca_rev[i][1])
plt.figure(figsize=(4,4))
for x,y,z in zip(pc1_rev,pc2_rev,industry):
    plt.scatter(x,y,label=z)
plt.legend
plt.show()

#t-SNE analysis
tsne=TSNE(n_components=2,random_state=0)
rev_2d=tsne.fit_transform(rev_clus)
target_ids=range(n)
tsne1_rev=[]
tsne2_rev=[]
for i in range(n):
    tsne1_rev.append(rev_2d[i][0])
    tsne2_rev.append(rev_2d[i][1])
plt.figure(figsize=(40,40))
for x,y,z in zip(tsne1_rev,tsne2_rev,industry):
    plt.scatter(x,y,label=z)
plt.legend
plt.show()
