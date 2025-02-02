from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Optional

"""
Housing Data Analysis Script
---------------------------
This script performs exploratory data analysis on a housing dataset.
It loads housing data from a CSV file and generates various statistical
summaries and visualizations.

The script includes:
1. Basic data exploration (head, info, describe)
2. Analysis of ocean proximity categories
3. Histogram visualization of numerical features
"""

class DataLoader:
    """
    Responsible for loading and providing access to the housing dataset.
    Following Single Responsibility Principle - handles only data loading.
    """
    def __init__(self, file_path: str):
        """
        Initialize DataLoader with the path to the dataset.
        
        Args:
            file_path (str): Path to the CSV file
        """
        self.file_path = file_path
        self._data: Optional[pd.DataFrame] = None
    
    def load_data(self) -> pd.DataFrame:
        """
        Loads the dataset from the CSV file.
        
        Returns:
            pd.DataFrame: The loaded housing dataset
        """
        if self._data is None:
            self._data = pd.read_csv(self.file_path)
        return self._data

class DataExplorer:
    """
    Responsible for performing exploratory data analysis.
    Following Single Responsibility Principle - handles only data exploration.
    """
    @staticmethod
    def explore_dataset(df: pd.DataFrame) -> None:
        """
        Performs initial exploration of the dataset by displaying basic information.
        
        Args:
            df (pd.DataFrame): The housing dataset to analyze
        """
        print(
            "🧠 let me show you some information about the dataset: \n",
            "Head: \n", df.head(), "\n",
            "Information: \n", df.info(), "\n",
            "Describe: \n", df.describe(), "\n"
        )
        print("Ocean Proximity Categories:")
        print(df["ocean_proximity"].value_counts())

class DataVisualizer:
    """
    Responsible for creating visualizations of the data.
    Following Single Responsibility Principle - handles only data visualization.
    """
    def __init__(self):
        """Initialize DataVisualizer with default plot settings"""
        self.figure_size = (12, 4)
        self.n_cols = 2
    
    def _calculate_bins(self, data_length: int) -> int:
        """
        Calculate optimal number of bins using square root rule.
        
        Args:
            data_length (int): Length of the dataset
            
        Returns:
            int: Optimal number of bins
        """
        return int(sqrt(data_length))
    
    def _get_numerical_columns(self, df: pd.DataFrame) -> List[str]:
        """
        Get list of numerical columns from DataFrame.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            
        Returns:
            List[str]: List of numerical column names
        """
        return list(df.select_dtypes(include=['int64', 'float64']).columns)
    
    def plot_numerical_distributions(self, df: pd.DataFrame) -> None:
        """
        Creates histograms for all numerical columns in the dataset.
        
        Args:
            df (pd.DataFrame): The housing dataset to visualize
        
        Notes:
            - Number of bins is calculated using square root of N rule
            - Plots are arranged in a 2-column grid
        """
        N = len(df)
        bins = self._calculate_bins(N)
        numerical_columns = self._get_numerical_columns(df)
        
        print(f"Data Points: {N}, Number of bins: {bins}")
        
        # Calculate grid dimensions
        n_rows = (len(numerical_columns) + 1) // 2
        
        # Create subplots
        plt.figure(figsize=(self.figure_size[0], self.figure_size[1] * n_rows))
        
        # Plot histograms
        for i, column in enumerate(numerical_columns, 1):
            plt.subplot(n_rows, self.n_cols, i)
            plt.hist(df[column], bins=bins)
            plt.title(column)
            plt.xlabel(column)
            plt.ylabel("Frequency")
        
        plt.tight_layout()
        plt.show()

class HousingAnalysis:
    """
    Main class that orchestrates the housing data analysis.
    Following Interface Segregation Principle - uses specific interfaces for different tasks.
    """
    def __init__(self, data_path: str):
        """
        Initialize the analysis with required components.
        
        Args:
            data_path (str): Path to the housing dataset
        """
        self.loader = DataLoader(data_path)
        self.explorer = DataExplorer()
        self.visualizer = DataVisualizer()
        self.data = None
    
    def run_analysis(self):
        """Execute the complete analysis workflow"""
        self.data = self.loader.load_data()
        self.explorer.explore_dataset(self.data)
        self.visualizer.plot_numerical_distributions(self.data)

def main():
    """Main entry point of the script"""
    analysis = HousingAnalysis("datasets/housing/housing.csv")
    analysis.run_analysis()

if __name__ == "__main__":
    main()
