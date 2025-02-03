#!/usr/bin/env python3

"""
NumPy Operations and Array Manipulations Module
---------------------------------------------

This module demonstrates various NumPy operations and array manipulations,
including array creation, arithmetic operations, mathematical functions,
and array transformations.

Key Features:
    - Array creation (1D to 4D)
    - Basic arithmetic operations
    - Mathematical functions (sqrt, exp, log, trigonometric)
    - Array transformations (reshape, transpose, flatten)
    - Matrix operations (dot product)

Requirements:
    - NumPy >= 1.19.0

Example:
    >>> import numpy as np
    >>> arr = np.array([1, 2, 3])
    >>> print(arr)
    [1 2 3]
"""

import numpy as np

def create_arrays():
    """
    Creates arrays of different dimensions and demonstrates basic array operations.
    
    Returns:
        tuple: Contains arrays of different dimensions (1D, 2D, 3D, 4D)
        
    Raises:
        ValueError: If array creation fails due to invalid input
        
    Example:
        >>> arr, arr2d, arr3d, arr4d = create_arrays()
        >>> print(arr.shape)  # (3,)
    """
    try:
        # Create a 1D array
        arr = np.array([1, 2, 3])
        print("1D Array:", arr)
        print("Shape:", arr.shape, "Dimension:", arr.ndim)

        # Create a 2D array
        arr2d = np.array([[1, 2, 3], [4, 5, 6]])
        print("\n2D Array:\n", arr2d)
        print("Shape:", arr2d.shape, "Dimension:", arr2d.ndim)

        # Create a 3D array
        arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
        print("\n3D Array:\n", arr3d)
        print("Shape:", arr3d.shape, "Dimension:", arr3d.ndim)

        # Create a 4D array
        arr4d = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]])
        print("\n4D Array:\n", arr4d)
        print("Shape:", arr4d.shape, "Dimension:", arr4d.ndim)

        return arr, arr2d, arr3d, arr4d
    
    except ValueError as e:
        print(f"Error creating arrays: {e}")
        raise

def perform_arithmetic_operations(arr1, arr2):
    """
    Performs basic arithmetic operations on NumPy arrays.
    
    Args:
        arr1 (np.ndarray): First input array
        arr2 (np.ndarray): Second input array
        
    Returns:
        dict: Dictionary containing results of arithmetic operations
        
    Raises:
        ValueError: If arrays have incompatible shapes
        
    Example:
        >>> a = np.array([1, 2, 3])
        >>> b = np.array([4, 5, 6])
        >>> results = perform_arithmetic_operations(a, b)
        >>> print(results['sum'])
    """
    try:
        results = {
            'sum': arr1 + arr2,
            'difference': arr1 - arr2,
            'product': arr1 * arr2,
            'division': arr1 / arr2
        }
        return results
    except ValueError as e:
        print(f"Error in arithmetic operations: {e}")
        raise
    except ZeroDivisionError:
        print("Warning: Division by zero encountered")
        raise

def mathematical_functions(arr):
    """
    Applies various mathematical functions to an array.
    
    Args:
        arr (np.ndarray): Input array
        
    Returns:
        dict: Dictionary containing results of mathematical operations
        
    Raises:
        ValueError: If input contains negative numbers for sqrt/log
        
    Example:
        >>> arr = np.array([1, 2, 3])
        >>> results = mathematical_functions(arr)
        >>> print(results['sqrt'])
    """
    try:
        return {
            'sqrt': np.sqrt(arr),
            'power': np.power(arr, 2),
            'exp': np.exp(arr),
            'log': np.log(arr),
            'sin': np.sin(arr),
            'cos': np.cos(arr),
            'tan': np.tan(arr)
        }
    except ValueError as e:
        print(f"Error in mathematical operations: {e}")
        raise

def array_transformations(arr):
    """
    Demonstrates various array transformation operations.
    
    Args:
        arr (np.ndarray): Input array
        
    Returns:
        dict: Dictionary containing transformed arrays
        
    Raises:
        ValueError: If reshape dimensions are incompatible
        
    Example:
        >>> arr = np.array([[1, 2], [3, 4]])
        >>> transforms = array_transformations(arr)
        >>> print(transforms['transpose'])
    """
    try:
        return {
            'transpose': arr.T,
            'flatten': arr.flatten(),
            'zeros': np.zeros(arr.shape),
            'ones': np.ones(arr.shape)
        }
    except ValueError as e:
        print(f"Error in array transformations: {e}")
        raise

def main():
    """
    Main function to demonstrate NumPy operations.
    
    This function runs through all the major operations and prints results.
    """
    try:
        # Create arrays
        arr, arr2d, arr3d, arr4d = create_arrays()
        
        # Demonstrate array compatibility check
        if arr.ndim == arr2d.ndim:
            print("\nArrays have same dimensions")
        else:
            print("\nArrays have different dimensions:", 
                  f"arr: {arr.ndim}D, arr2d: {arr2d.ndim}D")
        
        # Perform operations
        print("\nArray Shapes:")
        print(f"arr: {arr.shape}, arr2d: {arr2d.shape}")
        
        # Mathematical operations
        math_results = mathematical_functions(arr)
        print("\nMathematical Functions Results:")
        for op, result in math_results.items():
            print(f"{op}: {result}")
        
        # Array transformations
        trans_results = array_transformations(arr2d)
        print("\nArray Transformations:")
        for op, result in trans_results.items():
            print(f"{op}:\n{result}")
        
        # Matrix operations
        print("\nDot Product:")
        dot_product = np.dot(arr, arr2d.T)
        print(dot_product)

    except Exception as e:
        print(f"An error occurred in main: {e}")
        raise

if __name__ == "__main__":
    main()

