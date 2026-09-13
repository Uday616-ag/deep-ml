import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    tp=0
    fn=0
    for i in range(len(y_true)):
        if y_true[i]==1 and y_pred[i]==1:
            tp+=1
        elif y_true[i]==1 and y_pred[i]==0:
            fn+=1
    total=tp+fn
    if total==0:
        return 0
    return tp/total
    pass
