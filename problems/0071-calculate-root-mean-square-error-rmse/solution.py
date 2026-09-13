import numpy as np

def rmse(y_true, y_pred):
    mse = np.mean((y_true - y_pred) ** 2)
    return round(np.sqrt(mse),3)