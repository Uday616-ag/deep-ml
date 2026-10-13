import numpy as np

def lora_forward(
	x: list[list[float]],
	W: list[list[float]],
	A: list[list[float]],
	B: list[list[float]],
	alpha: float = 1.0
) -> list[list[float]]:
	"""
	Compute the LoRA forward pass.
	
	Args:
		x: Input matrix (batch_size x in_features)
		W: Frozen pretrained weights (in_features x out_features)
		A: LoRA matrix A (rank x out_features)
		B: LoRA matrix B (in_features x rank)
		alpha: LoRA scaling factor
		
	Returns:
		Output matrix (batch_size x out_features)
	"""
	arr_x=np.array(x)
	arr_w=np.array(W)
	arr_a=np.array(A)
	arr_b=np.array(B)
	rank=len(arr_a)
	out_arr=arr_x@ (arr_w+(alpha/rank)*(arr_b @ arr_a))
	return out_arr.tolist()