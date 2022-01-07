from pqcrypto.coding.rank_metric import random_vector, rank_weight
from pqcrypto.algebra.finite_field import finite_field

from contextlib import nullcontext
from pytest import mark, raises


@mark.parametrize(
    "field, degree, weight, context",
    [
        (finite_field(2), 0, 0, nullcontext()),
        (finite_field(2), 1, 1, nullcontext()),
        (finite_field(2), 0, 1, raises(ValueError)),
        (finite_field(2 ** 2), 3, 0, nullcontext()),
        (finite_field(2 ** 2), 3, 2, nullcontext()),
        (finite_field(2 ** 2), 3, 3, raises(ValueError)),
        (finite_field(2 ** 3), 2, 3, raises(ValueError)),
    ],
)
def test_random_vector(field, degree, weight, context):
    with context:
        v = random_vector(field, degree, weight)

        assert v.base_ring() is field
        assert rank_weight(v) == weight
