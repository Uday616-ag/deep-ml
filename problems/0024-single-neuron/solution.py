import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	row=len(features)
	col=len(features[0])
	probabilities=[]
	mse=0
	for i in range(row):
		total=0
		for j in range(col):
			total+=features[i][j]*weights[j]
		total+=bias
		probabilities.append(round(1/(1+math.exp(-total)),4))
	for i in range(row):
		mse+=(labels[i]-probabilities[i])**2
	return probabilities, round(mse/row,4)