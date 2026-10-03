import numpy as np

def cramers_rule(A, b):
    # Your code here
    arr_A=np.array(A)
    det_a=np.linalg.det(arr_A)
    if det_a==0:
        return -1
    
    lst_temp=[]

    for i in range(len(A)):
        arr_temp=arr_A.copy()
        arr_temp[:, i]=b
        lst_temp.append(np.linalg.det(arr_temp)/det_a)
    return lst_temp