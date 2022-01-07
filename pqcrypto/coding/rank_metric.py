from pqcrypto.algebra.matrix import random_matrix
from pqcrypto.algebra.vector import vector

import sage.all  # noqa: F401 (required by sage)
from sage.coding.linear_rank_metric import rank_weight


def random_vector(field, num_of_elements, rank_weight):
    """Generate a random vector with a given rank.

    Parameters
    ----------
    field : Field
        Field of vector elements.
    num_of_elements : int
        Number of elements in the vector.
    rank_weight : int
        Rank weight of the vector.
    """
    base_field = field.base()
    field_degree = field.degree()

    if rank_weight > min(field_degree, num_of_elements):
        raise ValueError(
            "rank weight cannot be greater than the field degree or the number"
            "of elements in the vector"
        )

    m = random_matrix(
        base_field,
        num_of_elements,
        field_degree,
        algorithm="echelonizable",
        rank=rank_weight,
        max_tries=None,
    )

    if field_degree == 1:
        return vector(field, m.list())
    else:
        return vector(field, m.rows())
