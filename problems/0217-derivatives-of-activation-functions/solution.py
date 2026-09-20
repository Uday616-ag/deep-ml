import math
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	sig_der=(1/(1+math.exp(-x)))*(1-1/(1+math.exp(-x)))
	relu=1 if x>0 else 0
	tanh=1-(math.exp(x)-math.exp(-x))**2/(math.exp(x)+math.exp(-x))**2
	return {'sigmoid':sig_der,'tanh':tanh,'relu':relu}