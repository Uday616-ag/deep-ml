import numpy as np

def adam_optimizer(
    f,
    grad,
    x0,
    learning_rate=0.001,
    beta1=0.9,
    beta2=0.999,
    epsilon=1e-8,
    num_iterations=10
):
    mt = np.zeros_like(x0, dtype=float)
    vt = np.zeros_like(x0, dtype=float)

    x = np.array(x0, dtype=float)

    for i in range(1, num_iterations + 1):

        # Calculate gradient at current x
        g = grad(x)

        # First moment
        mt = beta1 * mt + (1 - beta1) * g

        # Second moment
        vt = beta2 * vt + (1 - beta2) * (g ** 2)

        # Bias correction
        mt_hat = mt / (1 - beta1 ** i)
        vt_hat = vt / (1 - beta2 ** i)

        # Update parameter
        x = x - learning_rate * mt_hat / (
            np.sqrt(vt_hat) + epsilon
        )

    return x