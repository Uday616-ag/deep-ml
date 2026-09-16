import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	mat=np.array(matrix,dtype=float)
	eigenvalues=np.linalg.eigvals(mat)
	return eigenvalues.tolist()