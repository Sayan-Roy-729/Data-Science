import numpy as np


class MinMaxScaler:
    def __init__(self):
        self.min_ = None
        self.max_ = None

    def fit(self, X):
        self.min_ = np.min(X, axis=0)
        self.max_ = np.max(X, axis=0)

    def fit_transform(self, X):
        self.fit(X)
        return (X - self.min_)/(self.max_ - self.min_)

    def transform(self, X):
        return (X - self.min_)/(self.max_ - self.min_)
