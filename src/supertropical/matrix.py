# src/supertropical/matrix.py
import numpy as np
import itertools
from.element import SupertropicalElement

class SupertropicalMatrix:
    """
    Represents a matrix over the supertropical algebra.
    """

    def __init__(self, data):
        """
        Initializes from a list of lists or a numpy array.
        """
        if not isinstance(data, np.ndarray):
            # Convert list of (float, int, or SupertropicalElement)
            # to a numpy array of SupertropicalElement objects
            if isinstance(data, list):
                # Get shape from nested list
                rows = len(data)
                cols = len(data[0]) if rows > 0 else 0
                object_array = np.empty((rows, cols), dtype=object)
                
                for i in range(rows):
                    for j in range(cols):
                        val = data[i][j]
                        if not isinstance(val, SupertropicalElement):
                            val = SupertropicalElement(val)
                        object_array[i, j] = val
                self.data = object_array
            else:
                # If it's already a numpy array
                self.data = np.array(data, dtype=object)
        else:
            self.data = data
            
        self.shape = self.data.shape

    def __repr__(self):
        return f"SupertropicalMatrix(\n{self.data}\n)"

    def __getitem__(self, key):
        return self.data[key]

    def __mul__(self, other):
        """
        Matrix multiplication or scalar multiplication.
        
        - If other is SupertropicalMatrix: performs supertropical matrix multiplication
          C_ij = ⊕_k (A_ik ⊙ B_kj)
        - If other is scalar (SupertropicalElement, int, float): multiplies each element
        """
        if isinstance(other, SupertropicalMatrix):
            # Matrix multiplication
            if self.shape[1] != other.shape[0]:
                raise ValueError(f"Matrix dimensions do not match: {self.shape} * {other.shape}.")

            new_shape = (self.shape[0], other.shape[1])
            result_matrix = np.empty(new_shape, dtype=object)

            for i in range(new_shape[0]):
                for j in range(new_shape[1]):
                    # Initialize C_ij with the zero element (-inf)
                    sum_val = SupertropicalElement(-np.inf)
                    
                    for k in range(self.shape[1]):
                        # Calculate A_ik ⊙ B_kj (using element multiplication)
                        prod = self[i, k] * other[k, j]
                        # Perform C_ij = C_ij ⊕ (A_ik ⊙ B_kj) (using element addition)
                        sum_val = sum_val + prod
                    
                    result_matrix[i, j] = sum_val

            return SupertropicalMatrix(result_matrix)
            
        elif isinstance(other, SupertropicalElement):
            # Scalar multiplication
            result = np.empty(self.shape, dtype=object)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i, j] = self[i, j] * other
            return SupertropicalMatrix(result)
            
        elif isinstance(other, (int, float)):
            return self * SupertropicalElement(other)
            
        else:
            raise TypeError("Can only multiply by SupertropicalMatrix, SupertropicalElement or scalar.")

    def __rmul__(self, other):
        if isinstance(other, (int, float, SupertropicalElement)):
            return self.__mul__(other)
        else:
            raise TypeError("Left multiplication only supported for scalars.")
    
    # --- Linear Algebra Methods ---

    def get_minor(self, i: int, j: int):
        """
        Returns the minor matrix by removing row i and column j.
        
        Args:
            i (int): Row index to remove.
            j (int): Column index to remove.

        Returns:
            SupertropicalMatrix: The (n-1)x(n-1) minor matrix.
        """
        data_without_row = np.delete(self.data, i, axis=0)
        data_without_col = np.delete(data_without_row, j, axis=1)
        return SupertropicalMatrix(data_without_col)

    def permanent(self):
        """
        Calculates the supertropical permanent of the matrix.
        
        The permanent is defined as:
        per(A) = $\oplus_{\pi \in S_n} \odot_{i=1}^n a_{i, \pi(i)}$
        
        This is used as the supertropical equivalent of the determinant. [5, 19]

        Returns:
            SupertropicalElement: The permanent of the matrix.
        """
        if self.shape[0] != self.shape[1]:
            raise ValueError("Permanent is only defined for square matrices.")
            
        n = self.shape[0]
        if n == 0:
            return SupertropicalElement(0.0) # Multiplicative identity

        # Use itertools.permutations to sum over all permutations
        perms = itertools.permutations(range(n))
        
        # Start with the additive identity (-inf)
        total_sum = SupertropicalElement(-np.inf)

        for perm in perms:
            # Start with the multiplicative identity (0.0)
            term_prod = SupertropicalElement(0.0)
            for i in range(n):
                term_prod = term_prod * self[i, perm[i]]
            
            # Add the product of this permutation to the total sum
            total_sum = total_sum + term_prod
            
        return total_sum

    def adjoint(self):
        """
        Calculates the supertropical adjoint matrix.
        
        The adjoint is the transpose of the cofactor matrix.
        The (i, j)-th entry of the adjoint is the (j, i)-th cofactor.
        The (j, i)-th cofactor is the permanent of the minor M_ji. [5, 11]

        Returns:
            SupertropicalMatrix: The adjoint matrix of self.
        """
        if self.shape[0] != self.shape[1]:
            raise ValueError("Adjoint is only defined for square matrices.")

        n = self.shape[0]
        adj_matrix_data = np.empty(self.shape, dtype=object)
        
        for i in range(n):
            for j in range(n):
                # Adjoint(i, j) = Cofactor(j, i) = permanent(Minor(j, i))
                minor = self.get_minor(j, i) 
                adj_matrix_data[i, j] = minor.permanent()
                
        return SupertropicalMatrix(adj_matrix_data)

    def solve(self, b: 'SupertropicalMatrix'):
        """
        Solves the supertropical linear system A @ x = b using
        a version of Cramer's Rule. 

        The solution is calculated using the adjoint matrix:
        x = adj(A) @ b @ (per(A))^{-1}
        
        This provides the unique maximal tangible solution to the
        system $Ax \mid_{gs}= b$. 

        Args:
            b (SupertropicalMatrix): The (n, 1) vector on the 
                                     right-hand side.

        Returns:
            SupertropicalMatrix: The (n, 1) solution vector x.
            
        Raises:
            ValueError: If the matrix is singular (permanent is ghost)
                        or dimensions are incorrect.
        """
        if self.shape[0] != self.shape[1]:
            raise ValueError("System must be square (n x n) to solve.")
        # b must be a column vector with same number of rows as A, allow (n,1) or (n,)
        if b.shape != (self.shape[0], 1) and b.shape != (self.shape[0],):
            raise ValueError(f"Dimension mismatch. A is {self.shape} but b is {b.shape}.")

        # 1. Calculate the permanent (supertropical determinant)
        per_A = self.permanent()
        
        # A matrix is nonsingular if its permanent is tangible [7, 19]
        if per_A.is_ghost:
            raise ValueError("Matrix is singular (permanent is ghost). Cannot solve.")

        # 2. Calculate the inverse of the permanent
        # (1/a) in supertropical algebra is -a (classical)
        per_A_inv = SupertropicalElement(-per_A.value, is_ghost=per_A.is_ghost)

        # 3. Calculate the tangible adjoint matrix 
        adj_A = self.adjoint()
        
        # 4. Calculate solution x = adj(A) @ b @ per(A)^-1
        # Reshape b if needed to ensure column vector
        if len(b.shape) == 1:
            b_reshaped = SupertropicalMatrix(b.data.reshape(-1, 1))
        else:
            b_reshaped = b
            
        x = (adj_A @ b_reshaped) * per_A_inv
        
        return x