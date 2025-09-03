import numpy as np

def basisnl(nmin, nmax):
    for n in range(nmin, nmax + 1):
        for l in range(0, n):
            yield n, l


