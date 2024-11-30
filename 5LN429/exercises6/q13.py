import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys
import os

def explain_linear_regression():
    """Explain basic concepts of linear regression"""
    print("""
====== Linear Regression Explanation ======
1. Basic form of the linear regression model:
   y = β₀ + β₁x + ε
   Where:
   - y is the dependent variable (prediction)
   - x is the independent variable (predictor)
   - β₀ is the intercept (y-axis intercept)
   - β₁ is the slope (coefficient)
   - ε is the error term

2. Key statistical measures:
   - R²: Indicates the proportion of variance explained by the model (range 0-1)
   - P-value: Indicates statistical significance, usually considered significant if <0.05
   - Standard error: Reflects the accuracy of the estimate
""")

def validate_data(df):
    """
    Validate the data and print column information
    Returns True if validation passes, False otherwise
    """
    print("\nAvailable columns in the dataset:")
    print("-----------------------------------")
    for col in df.columns:
        print(f"- {col}")
    
    print("\nFirst few rows of the dataset:")
    print(df.head())
    
    print("\nDataset information:")
    print(df.info())
    
    return True

def get_regression(path, x_par, y_par):
    """
    Perform regression analysis with error handling
    """
    try:
        # Check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"Data file not found at path: {path}")
        
        print(f"\n====== Starting Regression Analysis ======")
        print(f"Data file: {path}")
        print(f"Variables to analyze:")
        print(f"Independent variable (x): {x_par}")
        print(f"Dependent variable (y): {y_par}")
        
        # Read the data
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")
        
        # Validate data
        if not validate_data(df):
            raise ValueError("Data validation failed")
        
        # Check if specified columns exist
        if x_par not in df.columns:
            raise KeyError(f"Column '{x_par}' not found in the dataset")
        if y_par not in df.columns:
            raise KeyError(f"Column '{y_par}' not found in the dataset")
        
        # Check for missing values
        if df[x_par].isnull().any() or df[y_par].isnull().any():
            print("\nWarning: Dataset contains missing values")
            print(f"Missing values in {x_par}: {df[x_par].isnull().sum()}")
            print(f"Missing values in {y_par}: {df[y_par].isnull().sum()}")
            print("Removing rows with missing values...")
            df = df.dropna(subset=[x_par, y_par])
        
        # Check if we have enough data points
        if len(df) < 3:
            raise ValueError("Not enough data points for regression analysis")
        
        print(f"\nAnalysis will proceed with {len(df)} data points")
        
        # Continue with the rest of the analysis...
        x = df[x_par].values
        y = df[y_par].values
        
        # Calculate regression parameters
        results = calculate_regression_parameters(x, y)
        
        # Make predictions
        x_new = np.linspace(min(x), max(x), 100)
        pred_intervals = calculate_prediction_intervals(x_new, x, y, results)
        
        # Check for log transformation
        log_check = check_log_transformation(x, y)
        
        return results, log_check, pred_intervals
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting suggestions:")
        print("1. Check if the file path is correct")
        print("2. Verify that the column names match exactly")
        print("3. Ensure the data file is properly formatted CSV")
        print("4. Check for missing or invalid data")
        return None, None, None

if __name__ == "__main__":
    # You can either use command line arguments or specify the path directly
    if len(sys.argv) > 3:
        path = sys.argv[1]
        x_par = sys.argv[2]
        y_par = sys.argv[3]
    else:
        # Default values for testing
        path = "/home/yaxi4987/5LN429/exercises6/EcommerceCustomers.csv"  # Replace with your actual data path
        x_par = input("Enter the name of the independent variable column: ")
        y_par = input("Enter the name of the dependent variable column: ")
    
    explain_linear_regression()
    results, log_check, predictions = get_regression(path, x_par, y_par)
    
    if results is not None:
        # Continue with the analysis...
        explain_calculations(results)
        analyze_residuals(results['residuals'], results['predicted'])