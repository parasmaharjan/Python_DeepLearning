from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

gaussian_kernal = GaussianNB()
predict = gaussian_kernal.fit(x_train, y_train).predict(x_test)
print("Error: ", (y_test != predict).sum()/iris.data.__len__())

print(metrics.confusion_matrix(y_test, predict))
print(metrics.classification_report(y_test, predict))