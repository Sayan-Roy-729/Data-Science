"""
Author: Sayan Roy
Date:   18-01-2022
"""


import numpy as np


class StandardScaler:
    def __init__(self):
        self.std = None
        self.mean = None

    def fit(self, X):
        """
        :param X: numpy array or pandas dataframe
        :return: nothing
        """
        self.std = np.std(X, axis=0)
        self.mean = np.mean(X, axis=0)

    def fit_transform(self, X):
        """
        :param X: numpy array or pandas dataframe
        :return: standardization numpy array along to column(s)
        """
        self.fit(X)
        return (X - self.mean)/self.std

    def transform(self, X):
        return (X - self.mean)/self.std
