def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    total=len(data)
    tot_x=0
    tot_xy=0
    for i in data:
      var_x=i[0]
      if var_x==x:
        tot_x+=1
    for i in data:
      var_x=i[0]
      var_xy=i[1]
      if var_x==x and var_xy==y:
        tot_xy+=1
    if tot_x==0:
      return 0
    prob_x=tot_x/total
    prob_xy=tot_xy/total
    return round(prob_xy/prob_x,4)