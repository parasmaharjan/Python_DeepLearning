from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics


def main():
    iris = load_iris()

    # print(iris.data)

    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

    rbf = svm.SVC()
    linear = svm.SVC(kernel='linear')

    print(rbf)
    rbf.fit(x_train, y_train)
    labels = rbf.predict(x_test)
    print("RBF Error: ", (y_test != labels).sum()/y_test.__len__())

    print(linear)
    linear.fit(x_train, y_train)
    labels = linear.predict(x_test)
    print("Linear Error: ", (y_test != labels).sum() / y_test.__len__())

if __name__ == '__main__':
    print("LAB3 - Problem2\nSVM Classification of Iris Data")
    main()



