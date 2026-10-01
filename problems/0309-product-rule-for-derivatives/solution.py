import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    result=[0]*(len(f_coeffs)+len(g_coeffs)-1)
    for i in range(len(f_coeffs)):
        for j in range(len(g_coeffs)):
            result[i+j]+=f_coeffs[i]*g_coeffs[j]
    if len(result)==1:
        return 0  
    final=[]
    for i in range(1,len(result)):
        final.append(i*result[i])
    return final