import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	vmx=np.max(data,axis=0)
	vmn=np.min(data,axis=0)
	vmean=np.mean(data,axis=0)
	vstd=np.std(data,axis=0)
	standardized_data=(data-vmean)/vstd
	normalized_data=(data-vmn)/(vmx-vmn)
	return standardized_data.tolist(), normalized_data.tolist()