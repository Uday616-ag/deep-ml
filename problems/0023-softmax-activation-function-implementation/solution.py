import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score=max(scores)
    total=0
    lst=[]
    for i in scores:
        total+=math.exp(i-max_score)
    for i in scores:
        lst.append(math.exp(i-max_score)/total)
    return lst
    pass