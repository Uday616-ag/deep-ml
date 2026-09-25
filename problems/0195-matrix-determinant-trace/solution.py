import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	matrix=np.array(matrix)
	det=np.linalg.det(matrix)
	trace=np.trace(matrix)
	return (det,trace)
	pass