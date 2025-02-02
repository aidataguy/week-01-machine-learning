from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt

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

# Load the housing dataset
housing_read_csv = pd.read_csv("datasets/housing/housing.csv")

def explore_dataset(df):
    """
    Performs initial exploration of the dataset by displaying basic information.
    
    Args:
        df (pandas.DataFrame): The housing dataset to analyze
        
    Returns:
        None - prints the exploration results
    """
    print(
        "🧠 let me show you some information about the dataset: \n",
        "Head: \n", df.head(), "\n",
        "Information: \n", df.info(), "\n",
        "Describe: \n", df.describe(), "\n"
    )
    # Get categories of ocean_proximity
    print("Ocean Proximity Categories:")
    print(df["ocean_proximity"].value_counts())

def plot_numerical_distributions(df):
    """
    Creates histograms for all numerical columns in the dataset.
    
    Args:
        df (pandas.DataFrame): The housing dataset to visualize
        
    Returns:
        None - displays the histogram plots
    
    Notes:
        - Number of bins is calculated using square root of N rule
        - Plots are arranged in a 2-column grid
    """
    # Calculate optimal number of bins using square root rule
    N = len(df)
    bins = int(sqrt(N))
    
    print(f"Data Points: {N}, Number of bins: {bins}")
    
    # Select numerical columns
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    
    # Calculate grid dimensions
    n_rows = (len(numerical_columns) + 1) // 2
    n_cols = 2
    
    # Create subplots
    plt.figure(figsize=(12, 4*n_rows))
    
    # Plot histograms
    for i, column in enumerate(numerical_columns, 1):
        plt.subplot(n_rows, n_cols, i)
        plt.hist(df[column], bins=bins)
        plt.title(column)
        plt.xlabel(column)
        plt.ylabel("Frequency")
    
    plt.tight_layout()
    plt.show()

# Execute the analysis
if __name__ == "__main__":
    explore_dataset(housing_read_csv)
    plot_numerical_distributions(housing_read_csv)
