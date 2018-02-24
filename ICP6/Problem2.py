from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

df = pd.read_csv(r'C:\Users\Samsung\PycharmProjects\Python_DeepLearning\venv\ICP6\sample_stocks.csv')
feature = df.values;

if 1:
    x = feature[:, 0]
    y = feature[:, 1]
    print(x)
    print(y)
    kmeans = KMeans(n_clusters=3).fit(feature)

    plt.scatter(x, y, c=kmeans.labels_)
    plt.show()

else:
    # k means determine k
    distortions = []
    K = range(1, 10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(feature)
        kmeanModel.fit(feature)
        distortions.append(sum(np.min(cdist(feature, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / feature.shape[0])

    # Plot the elbow
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()
