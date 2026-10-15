import jax
import jax.numpy as jnp

def replace_at(x, indices, values):
    """Return a copy of 1-D array x with x[indices] replaced by values.
    Must not modify x."""
    y=x
    
    for i in range(len(indices)):
        y=y.at[indices[i]].set(values[i])
    
    

    return y
