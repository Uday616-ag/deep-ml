import numpy as np
def to_categorical(x, n_col=None):

    if n_col is None:
        n_col = np.max(x) + 1

    encode = np.zeros((len(x), n_col))

    for i, value in enumerate(x):
        encode[i, value] = 1

    return encode