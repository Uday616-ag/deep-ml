def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	row=len(matrix)
	col=len(matrix[0])
	lst=[]
	for i in range(row):
		mult=[]
		for j in range(col):
			mult.append(scalar*matrix[i][j])
		lst.append(mult)
	return lst
	pass