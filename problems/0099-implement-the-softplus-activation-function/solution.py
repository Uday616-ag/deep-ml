import math
def softplus(x: float) -> float:
	"""
	Compute the softplus activation function.

	Args:
		x: Input value

	Returns:
		The softplus value: log(1 + e^x)
	"""
	# Your code here
	val=math.log(1+math.exp(x))
	return round(val,4)