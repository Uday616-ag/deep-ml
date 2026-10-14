
import numpy as np

def simple_self_attention(X: list[list[float]]) -> list[list[float]]:
    """
    Compute context vectors using simple self-attention (no trainable weights).
    """

    arr_x = np.array(X, dtype=float)

    # Step 1: Calculate attention scores
    scores_mat = arr_x @ arr_x.T

    # Step 2: Apply softmax to each row of attention scores
    exp_scores = np.exp(scores_mat - np.max(scores_mat, axis=1, keepdims=True))
    attention_weights = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    # Step 3: Calculate context vectors
    context_vectors = attention_weights @ arr_x

    return context_vectors.tolist()

