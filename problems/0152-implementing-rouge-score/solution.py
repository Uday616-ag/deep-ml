# Implement your function below.

def rouge_1_score(reference: str, candidate: str) -> dict:
    """
    Compute ROUGE-1 score between reference and candidate texts.
    
    Returns a dictionary with precision, recall, and f1.
    """
    reference=reference.split()
    candidate=candidate.split()
    total=0
    for words in reference:
        if words in candidate:
            total+=1
    recall=total/len(reference)
    precision=total/len(candidate)
    f1=2*((recall*precision)/(recall+precision))
    return {'precision':precision,
             'recall':recall,
             'f1':f1}


