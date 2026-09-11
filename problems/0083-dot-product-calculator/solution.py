import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	len1=len(vec1)
	len2=len(vec2)
	sum=0
	if len1==len2:
		for i in range(len1):
			sum+=vec1[i]*vec2[i]
	return sum
	pass