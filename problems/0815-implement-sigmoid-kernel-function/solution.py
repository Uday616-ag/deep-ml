import numpy as np

def sigmoid_kernel(X1, X2, alpha=0.01, c=0.0):
    """
    Compute the sigmoid kernel matrix between rows of X1 and rows of X2.

    Args:
        X1: numpy array of shape (n, d)
        X2: numpy array of shape (m, d)
        alpha: float, slope parameter
        c: float, intercept (constant) parameter

    Returns:
        Nested list of shape (n, m) with entries rounded to 4 decimals.
    """
    arr_x1=np.array(X1)
    arr_x2=np.array(X2)

    fun_in=alpha*(arr_x1 @ arr_x2.T)+c 
    kernel_out=np.round(np.tanh(fun_in),4)
    return kernel_out.tolist()

