import sage.all  # noqa: F401 (required by sage)
from sage.matrix.special import random_matrix as sage_random_matrix


def random_invertible_matrix(ring, order):
    """Generate a random invertible matrix.

    Parameters
    ----------
    ring : Ring
        Base ring of matrix elements.
    order : int
        Matrix order.

    Returns
    -------
    Matrix
    """
    return random_matrix(ring, order, rank=order)


def random_matrix(ring, nrows, ncols=None, rank=None):
    """Generate a random matrix.

    Parameters
    ----------
    ring : Ring
        Base ring of matrix elements.
    nrows : int
        Number of rows in the matrix.
    ncols : int, optional
        Number of columns in the matrix (if `None`, the number of columns is the
        same as the number of rows).
    rank : int, optional
        The rank of the matrix (if `None`, the matrix will not have any special
        rank).
    """
    if rank is None:
        return sage_random_matrix(ring, nrows, ncols)

    return sage_random_matrix(
        ring,
        nrows,
        ncols,
        algorithm="echelonizable",
        rank=rank,
        max_tries=None,
    )
