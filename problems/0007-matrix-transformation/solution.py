import numpy as np
def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	mat_A=np.array(A)
	mat_T=np.array(T)
	mat_S=np.array(S)
	det_T=np.linalg.det(T)
	det_S=np.linalg.det(S)
	inv_T=np.linalg.inv(T)
	if det_T!=0 and det_S!=0:
	    transformed_matrix=inv_T @ mat_A @ mat_S
	else:
		return -1
	return transformed_matrix.tolist()