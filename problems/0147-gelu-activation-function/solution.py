import numpy as np
import math

def GeLU(x: np.ndarray) -> np.ndarray:
    lst = []

    for i in x:
        lst.append(
            round(
                0.5 * i * (1 + math.erf(i / math.sqrt(2))),
                4
            )
        )

    scores = np.array(lst)

    return scores