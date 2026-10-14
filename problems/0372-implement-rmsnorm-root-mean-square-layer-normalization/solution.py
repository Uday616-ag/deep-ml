import numpy as np

def rmsnorm(x: np.ndarray, g: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    """
    Apply RMSNorm to the input array.
    
    Parameters:
        x   : np.ndarray of shape (batch_size, features)
        g   : np.ndarray of shape (features,) - gain parameter
        eps : float - small constant for numerical stability
    
    Returns:
        np.ndarray of same shape as x
    """
    sqroot_arr=np.sqrt((np.mean(x**2,axis=1,keepdims=True)+eps))
    norm_x=x/sqroot_arr
    out_norm=norm_x*g
    return out_norm