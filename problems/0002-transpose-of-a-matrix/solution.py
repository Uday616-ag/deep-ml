def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row=len(a[0])
    col=len(a)
    res=[]
    for i in range(row):
        lst=[]
        for j in range(col):
            lst.append(a[j][i])
        res.append(lst)
    return res 
    pass