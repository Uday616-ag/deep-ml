import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp=0
	fp=0
	length=len(y_true)
	for i in range(length):
		if y_true[i]==1 and y_pred[i]==1:
			tp+=1
		elif y_true[i]==0 and y_pred[i]==1:
			fp+=1
	total=tp+fp
	if total==0:
		return 0
	return tp/total
	pass
