def hardtanh(x: float, min_val: float = -1.0, max_val: float = 1.0) -> float:
	return max(min_val,min(x,max_val))