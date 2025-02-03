#! /usr/bin/env python3

import numpy as np

def vectors():
    # Create example vectors using numpy
    import numpy as np
    
    # Create a 1D vector
    vector_1d = np.array([1, 2])
    print("1D Vector:", vector_1d)
    print("Shape:", vector_1d.shape)
    
    # Create a 2D vector/matrix 
    vector_2d = np.array([[1, 2], [3, 4]])
    print("\n2D Vector:\n", vector_2d)
    print("Shape:", vector_2d.shape)
    
    # Common vector operations
    print("\nVector Operations:")
    print("Dot product:", np.dot(vector_1d, vector_1d))
    print("Vector norm:", np.linalg.norm(vector_1d))
    print("Unit vector:", vector_1d / np.linalg.norm(vector_1d))

    vector_2d_transpose = vector_2d.T
    print("Transpose of 2D vector:\n", vector_2d_transpose)

    # Dot product of 1D and 2D vectors
    reshaped_vector_1d = vector_1d.reshape(1, -1)
    vector_dot_product = np.dot(vector_1d, vector_2d)
    print("Dot product of 1D and 2D vectors:\n", vector_dot_product)

def row_vector():
    vector_1d = np.array([1, 2, 3])
    print("Row vector:", vector_1d)
    print("Shape:", vector_1d.shape)

def column_vector():
    vector_1d = np.array([[1], [2], [3]])
    print("Column vector:", vector_1d)
    print("Shape:", vector_1d.shape)

# element wise operations
def element_wise_addition():
    vector_1d = np.array([1, 2, 3])
    vector_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element wise operations:", vector_1d + vector_2d)

# element wise multiplication
def element_wise_multiplication():
    vector_1d = np.array([1, 2, 3])
    vector_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element wise multiplication:: ", vector_1d * vector_2d)

def element_wise_division():
    vector_1d = np.array([1, 2, 3])
    vector_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element wise division:: ", vector_1d / vector_2d)


def element_wise_power():
    vector_1d = np.array([1, 2, 3])
    vector_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element wise power:: ", vector_1d ** vector_2d)

def element_wise_modulus():
    vector_1d = np.array([1, 2, 3])
    vector_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element wise modulus:: ", vector_1d % vector_2d)

def element_wise_subtraction():
    vector_1d = np.array([1, 2, 3])
    vector_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element wise subtraction:: ", vector_1d - vector_2d)
#dot product
def vector_dot_product():
    vector1d = np.array([1, 2, 3])
    vector2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Dot product::", np.dot(vector1d, vector2d))

def vector_cross_product():
    vector1d = np.array([1, 2, 3])
    vector2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Cross product::", np.cross(vector1d, vector2d))


def main():
    vectors()

if __name__ == "__main__":
    main()
