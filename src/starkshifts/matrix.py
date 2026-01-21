from abc import ABC, abstractmethod
import numpy as np
from numpy.typing import NDArray
from typing import Callable, Iterable, List, Dict, Tuple, Any

State = Tuple[int, ...]


class matrix(ABC):
    basis: Callable[..., Iterable[State]]
    states: List[State]
    lookuptable: Dict[State, int]
    matrix: NDArray[np.float64]

    @abstractmethod
    def generate_matrix(self) -> NDArray[np.float64]:
        """Generate the matrix representation of a given operator."""
        pass

    def generate_basis_states(self, **kwargs) -> Tuple[List[State], Dict[State, int]]:
        """Generate list of basis states where the arguments decide the quantum numbers."""
        states: List[State] = []
        lookuptable: Dict[State, int] = {}
        index = 0
        for state in self.basis(**kwargs):
            states.append(state)
            lookuptable[state] = index
            index += 1
        return states, lookuptable

    def convert_state_to_index(self, state: State) -> int:
        return self.lookuptable[state]

    def convert_states_to_index(self, state1: State, state2: State) -> Tuple[int, int]:
        return self.lookuptable[state1], self.lookuptable[state2]

    def convert_index_to_state(self, index: int) -> State:
        return self.states[index]

    def convert_indices_to_states(
        self, index1: int, index2: int
    ) -> Tuple[State, State]:
        return self.states[index1], self.states[index2]

    def __repr__(self) -> str:
        return str(self.matrix)

    def __getitem__(self, index: int):
        return self.matrix[index]
