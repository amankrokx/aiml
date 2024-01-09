import matplotlib.pyplot as plt
import numpy as np


def local_regression(x0, X, Y, tau):
    X = np.c_[np.ones_like(X), X]
    x0 = np.array([1, x0])

    xw = np.diag(np.exp(-np.sum((X - x0) ** 2, axis=1) / (2 * tau)))
    beta = np.linalg.inv(X.T @ xw @ X) @ X.T @ xw @ Y
    return x0 @ beta

def draw(tau):
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
    plt.plot(X, Y, 'o', color='black')
    plt.plot(domain, prediction, color='red')
    plt.show()

X = np.linspace(-3, 3, num=1000)
domain = X
Y = np.log(np.abs(X ** 2 - 1) + .5)

draw(10)
draw(0.01)
