import numpy as np

def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int
):
    features = np.array(features, dtype=float)
    labels = np.array(labels, dtype=float)
    weights = np.array(initial_weights, dtype=float)
    bias = float(initial_bias)

    mse_values = []
    m = len(labels)

    for _ in range(epochs):

        # Forward pass
        z = features @ weights + bias
        predictions = 1 / (1 + np.exp(-z))

        # MSE BEFORE update
        mse = np.mean((labels - predictions) ** 2)
        mse_values.append(round(mse, 4))

        # Error
        error = labels - predictions

        # Sigmoid derivative
        sigmoid_derivative = predictions * (1 - predictions)

        # Backpropagation
        delta = error * sigmoid_derivative

        # Batch gradients
        weight_gradient = -(2 / m) * (delta @ features)
        bias_gradient = -(2 / m) * np.sum(delta)

        # Update
        weights = weights - learning_rate * weight_gradient
        bias = bias - learning_rate * bias_gradient

    return (
        np.round(weights, 4).tolist(),
        round(bias, 4),
        mse_values
    )