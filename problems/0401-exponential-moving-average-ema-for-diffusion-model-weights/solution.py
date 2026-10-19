import numpy as np

def ema_update(ema_params, model_params_list, decay):
    """
    Compute the Exponential Moving Average of model parameters over training steps.
    
    Args:
        ema_params: numpy array, initial EMA parameters
        model_params_list: list of numpy arrays, model params at each training step
        decay: float, EMA decay rate in [0, 1]
    Returns:
        Final EMA parameters as a (nested) list, rounded to 4 decimal places
    """
    temp=np.array(ema_params)
    arr_param=np.array(ema_params)
    arr_params_model=np.array(model_params_list)

    for i in range(len(model_params_list)):
        temp=decay*temp+(1-decay)*arr_params_model[i]

    return temp.tolist()