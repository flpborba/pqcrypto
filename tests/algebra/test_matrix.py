from pqcrypto.algebra.finite_field import finite_field
from pqcrypto.algebra.matrix import random_invertible_matrix

from pytest import mark


@mark.parametrize(
    "field, order",
    [
        (finite_field(2), 0),
        (finite_field(2), 1),
        (finite_field(2), 3),
        (finite_field(2 ** 2), 0),
        (finite_field(2 ** 2), 1),
        (finite_field(2 ** 2), 2),
        (finite_field(2 ** 3), 0),
        (finite_field(2 ** 3), 1),
        (finite_field(2 ** 3), 2),
    ],
)
def test_random_invertible_matrix(field, order):
    m = random_invertible_matrix(field, order)

    assert m.nrows() == order
    assert m.ncols() == order
    assert m.rank() == order
