def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	total=[]
	if len(a)!=len(b):
		return -1
	for i in range(len(a)):
		tot=a[i]+b[i]
		total.append(tot)
	return total