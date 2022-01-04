import sage.all  # noqa: F401 (required by sage)
from sage.matrix.special import random_matrix


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
    return random_matrix(
        ring,
        order,
        algorithm="echelonizable",
        rank=order,
        max_tries=None,
    )
