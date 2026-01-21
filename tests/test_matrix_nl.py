import pytest
from starkshifts.matrix_nl import matrix_nl

def test_matrix_nl_shape():
    """ 
    Test to verify the shape of the generated matrix in matrix_nl class. 
    """
    nmin = 1
    nmax = 3
    mat = matrix_nl(nmin, nmax)

    #6 basis states {(1,0), (2,0), (2,1), (3,0), (3,1), (3,2)}
    expected_size = 6

    # Check the shape of the matrix
    assert mat.matrix.shape == (expected_size, expected_size)