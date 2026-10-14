import numpy as np

def epsilon_insensitive_loss(y_true: np.ndarray, y_pred: np.ndarray, epsilon: float) -> float:
    """
    Compute the average epsilon-insensitive loss for SVM regression.

    Args:
        y_true: Array of true target values
        y_pred: Array of predicted target values
        epsilon: Non-negative insensitivity tolerance

    Returns:
        Average epsilon-insensitive loss rounded to 4 decimal places
    """
    loss_val=np.abs(y_true-y_pred)-epsilon
    for i in range(len(loss_val)):
        if loss_val[i]<0:
            loss_val[i]=0
    final_error=np.round(np.mean(loss_val),4)
    return final_error