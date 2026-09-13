def selu(x: float) -> float:
	"""
	Implements the SELU (Scaled Exponential Linear Unit) activation function.

	Args:
		x: Input value

	Returns:
		SELU activation value
	"""
	import math
	alpha = 1.6732632423543772
	scale = 1.0507009873554804
	# Your code here
	mul=alpha*scale
	if x>0:
		return scale*x
	else:
	    return mul*(math.exp(x)-1)
	pass