import pytest
from starkshifts.matrix import Matrix

def test_abstract_matrix_fail():
    """
    Test to check for abstract method requirement.
    """
    with pytest.raises(TypeError):
        class IncompleteMatrix(Matrix):
            pass
        matrix = IncompleteMatrix()