from sklearn.datasets import load_digits
import numpy as np

digits = load_digits()

X = digits.data
y = digits.target


def calc_distance(x1, x2):
    return abs(np.sum(x1 - x2))


class NearestNeighborClassifier:
    def __init__(self):
        self.train_X = np.zeros(0)
        self.train_y = np.zeros(0)

    def fit(self, X, y):
        """
        fit the model using X as training data and y as target values
        :param X:
        :param y:
        :return:
        """
        self.train_X = X
        self.train_y = y

    def predict_single(self, x):
        """

        :param X:
        :return:
        """
        D = np.sum(np.abs(self.train_X - x), axis=1)
        i = np.argmin(D)
        return self.train_y[i]

    def predict(self, X):
        """

        :param X:
        :return:
        """
        num_test = X.shape[0]
        y = np.empty((num_test, ), dtype=int)
        for i in range(num_test):
            d_i = np.linalg.norm(self.train_X - X[i, ], ord=2, axis=1)
            y[i] = self.train_y[np.argmin(d_i)]
        return y

    def score(self, X, y):
        """
        returns the mean accuracy on the given test data and labels
        :param X:
        :param y:
        :return:
        """
        predict_y = self.predict(X)
        return np.sum(predict_y == y) / float(y.shape[0])


train_X, test_X = np.array_split(X, 2)
train_y, test_y = np.array_split(y, 2)

clf = NearestNeighborClassifier()
clf.fit(train_X, train_y)
print(clf.predict_single(test_X[0]))
print(clf.predict(test_X))
print(clf.score(test_X, test_y))
