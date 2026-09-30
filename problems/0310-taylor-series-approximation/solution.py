import numpy as np
from math import factorial

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    
    total=0
    for i in range(n_terms):
        if func_name=="exp":
            total+=x**i/factorial(i)
        if func_name=='sin':
            total+=(((-1)**i)*x**(2*i+1))/factorial(2*i+1)
        if func_name=='cos':
            total+=(((-1)**i)*x**(2*i))/factorial(2*i)
    return round(total,6)