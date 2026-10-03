import numpy as np
def gini_impurity(y):
	arr=np.array(y)
	unique=np.unique(arr)
	gini=1

	total=len(y)
	counts=0

	for i in unique:
		counts=np.sum(arr==i)
		gini-=(counts/total)**2

	return round(gini,3)
