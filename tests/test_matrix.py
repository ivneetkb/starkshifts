import pytest
from starkshifts.matrix import Matrix

def test_abstract_matrix_fail():
    with pytest.raises(TypeError):
        class IncompleteMatrix(Matrix):
            pass
        IncompleteMatrix()