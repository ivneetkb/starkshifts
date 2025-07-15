from basis import basisnl

def test_basis():
    nmin = 1
    nmax = 3
    basis = list(basisnl(nmin, nmax))

    basis_compare = []
    for n in range(nmin, nmax + 1):
        for l in range(0, n):
            basis_compare.append((n,l))

    assert basis == basis_compare