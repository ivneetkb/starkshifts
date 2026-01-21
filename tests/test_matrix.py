import pytest
from starkshifts.matrix import matrix


def test_abstract_matrix_fail():
    """
    Test to check for abstract method requirement.
    """
    with pytest.raises(TypeError):

        class Incompletematrix(matrix):
            pass

        m = Incompletematrix()
