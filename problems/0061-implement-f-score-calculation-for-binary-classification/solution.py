import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp=0
	fn=0
	fp=0
	for i in range(len(y_true)):
		if y_true[i]==1 and y_pred[i]==1:
			tp+=1
		elif y_true[i]==1 and y_pred[i]==0:
			fn+=1
		elif y_true[i]==0 and y_pred[i]==1:
			fp+=1
	t1=tp+fn
	t2=tp+fp
	pre=tp/t2
	re=tp/t1
	return round((1+beta**2)*(pre*re)/(re+beta**2*pre),3)
	pass
