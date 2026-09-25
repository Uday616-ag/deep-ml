import numpy as np

def SwiGLU(x: np.ndarray) -> np.ndarray:
    """
    Args:
        x: np.ndarray of shape (batch_size, 2d)
    Returns:
        np.ndarray of shape (batch_size, d)
    """
    x1,x2=np.split(x, 2,axis=1)
    swish=x2*(1/(1+np.exp(-x2)))
    scores=x1*swish
    
        
    # Your code here
    return scores