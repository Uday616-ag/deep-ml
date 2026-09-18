
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	tp=0
	fp=0
	fn=0
	for i in range(len(y_true)):
		if y_pred[i]==1 and y_true[i]==1:
			tp+=1
		elif y_pred[i]==1 and y_true[i]==0:
			fp+=1
		elif y_pred[i]==0 and y_true[i]==1:
			fn+=1
	if (tp+fn+fp)==0:
		return 0
	res=2*tp/(2*tp+fn+fp)
	
	return round(res, 3)
