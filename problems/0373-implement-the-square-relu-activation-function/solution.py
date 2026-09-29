import numpy as np

def square_relu(x: np.ndarray) -> dict:
    output = np.maximum(0, x) ** 2
    derivative = np.where(x > 0, 2 * x, 0)

    return {
        "output": np.round(output,4),
        "derivative": derivative
    }