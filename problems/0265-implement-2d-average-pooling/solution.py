import numpy as np
def avg_pool_2d(input_matrix: list[list[float]], pool_size: int) -> list[list[float]]:
	inp_mat=np.array(input_matrix)
	lst=[]
	new_height=len(input_matrix)-pool_size
	for i in range(0,new_height+1,pool_size):
		temp=[]
		for j in range(0,new_height+1,pool_size):
			win_mat=inp_mat[
				i:i+pool_size,
				j:j+pool_size
			]
			temp.append(np.mean(win_mat).tolist())
		lst.append(temp)
	return lst