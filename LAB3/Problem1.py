import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


def main():
    iris = datasets.load_iris()

    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Build LDA model
    lda = LinearDiscriminantAnalysis(n_components=3)
    # Traing the LDA and project it to 2D
	predict = lda.fit(X, y).transform(X)

	# Use the discriminant function to predict for new data
    print("New predict for [6.0, 2.5, 7.0, 2.4]: ", target_names[lda.predict([[6.0, 2.5, 7.0, 2.4]])])
	
	# Plot data using LDA classification
    plt.figure()
    colors = ['navy', 'turquoise', 'darkorange']

    for color, i, target_name in zip(colors, [0, 1, 2], target_names):
        plt.scatter(predict[y == i, 0], predict[y == i, 1], alpha=.8, color=color, label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('LDA of IRIS dataset')

    plt.show()


if __name__ == '__main__':
    print("LAB 3 - Problem 1\nLDA - Fisher Data")
    main()

