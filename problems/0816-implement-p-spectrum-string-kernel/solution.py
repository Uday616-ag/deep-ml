def string_kernel(s: str, t: str, p: int) -> int:
    """
    Compute the p-spectrum string kernel between two strings.
    """
    lst_s=[]
    lst_t=[]
    for i in range(len(s)-p+1):
        comp=s[i:i+p]
        lst_s.append(comp)

    for i in range(len(t)-p+1):
        comp=t[i:i+p]
        lst_t.append(comp)
    
    total=0

    for i in range(len(lst_s)):
        for j in range(len(lst_t)):
            if lst_s[i]==lst_t[j]:
                total+=1
    
    return total
        