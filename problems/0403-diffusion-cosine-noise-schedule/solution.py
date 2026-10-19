import numpy as np

def cosine_noise_schedule(T: int, s: float = 0.008, beta_max: float = 0.999) -> dict:
    """
    Compute the cosine noise schedule for a diffusion model.
    
    Args:
        T: Total number of diffusion timesteps
        s: Small offset to prevent alpha_bar from being too small near t=0
        beta_max: Maximum value for beta clipping
    
    Returns:
        Dictionary with keys 'betas', 'alphas', 'alpha_bars',
        each containing a numpy array of length T.
    """
    noise_0=float((np.cos((s/(1+s))*(np.pi/2)))**2)
    alpha_raw=[]
    for i in range(1,T+1):
        temp_noise=float((np.cos(((i/T+s)/(1+s))*(np.pi/2)))**2)
        noise_val=temp_noise/noise_0
        alpha_raw.append(noise_val)
    
    alpha_raw.insert(0,1)
    arr_alpha_raw=np.array(alpha_raw)

    betas=[]
    

    for i in range(0,T):
        temp_beta=(1-(arr_alpha_raw[i+1]/arr_alpha_raw[i]))
        betas.append(float(np.clip(temp_beta, 0, beta_max)))
    
    arr_betas=np.array(betas)

    alphas=1-arr_betas

    alpha_bars=[]
    multi=1
    
    for i in range(len(alphas)):
        multi*=alphas[i]
        alpha_bars.append(multi)

    arr_alphas_bar=np.array(alpha_bars)

    return {'betas': arr_betas, 
            'alphas': alphas, 
            'alpha_bars': arr_alphas_bar
        }

