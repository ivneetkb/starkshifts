from abc import ABC, abstractmethod
import numpy as np

class Matrix(ABC):

    @abstractmethod
    def generate_matrix(self):
        """ Generate the matrix representation of a given operator."""
        pass

    def generate_basis_states(self, **kwargs):
        """ Generate list of basis states where the arguments decide the quantum numbers."""
        states = []
        lookuptable = {}
        index = 0
        for state in self.basis(**kwargs):
            states.append(state)
            lookuptable[state] = index
            index +=1
        return states, lookuptable
    
    def convert_state_to_index(self,state):
        return self.lookuptable[state]
    
    def convert_states_to_index(self, state1, state2):
        return self.lookuptable[state1], self.lookuptable[state2]
    
    def convert_index_to_state(self, index):
        return self.states[index]
    
    def convert_indices_to_states(self, index1, index2):
        return self.states[index1], self.states[index2]
    
    def __repr__(self):
        return str(self.matrix)
    
    def __getitem__(self, index):
        return self.matrix(index)