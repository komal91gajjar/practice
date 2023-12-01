from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


centroids = [(-5,-5),(5,5)]
cluster_std = [1,1]

x,y = make_blobs(n_samples= 1000, cluster_std=cluster_std, centers= centroids, n_features= 5, random_state=5 )

plt.scatter(x[:,0], x[:,1])
plt.show()