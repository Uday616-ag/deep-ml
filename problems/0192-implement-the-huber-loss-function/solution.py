import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    error = np.abs(y_true - y_pred)

    loss = np.where(
        error <= delta,
        0.5 * error**2,
        delta * (error - 0.5 * delta)
    )

    return np.mean(loss)