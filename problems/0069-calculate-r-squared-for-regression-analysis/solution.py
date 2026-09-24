
import numpy as np

def r_squared(y_true, y_pred):
	true_mean=np.mean(y_true)
	SSres=np.sum((y_true-y_pred)**2)
	SStot=np.sum((y_true-true_mean)**2)
	return (1-SSres/SStot)
