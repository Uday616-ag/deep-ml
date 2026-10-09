import numpy as np

def elo_rating_update(ratings: dict, matches: list, k_factor: float) -> dict:
    """
    Update Elo ratings based on pairwise comparison results.
    
    Args:
        ratings: Dictionary mapping model names to their current Elo ratings
        matches: List of tuples (model_a, model_b, result) where result is 'a', 'b', or 'draw'
        k_factor: The K-factor controlling rating update magnitude
    
    Returns:
        Dictionary with updated ratings for all models
    """
    for model_a,model_b,result in matches:
        rating_a=ratings[model_a]
        rating_b=ratings[model_b]

        expected_a=1/(1+10**((rating_b-rating_a)/400))
        expected_b=1-expected_a

        if result=='a':
            score_a=1
            score_b=0
        elif result=='b':
            score_a=0
            score_b=1
        elif result=='draw':
            score_a=0.5
            score_b=0.5

        ratings[model_a]=rating_a+k_factor*(score_a-expected_a)
        ratings[model_b]=rating_b+k_factor*(score_b-expected_b)
    
    return ratings
