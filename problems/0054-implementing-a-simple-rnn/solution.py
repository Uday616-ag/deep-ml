import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state:list[float],Wx:list[list[float]],Wh:list[list[float]],b:list[float]) ->list[float]:
	# Your code here
    x=np.array(input_sequence)

    h=np.array(initial_hidden_state)

    Wx=np.array(Wx)

    Wh=np.array(Wh)

    b=np.array(b)

    for i in x:

        h=np.tanh(Wx@ i.T+Wh@ h+b)

    return np.round(h,4)