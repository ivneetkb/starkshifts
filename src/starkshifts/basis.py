import numpy as np
from typing import Iterator, Tuple, Optional


def basisnl(
    nmin: int, nmax: int, lmax: Optional[int] = None
) -> Iterator[Tuple[int, int]]:
    """
    Generates quantum numbers:
    n: principal quantum number
    l: angular momentum quantum number
    """
    if nmax < nmin:
        raise ValueError(
            f"Invalid range: nmax ({nmax}) cannot be less than nmin ({nmin})"
        )

    for n in range(nmin, nmax + 1):
        for l in range(0, n):
            if lmax == None:
                yield n, l
            elif l <= lmax:
                yield n, l
            else:
                pass
