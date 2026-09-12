import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	length=len(y_true)
	predict=0
	for i in range(length):
		if y_true[i]==y_pred[i]:
			predict=predict+1
	return predict/length
	pass