def hard_voting_classifier(predictions: list[list[int]]) -> list[int]:
    """
    Implement a hard voting classifier using majority vote.
    
    Args:
        predictions: 2D list where predictions[i][j] is classifier i's prediction for sample j
        
    Returns:
        List of final predictions using majority vote
    """
    row=len(predictions)
    col=len(predictions[0])
    hard_vote=[]
    for i in range(col):
        temp=[]
        val0=0
        val1=0
        val2=0
        for j in range(row):
            if predictions[j][i]==0:
                val0+=1
            elif predictions[j][i]==1:
                val1+=1
            elif predictions[j][i]==2:
                val2+=1
        temp.extend([val0,val1,val2])
        if max(temp)==val0:
            hard_vote.append(0)
        elif max(temp)==val1:
            hard_vote.append(1)
        elif max(temp)==val2:
            hard_vote.append(2)
        
    return hard_vote
