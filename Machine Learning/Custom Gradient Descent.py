import numpy as np

class GDRegressor:

    def __init__(self, learning_rate: float = 0.1, epochs: int = 100):
        self.coef_ = None
        self.intercept_ = None
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X: np.ndarray, y: np.ndarray):
        # initialize your coefficient
        self.intercept_ = 0
        self.coef_ = np.ones(X.shape[1])

        for epoch in range(self.epochs):
            # update the intercept value
            y_hat = np.dot(X, self.coef_) + self.intercept_
            intercept_der = -2 * np.mean(y - y_hat)
            self.intercept_ = self.intercept_ - ( self.learning_rate * intercept_der )

            # update the coefficients
            coeff_der = -2 * np.dot(y - y_hat, X) / X.shape[0]
            self.coef_ = self.coef_ - ( self.learning_rate * coeff_der )

    def predict(self, X: np.ndarray):
        return np.dot( X, self.coef_ ) + self.intercept_


if __name__ == "__main__":
    gdr = GDRegressor()
    X = np.random.rand(10, 2)
    y = np.zeros((10,))
    print(X)
    print(y)
    gdr.fit(X, y)
    print(gdr.coef_, gdr.intercept_)