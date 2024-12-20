import utils


def encode(tG, v, snr, seed=None):
    """Encode a binary message and adds Gaussian noise.

    Parameters
    ----------
    tG: array or scipy.sparse.csr_matrix (m, k). Transposed coding matrix
    obtained from `pyldpc.make_ldpc`.

    v: array (k, ) or (k, n_messages) binary messages to be encoded.

    snr: float. Signal-Noise Ratio. SNR = 10log(1 / variance) in decibels.

    Returns
    -------
    y: array (n,) or (n, n_messages) coded messages + noise.

    """
    n, k = tG.shape

    rng = utils.check_random_state(seed)
    d = utils.binaryproduct(tG, v)
    x = (-1) ** d

    sigma = 10 ** (- snr / 20)
    e = rng.randn(*x.shape) * sigma

    y = x + e

    return y
