def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    row =len(matrix)
    col=len(matrix[0])
    det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    inv=[]
    if det==0:
        return None
    else:
        for i in range(col,0,-1):
            cof=[]
            for j in range(row,0,-1):
                cof.append((-1)**(i+j)*((matrix[j-1][i-1])/det))
            inv.append(cof)
        return inv
    pass