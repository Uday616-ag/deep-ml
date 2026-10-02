import numpy as np

def compute_cross_entropy_loss(predicted_probs, true_labels, epsilon=1e-15):
    predicted_probs = np.array(predicted_probs)
    true_labels = np.array(true_labels)

    predicted_probs = np.clip(predicted_probs, epsilon, 1 - epsilon)

    cross_ent = np.sum(-np.log(predicted_probs) * true_labels)

    return cross_ent / len(true_labels)