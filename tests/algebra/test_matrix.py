from pqcrypto.algebra.finite_field import finite_field
from pqcrypto.algebra.matrix import random_invertible_matrix, random_matrix

from contextlib import nullcontext
from pytest import mark, raises


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


@mark.parametrize(
    "field, nrows, ncols, rank, context",
    [
        (finite_field(2), 0, 0, 0, nullcontext()),
        (finite_field(2), 0, 0, 1, raises(ValueError)),
        (finite_field(2), 1, 1, 0, nullcontext()),
        (finite_field(2), 1, 1, 1, nullcontext()),
        (finite_field(2), 1, 1, 2, raises(ValueError)),
        (finite_field(2 ** 2), 2, 3, 0, nullcontext()),
        (finite_field(2 ** 2), 3, 2, 2, nullcontext()),
        (finite_field(2 ** 2), 2, 3, 3, raises(ValueError)),
        (finite_field(2 ** 3), 2, 2, 3, raises(ValueError)),
        (finite_field(2 ** 2), 3, None, 3, nullcontext()),
        (finite_field(2 ** 2), 3, 2, None, nullcontext()),
    ],
)
def test_random_matrix(field, nrows, ncols, rank, context):
    with context:
        m = random_matrix(field, nrows, ncols, rank)

        if ncols is None:
            ncols = nrows

        assert m.nrows() == nrows
        assert m.ncols() == ncols

        if rank is not None:
            assert m.rank() == rank
