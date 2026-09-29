import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:

    arr_p=np.array(p)
    arr_q=np.array(q)
    sp=arr_p.size
    sq=arr_q.size
    if sp!=sq:
        return 0
    if sp==0 or sq==0:
        return 0
    total=np.sum(np.sqrt(arr_p*arr_q))
    return np.round((-np.log(total)),4)