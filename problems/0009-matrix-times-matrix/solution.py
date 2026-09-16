def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    row1=len(a)            
    row2=len(b)
    col1=len(a[0])            
    col2=len(b[0])
    c=[]
    if col1!=row2:
        return -1
    for i in range(row1):
        lst=[]
        for  j in range(col2):
            total=0
            for k in range(col1):
                total+=a[i][k]*b[k][j]
            lst.append(total)
        c.append(lst)       
    return c