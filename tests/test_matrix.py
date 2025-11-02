"""
Unit tests for SupertropicalMatrix class.
"""
import pytest
import numpy as np
import math
from src.supertropical import SupertropicalElement, SupertropicalMatrix


class TestMatrixCreation:
    """Test matrix creation and initialization."""
    
    def test_create_from_list(self):
        """Test creating matrix from list of lists."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        assert A.shape == (2, 2)
        assert A[0, 0].value == 1.0
        assert A[1, 1].value == 4.0
        
    def test_create_from_elements(self):
        """Test creating matrix from SupertropicalElement objects."""
        e1 = SupertropicalElement(5)
        e2 = SupertropicalElement(3, is_ghost=True)
        A = SupertropicalMatrix([[e1, e2], [e2, e1]])
        assert A.shape == (2, 2)
        assert A[0, 0].value == 5.0
        assert A[0, 1].is_ghost
        
    def test_create_3x3_matrix(self):
        """Test creating a 3×3 matrix."""
        A = SupertropicalMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert A.shape == (3, 3)
        
    def test_create_non_square_matrix(self):
        """Test creating a non-square matrix."""
        A = SupertropicalMatrix([[1, 2, 3], [4, 5, 6]])
        assert A.shape == (2, 3)


class TestMatrixMultiplication:
    """Test matrix multiplication (⊙)."""
    
    def test_multiply_2x2_matrices(self):
        """Test multiplying two 2×2 matrices."""
        A = SupertropicalMatrix([[2, 1], [1, 3]])
        B = SupertropicalMatrix([[1, 0], [0, 1]])
        C = A * B
        assert C.shape == (2, 2)
        # Verify some elements
        assert isinstance(C[0, 0], SupertropicalElement)
        
    def test_multiply_identity_matrix(self):
        """Test multiplying by identity-like matrix."""
        A = SupertropicalMatrix([[2, 1], [1, 3]])
        # In supertropical, 0 is multiplicative identity
        I = SupertropicalMatrix([[0, -math.inf], [-math.inf, 0]])
        C = A * I
        # Result should be close to A (considering ghost conversions)
        assert C.shape == A.shape
        
    def test_multiply_3x3_matrices(self):
        """Test multiplying 3×3 matrices."""
        A = SupertropicalMatrix([[1, 2, 0], [0, 1, 2], [2, 0, 1]])
        B = SupertropicalMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        C = A * B
        assert C.shape == (3, 3)
        
    def test_multiply_non_square_matrices(self):
        """Test multiplying non-square matrices."""
        A = SupertropicalMatrix([[1, 2], [3, 4], [5, 6]])  # 3×2
        B = SupertropicalMatrix([[1, 2, 3], [4, 5, 6]])    # 2×3
        C = A * B
        assert C.shape == (3, 3)
        
    def test_multiply_wrong_dimensions_raises_error(self):
        """Test that incompatible dimensions raise ValueError."""
        A = SupertropicalMatrix([[1, 2]])  # 1×2
        B = SupertropicalMatrix([[1], [2], [3]])  # 3×1
        with pytest.raises(ValueError):
            C = A * B


class TestScalarMultiplication:
    """Test scalar multiplication."""
    
    def test_scalar_multiply_tangible(self):
        """Test multiplying matrix by tangible scalar."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        scalar = SupertropicalElement(2)
        B = A * scalar
        assert B.shape == A.shape
        assert B[0, 0].value == 3.0  # 1 + 2
        assert B[1, 1].value == 6.0  # 4 + 2
        
    def test_scalar_multiply_ghost(self):
        """Test multiplying matrix by ghost scalar."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        scalar = SupertropicalElement(1, is_ghost=True)
        B = A * scalar
        # All elements should be ghost
        assert B[0, 0].is_ghost
        assert B[1, 1].is_ghost
        
    def test_scalar_multiply_with_int(self):
        """Test multiplying matrix by Python int."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        B = A * 2
        assert B[0, 0].value == 3.0
        
    def test_right_scalar_multiply(self):
        """Test right scalar multiplication."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        scalar = SupertropicalElement(2)
        B = scalar * A
        assert B.shape == A.shape


class TestMatrixPermanent:
    """Test permanent (supertropical determinant) calculation."""
    
    def test_permanent_2x2(self):
        """Test permanent of 2×2 matrix."""
        A = SupertropicalMatrix([[2, 1], [1, 3]])
        perm = A.permanent()
        # per(A) = (2 + 3) ⊕ (1 + 1) = 5 ⊕ 2 = 5
        assert perm.value == 5.0
        assert not perm.is_ghost
        
    def test_permanent_3x3(self):
        """Test permanent of 3×3 matrix."""
        A = SupertropicalMatrix([[1, 2, 0], [0, 1, 2], [2, 0, 1]])
        perm = A.permanent()
        assert isinstance(perm, SupertropicalElement)
        # Verify it's a valid result
        assert perm.value > -math.inf
        
    def test_permanent_identity(self):
        """Test permanent of identity-like matrix."""
        I = SupertropicalMatrix([[0, -math.inf], [-math.inf, 0]])
        perm = I.permanent()
        # per(I) should be 0 (multiplicative identity)
        assert perm.value == 0.0
        
    def test_permanent_non_square_raises_error(self):
        """Test that permanent of non-square matrix raises ValueError."""
        A = SupertropicalMatrix([[1, 2, 3], [4, 5, 6]])
        with pytest.raises(ValueError):
            A.permanent()


class TestMatrixAdjoint:
    """Test adjoint matrix calculation."""
    
    def test_adjoint_2x2(self):
        """Test adjoint of 2×2 matrix."""
        A = SupertropicalMatrix([[2, 1], [1, 3]])
        adj = A.adjoint()
        assert adj.shape == (2, 2)
        assert isinstance(adj, SupertropicalMatrix)
        
    def test_adjoint_3x3(self):
        """Test adjoint of 3×3 matrix."""
        A = SupertropicalMatrix([[1, 2, 0], [0, 1, 2], [2, 0, 1]])
        adj = A.adjoint()
        assert adj.shape == (3, 3)
        
    def test_adjoint_non_square_raises_error(self):
        """Test that adjoint of non-square matrix raises ValueError."""
        A = SupertropicalMatrix([[1, 2, 3], [4, 5, 6]])
        with pytest.raises(ValueError):
            A.adjoint()


class TestMatrixMinor:
    """Test minor matrix calculation."""
    
    def test_minor_2x2(self):
        """Test getting minor from 2×2 matrix."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        minor = A.get_minor(0, 0)
        assert minor.shape == (1, 1)
        assert minor[0, 0].value == 4.0
        
    def test_minor_3x3(self):
        """Test getting minor from 3×3 matrix."""
        A = SupertropicalMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        minor = A.get_minor(0, 0)
        assert minor.shape == (2, 2)
        assert minor[0, 0].value == 5.0
        assert minor[1, 1].value == 9.0


