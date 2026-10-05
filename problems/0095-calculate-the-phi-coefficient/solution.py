def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	if len(x)!=len(y):
		return -1
	a=0
	b=0
	c=0
	d=0
	for i in range(len(x)):
		if x[i]==1 and y[i]==1:
			a+=1
		elif x[i]==1 and y[i]==0:
			b+=1
		elif x[i]==0 and y[i]==1:
			c+=1
		elif x[i]==0 and y[i]==0:
			d+=1
	
	deno=((a+b)*(c+d)*(a+c)*(b+d))**0.5
	if deno==0:
		return 0
	val=(a*d-b*c)/deno
	return round(val,4)