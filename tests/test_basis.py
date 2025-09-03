from starkshifts.basis import basisnl
import pytest

def test_basis():
    nmin = 1
    nmax = 3
    basis = list(basisnl(nmin, nmax))

    basis_compare = []
    for n in range(nmin, nmax + 1):
        for l in range(0, n):
            basis_compare.append((n,l))

    assert basis == basis_compare
    
def test_basis_size():
    nmin = 1
    nmax = 3
    basis = list(basisnl(nmin, nmax))

    assert len(basis) == 6

def test_invalid_basisnl():
    with pytest.raises(ValueError):
        list(basisnl(3, 1))