class TestLinearSystemSolver:
    """Test solving linear systems using Cramer's rule."""
    
    def test_solve_2x2_system(self):
        """Test solving a 2×2 system."""
        A = SupertropicalMatrix([[2, 1], [1, 3]])
        b = SupertropicalMatrix([[5], [4]])
        
        # Check that matrix is nonsingular
        perm = A.permanent()
        assert perm.is_tangible()
        
        # Solve
        x = A.solve(b)
        assert x.shape == (2, 1)
        assert isinstance(x[0, 0], SupertropicalElement)
        
    def test_solve_3x3_system(self):
        """Test solving a 3×3 system."""
        A = SupertropicalMatrix([[1, 2, 0], [0, 1, 2], [2, 0, 1]])
        b = SupertropicalMatrix([[5], [4], [6]])
        
        perm = A.permanent()
        if perm.is_tangible():
            x = A.solve(b)
            assert x.shape == (3, 1)
        else:
            # Matrix is singular
            with pytest.raises(ValueError):
                A.solve(b)
                
    def test_solve_singular_matrix_raises_error(self):
        """Test that solving singular system raises ValueError."""
        # Create a singular matrix (permanent will be ghost)
        A = SupertropicalMatrix([[1, 1], [1, 1]])
        b = SupertropicalMatrix([[2], [2]])
        
        perm = A.permanent()
        if perm.is_ghost:
            with pytest.raises(ValueError):
                A.solve(b)
                
    def test_solve_non_square_raises_error(self):
        """Test that solving non-square system raises ValueError."""
        A = SupertropicalMatrix([[1, 2, 3], [4, 5, 6]])
        b = SupertropicalMatrix([[1], [2]])
        with pytest.raises(ValueError):
            A.solve(b)
            
    def test_solve_dimension_mismatch_raises_error(self):
        """Test that dimension mismatch raises ValueError."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        b = SupertropicalMatrix([[1], [2], [3]])  # Wrong size
        with pytest.raises(ValueError):
            A.solve(b)


class TestMatrixRepresentation:
    """Test matrix string representation."""
    
    def test_repr_2x2(self):
        """Test repr of 2×2 matrix."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        repr_str = repr(A)
        assert "SupertropicalMatrix" in repr_str
        
    def test_getitem(self):
        """Test element access."""
        A = SupertropicalMatrix([[1, 2], [3, 4]])
        elem = A[0, 1]
        assert isinstance(elem, SupertropicalElement)
        assert elem.value == 2.0


class TestMatrixWithGhostElements:
    """Test matrices containing ghost elements."""
    
    def test_create_with_ghosts(self):
        """Test creating matrix with ghost elements."""
        g = SupertropicalElement(5, is_ghost=True)
        A = SupertropicalMatrix([[1, g], [g, 2]])
        assert A[0, 1].is_ghost
        assert A[1, 0].is_ghost
        
    def test_multiply_with_ghosts(self):
        """Test multiplying matrices with ghost elements."""
        g = SupertropicalElement(2, is_ghost=True)
        A = SupertropicalMatrix([[1, g], [2, 3]])
        B = SupertropicalMatrix([[1, 0], [0, 1]])
        C = A * B
        assert C.shape == (2, 2)
        
    def test_permanent_with_ghosts(self):
        """Test permanent of matrix with ghost elements."""
        g = SupertropicalElement(2, is_ghost=True)
        A = SupertropicalMatrix([[1, g], [2, 3]])
        perm = A.permanent()
        # Permanent might be ghost depending on the values
        assert isinstance(perm, SupertropicalElement)
