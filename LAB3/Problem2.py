from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


def main():
    # load fisher iris dataset
    iris = load_iris()

    # Split the dataset into 70% training data and 30% testing data
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

    # Bulding model to train the data
    rbf = svm.SVC()
    linear = svm.SVC(kernel='linear')

    # Train data using RBF kernel model
    rbf.fit(x_train, y_train)

    # Predict the test data
    labels = rbf.predict(x_test)
    print("RBF Error: ", (y_test != labels).sum()/y_test.__len__())
    print(metrics.confusion_matrix(y_test, labels))
    print(metrics.classification_report(y_test, labels))

    # Train data using linear kernel model
    linear.fit(x_train, y_train)

    # Predict the test data
    labels = linear.predict(x_test)
    print("Linear Error: ", (y_test != labels).sum() / y_test.__len__())
    print(metrics.confusion_matrix(y_test, labels))
    print(metrics.classification_report(y_test, labels))

if __name__ == '__main__':
    print("LAB3 - Problem2\nSVM Classification of Iris Data")
    main()



