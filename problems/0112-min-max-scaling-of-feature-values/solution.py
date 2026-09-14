def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    low=min(x)
    hgh=max(x)
    out=[]
    for i in x:
        out.append((i-low)/(hgh-low))
    return out
    pass