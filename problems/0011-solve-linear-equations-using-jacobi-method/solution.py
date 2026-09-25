import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(b))

    for i in range(n):
        x_new = np.zeros(len(b))

        for j in range(len(b)):
            sum_val = 0

            for k in range(len(b)):
                if k != j:
                    sum_val += A[j, k] * x[k]

            x_new[j] = (b[j] - sum_val) / A[j, j]

        x = x_new

    return x