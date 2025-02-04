#!/usr/bin/env python3

"""
Matrix Operations Module
-----------------------

This module provides a comprehensive set of matrix operations using NumPy arrays.
It includes both basic arithmetic operations and advanced matrix manipulations.

The Matrix_Operations class encapsulates common matrix operations that can be performed
on two matrices, including element-wise operations, matrix products, and transformations.

Example:
    >>> matrix1 = np.array([[1, 2], [3, 4]])
    >>> matrix2 = np.array([[5, 6], [7, 8]]) 
    >>> ops = Matrix_Operations(matrix1, matrix2)
    >>> ops.matrix_dot_product()
    Matrix dot product:
    [[19 22]
     [43 50]]

Requirements:
    - NumPy >= 1.19.0
"""

import numpy as np

# Example matrices for demonstration
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


class Matrix_Operations:
    """
    A class that implements various matrix operations using NumPy.

    This class provides methods for performing common matrix operations including
    basic arithmetic, element-wise operations, and matrix-specific transformations.

    Attributes:
        matrix (np.ndarray): First input matrix
        matrix_2 (np.ndarray): Second input matrix
    """

    def __init__(self, matrix, matrix_2):
        """
        Initialize with two matrices to perform operations on.

        Args:
            matrix (np.ndarray): First input matrix
            matrix_2 (np.ndarray): Second input matrix
        """
        self.matrix = matrix
        self.matrix_2 = matrix_2

    def matrix_transpose(self):
        """Compute and display the transpose of the first matrix."""
        result = self.matrix.T
        print("Matrix transpose:\n", result)
        return result

    def matrix_addition(self):
        """Perform matrix addition of the two matrices."""
        result = self.matrix + self.matrix_2
        print("Matrix addition:\n", result)
        return result
    
    def matrix_subtraction(self):
        """Perform matrix subtraction of the two matrices."""
        result = self.matrix - self.matrix_2
        print("Matrix subtraction:\n", result)
        return result
    
    def matrix_multiplication(self):
        """Perform element-wise multiplication of the two matrices."""
        result = self.matrix * self.matrix_2
        print("Matrix multiplication:\n", result)
        return result
    
    def matrix_division(self):
        """Perform element-wise division of the two matrices."""
        result = self.matrix / self.matrix_2
        print("Matrix division:\n", result)
        return result
    
    def matrix_power(self):
        """Raise elements of first matrix to powers specified by second matrix."""
        result = self.matrix ** self.matrix_2
        print("Matrix power:\n", result)
        return result
    
    def matrix_modulus(self):
        """Compute element-wise modulus of the two matrices."""
        result = self.matrix % self.matrix_2
        print("Matrix modulus:\n", result)
        return result
    
    def matrix_dot_product(self):
        """Compute the matrix dot product of the two matrices."""
        result = np.dot(self.matrix, self.matrix_2)
        print("Matrix dot product:\n", result)
        return result
    
    def matrix_cross_product(self):
        """Compute the cross product of the two matrices."""
        result = np.cross(self.matrix, self.matrix_2)
        print("Matrix cross product:\n", result)
        return result
    
    def matrix_element_wise_addition(self):
        """Perform element-wise addition of the two matrices."""
        result = self.matrix + self.matrix_2
        print("Matrix element-wise addition:\n", result)
        return result
    
    def matrix_element_wise_subtraction(self):
        """Perform element-wise subtraction of the two matrices."""
        result = self.matrix - self.matrix_2
        print("Matrix element-wise subtraction:\n", result)
        return result
    
    def matrix_element_wise_multiplication(self):
        """Perform element-wise multiplication of the two matrices."""
        result = self.matrix * self.matrix_2
        print("Matrix element-wise multiplication:\n", result)
        return result
    
    def matrix_element_wise_division(self):
        """Perform element-wise division of the two matrices."""
        result = self.matrix / self.matrix_2
        print("Matrix element-wise division:\n", result)
        return result
    
    def matrix_element_wise_power(self):
        """Perform element-wise power operation on the two matrices."""
        result = self.matrix ** self.matrix_2
        print("Matrix element-wise power:\n", result)
        return result
    
    def matrix_element_wise_modulus(self):
        """Perform element-wise modulus operation on the two matrices."""
        result = self.matrix % self.matrix_2
        print("Matrix element-wise modulus:\n", result)
        return result

    def identity_matrix(self):
        """
        Create and return an identity matrix of the same size as the first matrix.
        
        Returns:
            np.ndarray: An identity matrix with the same dimensions as self.matrix
        """
        Identity_Matrix = np.identity(self.matrix.shape[0])
        print("Identity Matrix:\n", Identity_Matrix)
        return Identity_Matrix

def main():
    """
    Main function to demonstrate all matrix operations.
    Creates two sample matrices and performs all available operations.
    """
    matrix_ops = Matrix_Operations(matrix, matrix_2)
    matrix_ops.matrix_transpose()
    matrix_ops.matrix_addition()
    matrix_ops.matrix_subtraction()
    matrix_ops.matrix_multiplication()
    matrix_ops.matrix_division()
    matrix_ops.matrix_power()
    matrix_ops.matrix_modulus()
    matrix_ops.matrix_dot_product()
    matrix_ops.matrix_cross_product()
    matrix_ops.matrix_element_wise_addition()
    matrix_ops.matrix_element_wise_subtraction()
    matrix_ops.matrix_element_wise_multiplication()
    matrix_ops.matrix_element_wise_division()
    matrix_ops.matrix_element_wise_power()
    matrix_ops.matrix_element_wise_modulus()       
    matrix_ops.identity_matrix()

if __name__ == "__main__":
    main()