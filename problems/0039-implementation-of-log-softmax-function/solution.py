import numpy as np
import math
def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	tot=0
	lst=[]
	soft=[]
	for i in scores:
		tot+=math.exp(i)
	for i in scores:
		lst.append(math.exp(i)/tot)
	for i in lst:
		soft.append(math.log(i))
	return np.array(soft) 
	pass