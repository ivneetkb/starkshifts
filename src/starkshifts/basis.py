import numpy as np


def basisnl(nmin, nmax):

    if nmax < nmin:
        raise ValueError(f"Invalid range: nmax ({nmax}) cannot be less than nmin ({nmin})")
    
    for n in range(nmin, nmax + 1):
        for l in range(0, n):
            yield n, l
