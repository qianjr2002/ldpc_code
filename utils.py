import numbers
import numpy as np
import scipy


def check_random_state(seed):
    """Turn seed into a np.random.RandomState instance
    Parameters
    ----------
    seed : None | int | instance of RandomState
        If seed is None, return the RandomState singleton used by np.random.
        If seed is an int, return a new RandomState instance seeded with seed.
        If seed is already a RandomState instance, return it.
        Otherwise raise ValueError.
    """
    if seed is None or seed is np.random:
        return np.random.mtrand._rand
    if isinstance(seed, numbers.Integral):
        return np.random.RandomState(seed)
    if isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError('%r cannot be used to seed a numpy.random.RandomState'
                     ' instance' % seed)


def gaussjordan(X, change=0):
    """Compute the binary row reduced echelon form of X.

    Parameters
    ----------
    X: array (m, n)
    change : boolean (default, False). If True returns the inverse transform

    Returns
    -------
    if `change` == 'True':
        A: array (m, n). row reduced form of X.
        P: tranformations applied to the identity
    else:
        A: array (m, n). row reduced form of X.

    """
    A = np.copy(X)
    m, n = A.shape

    if change:
        P = np.identity(m).astype(int)

    pivot_old = -1
    for j in range(n):
        filtre_down = A[pivot_old+1:m, j]
        pivot = np.argmax(filtre_down)+pivot_old+1

        if A[pivot, j]:
            pivot_old += 1
            if pivot_old != pivot:
                aux = np.copy(A[pivot, :])
                A[pivot, :] = A[pivot_old, :]
                A[pivot_old, :] = aux
                if change:
                    aux = np.copy(P[pivot, :])
                    P[pivot, :] = P[pivot_old, :]
                    P[pivot_old, :] = aux

            for i in range(m):
                if i != pivot_old and A[i, j]:
                    if change:
                        P[i, :] = abs(P[i, :]-P[pivot_old, :])
                    A[i, :] = abs(A[i, :]-A[pivot_old, :])

        if pivot_old == m-1:
            break

    if change:
        return A, P
    return A


def binaryproduct(X, Y):
    """Compute a matrix-matrix / vector product in Z/2Z."""
    A = X.dot(Y)
    try:
        A = A.toarray()
    except AttributeError:
        pass
    return A % 2


def _bitsandnodes(H):
    """Return bits and nodes of a parity-check matrix H."""
    if type(H) != scipy.sparse.csr_matrix:
        bits_indices, bits = np.where(H)
        nodes_indices, nodes = np.where(H.T)
    else:
        bits_indices, bits = scipy.sparse.find(H)[:2]
        nodes_indices, nodes = scipy.sparse.find(H.T)[:2]
    bits_histogram = np.bincount(bits_indices)
    nodes_histogram = np.bincount(nodes_indices)

    return bits_histogram, bits, nodes_histogram, nodes


def incode(H, x):
    """Compute Binary Product of H and x."""
    return (binaryproduct(H, x) == 0).all()


def gausselimination(A, b):
    """Solve linear system in Z/2Z via Gauss Gauss elimination."""
    if type(A) == scipy.sparse.csr_matrix:
        A = A.toarray().copy()
    else:
        A = A.copy()
    b = b.copy()
    n, k = A.shape

    for j in range(min(k, n)):
        listedepivots = [i for i in range(j, n) if A[i, j]]
        if len(listedepivots):
            pivot = np.min(listedepivots)
        else:
            continue
        if pivot != j:
            aux = (A[j, :]).copy()
            A[j, :] = A[pivot, :]
            A[pivot, :] = aux

            aux = b[j].copy()
            b[j] = b[pivot]
            b[pivot] = aux

        for i in range(j+1, n):
            if A[i, j]:
                A[i, :] = abs(A[i, :]-A[j, :])
                b[i] = abs(b[i]-b[j])

    return A, b
