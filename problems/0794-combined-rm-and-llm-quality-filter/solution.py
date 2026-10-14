import numpy as np
def combined_quality_filter(rm_scores, llm_scores):
    """
    Return a boolean list marking high-quality samples by combined RM and LLM criteria.
    """
    
    if len(rm_scores)==0:
        return []
    rm_scores=np.array(rm_scores)
    llm_scores=np.array(llm_scores)

    thresold=np.percentile(rm_scores,75)
    max_val=np.max(llm_scores)

    out_res=[]
    
    for i in range(len(rm_scores)):
        if rm_scores[i]>=thresold or llm_scores[i]==max_val:
            out_res.append(True)
        else:
            out_res.append(False)
    

    return out_res
