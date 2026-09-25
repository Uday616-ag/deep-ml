def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
	tp=0
	fp=0
	fn=0
	itr=len(y_true)
	for i in range(itr):
		if y_true[i]==1 and y_pred[i]==1:
			tp+=1
		elif y_true[i]==0 and y_pred[i]==1:
			fp+=1
		elif y_true[i]==1 and y_pred[i]==0:
			fn+=1
	total=tp
	if total==0:
		return 0
	precise=tp/(tp+fp)
	recall=tp/(tp+fn)
	f1=2*(precise*recall)/(precise+recall)
	return round(f1,3)