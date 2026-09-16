import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:

    X=np.array(X)

    y=np.array(y)

    beta=np.linalg.inv(X.T @ X)@ X.T@ y

    return [round(float(value),4) for value in beta]
    