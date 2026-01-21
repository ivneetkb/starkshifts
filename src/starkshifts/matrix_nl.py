import numpy as np
from typing import Optional, Callable, Iterable, Tuple
from starkshifts.matrix import matrix
from starkshifts.basis import basisnl

State = Tuple[int, int]


class matrix_nl(matrix):
    def __init__(self, nmin: int, nmax: int, lmax: Optional[int] = None) -> None:
        self.basis: Callable[..., Iterable[State]] = basisnl
        self.states, self.lookuptable = self.generate_basis_states(
            nmin=nmin, nmax=nmax, lmax=lmax
        )
        self.matrix = self.generate_matrix()

    def generate_matrix(self) -> np.ndarray:
        mat = np.zeros((len(self.states), len(self.states)))
        return mat
