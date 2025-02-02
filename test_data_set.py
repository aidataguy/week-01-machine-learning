import numpy as np
import pandas as pd
from typing import Tuple

"""
Data Split Testing Module
------------------------
This module provides functionality for splitting datasets into training and testing sets
for machine learning applications. It includes methods for random shuffling and
maintaining data proportions.

The module is designed to work with pandas DataFrames and includes validation
to ensure proper data splitting.

Example:
    >>> data = pd.read_csv("datasets/housing/housing.csv")
    >>> TestDataSplit.test_split_shuffle_data(data, 0.2)
    "✅ Test Data Split completed successfully"
"""

class TestDataSplit:
    """
    A class for testing data splitting functionality in machine learning workflows.
    
    This class provides methods to split datasets into training and testing sets
    while maintaining data integrity and random distribution.
    
    Attributes:
        None
        
    Methods:
        test_split_shuffle_data: Splits and shuffles data into training and testing sets
    """
    
    @staticmethod
    def test_split_shuffle_data(data: pd.DataFrame, 
                               test_ratio: float) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Splits a dataset into training and testing sets using random shuffling.
        
        Args:
            data (pd.DataFrame): The input dataset to be split
            test_ratio (float): The proportion of data to be used for testing
                               Must be between 0 and 1
                               
        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing:
                - train_set: The training dataset
                - test_set: The testing dataset
                
        Raises:
            ValueError: If test_ratio is not between 0 and 1
            TypeError: If data is not a pandas DataFrame
            
        Example:
            >>> housing_data = pd.read_csv("housing.csv")
            >>> train_data, test_data = test_split_shuffle_data(housing_data, 0.2)
            >>> print(f"Training set size: {len(train_data)}")
            >>> print(f"Testing set size: {len(test_data)}")
        
        Notes:
            - The function uses numpy's random permutation for shuffling
            - The split maintains the original data structure and column names
            - The function prints the sizes of resulting sets for verification
        """
        # Input validation
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame")
        if not 0 < test_ratio < 1:
            raise ValueError("test_ratio must be between 0 and 1")
        
        # Generate random indices for shuffling
        shuffled_indices = np.random.permutation(len(data))
        
        # Calculate split point
        test_set_size = int(len(data) * test_ratio)
        
        # Split indices
        test_indices = shuffled_indices[:test_set_size]
        train_indices = shuffled_indices[test_set_size:]
        
        # Create train and test sets
        train_set = data.iloc[train_indices]
        test_set = data.iloc[test_indices]
        
        # Print set sizes for verification
        print(f"Training set size: {len(train_set)}")
        print(f"Testing set size: {len(test_set)}")
        
        return train_set, test_set


# Example usage (commented out)
# data = pd.read_csv("datasets/housing/housing.csv")
# TestDataSplit.test_split_shuffle_data(data, 0.2)