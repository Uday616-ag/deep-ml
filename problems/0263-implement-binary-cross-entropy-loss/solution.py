import numpy as np
def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
	length=len(y_true)
	y_true=np.array(y_true)
	y_pred=np.array(y_pred)
	loss=np.sum(-(y_true*np.log(y_pred)+(1-y_true)*np.log(1-y_pred)))
	return loss/length