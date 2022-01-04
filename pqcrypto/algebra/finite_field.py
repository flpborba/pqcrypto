import sage.all  # noqa: F401 (required by sage)
from sage.rings.finite_rings.finite_field_constructor import GF


def finite_field(order):
    """Create a finite field.

    Parameters
    ----------
    order : int
        Finite field order.

    Returns
    -------
    FiniteField
    """
    return GF(order)
