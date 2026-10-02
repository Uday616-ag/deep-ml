import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""

	x=point[0]
	y=point[1]
	z=0

	if len(point)==3:
		z=point[2]


	pol_2dx=2*x*y+y**2
	pol_2dy=x**2+2*x*y

	exp_dx=np.exp(x+y)
	exp_dy=np.exp(x+y)

	pro_dx=np.sin(y)
	pro_dy=x*np.cos(y)

	poly_dx=2*x*y
	poly_dy=x**2+z**2
	poly_dz=2*z*y

	sq_dx=2*(x-y)
	sq_dy=(-2*(x-y))
		
	if func_name=="poly2d":
		return (pol_2dx,pol_2dy)
	elif func_name=="exp_sum":
		return (exp_dx,exp_dy)
	elif func_name=="product_sin":
		return (pro_dx,pro_dy)
	elif func_name=="poly3d":
		return (poly_dx,poly_dy,poly_dz)
	elif func_name=="squared_error":
		return (sq_dx,sq_dy)