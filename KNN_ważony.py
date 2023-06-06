import numpy as np
from collections import Counter
from sklearn import datasets
import random


def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1 - x2)**2))
    return distance

def manhattan_distance(x1, x2):
    distance = np.sum(np.abs(x1 - x2))
    return distance

def czebyszew_distance(x1, x2):
    distance = np.max(np.abs(x1 - x2))
    return distance


class KNN:
    def __init__(self, k=5, metric='euclidean'):
        self.k = k
        self.metric = metric

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        if self.metric == 'euclidean':
            distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        elif self.metric == 'manhattan':
            distances = [manhattan_distance(x, x_train) for x_train in self.X_train]
        elif self.metric == 'czebyszew':
            distances = [czebyszew_distance(x, x_train) for x_train in self.X_train]
        else:
            raise ValueError("Metryka może być tylko 'manhattan', 'czebyszew' lub 'euclidean'.")

        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        weights = [1 / d for d in distances if d != 0]
        weighted_predictions = Counter()
        for label, weight in zip(k_nearest_labels, weights):
            weighted_predictions[label] += weight

        most_common = weighted_predictions.most_common()

        #most_common = Counter(k_nearest_labels).most_common()

        return most_common[0][0]


def train_test_split(X, y, test_size=0.2, random_state=None):

    if random_state is None:
        random.seed(random_state)

    if len(X) != len(y):
        raise ValueError("Rozmiary X i y są niezgodne.")

    test_size = int(test_size * len(X))

    indices = list(range(len(X)))
    random.shuffle(indices)

    test_indices = indices[:test_size]
    train_indices = indices[test_size:]

    X_train = [X[i] for i in train_indices]
    y_train = [y[i] for i in train_indices]
    X_test = [X[i] for i in test_indices]
    y_test = [y[i] for i in test_indices]

    return X_train, X_test, y_train, y_test


iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


clf = KNN(k=5, metric='euclidean')
#clf = KNN(k=5, metric='manhattan')
#clf = KNN(k=5, metric='czebyszew')
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)


def show_coverage_in_percent(predictions, y_test):
    coverage = 0
    for i in range(len(predictions)):
        if predictions[i] == y_test[i]:
            coverage += 1
    print(f'Pokrycie: {coverage / len(predictions) * 100.0:.2f} %')


print(predictions)
show_coverage_in_percent(predictions, y_test)

