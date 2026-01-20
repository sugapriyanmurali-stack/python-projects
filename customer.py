from sklearn.cluster import KMeans

data=[[1000],[2000],[3000],[9000],[10000],[11000]]
model=KMeans(n_clusters=2)
model.fit(data)
print("Customer Groups:",model.labels_)