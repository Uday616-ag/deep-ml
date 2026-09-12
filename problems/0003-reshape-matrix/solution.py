import numpy as np

def reshape_matrix(
    a: list[list[int | float]],
    new_shape: tuple[int, int]
) -> list[list[int | float]]:

    row = len(a)
    col = len(a[0])

    rt = new_shape[0]
    ct = new_shape[1]

    if row == ct and col == rt:
        matrix = np.array(a)
        result = matrix.reshape(new_shape)
        return result.tolist()
    elif row==rt and col==ct:
        return a
    else:
        return []