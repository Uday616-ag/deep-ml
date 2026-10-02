import numpy as np

def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:

    hig_loss=1-(y_true*y_pred)
    max_list=[]
    for i in hig_loss:
        max_list.append(max(0,i.tolist()))
    return sum(max_list)/len(max_list)