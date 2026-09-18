import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dotprod=np.dot(v1, v2)
	mag1=np.sqrt(np.sum(v1**2))
	mag2=np.sqrt(np.sum(v2**2))
	mag=mag1*mag2
	return dotprod/mag