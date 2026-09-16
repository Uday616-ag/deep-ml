import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:

    arr_C = np.array(C, dtype=float)
    arr_B = np.array(B, dtype=float)

    inv_C = np.linalg.inv(arr_C)

    arr_P = inv_C @ arr_B

    return arr_P.tolist()
	