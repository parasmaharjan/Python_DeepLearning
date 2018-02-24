from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt


def cluster_content(X, mu):
    cluster = {}
    for x in X:
        value = min([(i[0], np.linalg.norm(x - mu[i[0]]))for i in enumerate(mu)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis=0))for k in keys])
    return newmu


def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))


def Apply_Kmeans(X, K, N):
    temp1 = np.random.randint(N, size = K)
    oldmu = np.array([X[i]for i in temp1])
    #temp2 = np.random.randint(N, size=K)
    #newmu = np.array([X[i] for i in temp2])
    cluster = cluster_content(X, oldmu)
    newmu = new_center(cluster)
    itr = 0
    plot_cluster(oldmu,cluster,itr)
    while not matched(newmu, oldmu):
        itr = itr + 1
        oldmu = newmu
        cluster = cluster_content(X,newmu)
        plot_cluster(newmu, cluster,itr)
        newmu = new_center(cluster)
    plot_cluster(newmu, cluster, itr)
    return


def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()


def main():
    print(".........Starting Cluster Simulation.........")
    N = 300
    K = 2
    X, y_true = make_blobs(n_samples=N, centers=K, cluster_std=0.5, random_state=0)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()

    Apply_Kmeans(X, K, N)


if __name__ == "__main__":
    main()