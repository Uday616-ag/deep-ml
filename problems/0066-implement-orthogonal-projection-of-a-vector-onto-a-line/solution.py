import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v=np.array(v)
	L=np.array(L)
	proj_v=(np.dot(v,L)/np.linalg.norm(L)**2)*L
	return proj_v.tolist()
	pass
