import numpy as np
from starkshifts.matrix import Matrix
from starkshifts.basis import basisnl

class Matrix_nl(Matrix):
    def __init__(self, nmin, nmax, lmax=None):
        self.basis = basisnl
        self.states, self.lookuptable = self.generate_basis_states(nmin=nmin, nmax=nmax, lmax=lmax)
        self.matrix = self.generate_matrix() 

    def generate_matrix(self):
        matrix = np.zeros((len(self.states), len(self.states)))
        return matrix