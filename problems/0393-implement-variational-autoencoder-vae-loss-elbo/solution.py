import numpy as np

def vae_loss(x: np.ndarray, x_reconstructed: np.ndarray, mu: np.ndarray, log_var: np.ndarray) -> tuple:
    """
    Compute the VAE loss (negative ELBO).

    Args:
        x: np.ndarray of shape (batch_size, features), original input
        x_reconstructed: np.ndarray of shape (batch_size, features), reconstructed input
        mu: np.ndarray of shape (batch_size, latent_dim), latent mean
        log_var: np.ndarray of shape (batch_size, latent_dim), latent log-variance

    Returns:
        tuple: (total_loss, reconstruction_loss, kl_divergence) as floats
    """
    reconst_loss=(x-x_reconstructed)**2
    avg_reconst_loss=np.sum(reconst_loss)/len(x)

    kl_loss=(-0.5)*(1+log_var-mu**2-np.exp(log_var))
    avg_kl_loss=np.sum(kl_loss)/len(x)

    total_loss=avg_reconst_loss.tolist()+avg_kl_loss.tolist()

    return (total_loss,avg_reconst_loss,avg_kl_loss)