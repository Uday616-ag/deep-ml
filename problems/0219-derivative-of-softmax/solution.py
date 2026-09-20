import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:

    length = len(x)
    x = np.array(x)

    # Calculate softmax
    exp_x = np.exp(x)
    softmax = exp_x / np.sum(exp_x)

    jac_mat = []

    for i in range(length):

        lst = []

        for j in range(length):

            if i == j:
                lst.append(softmax[i] * (1 - softmax[i]))

            else:
                lst.append(-softmax[i] * softmax[j])

        jac_mat.append(lst)

    return jac_mat