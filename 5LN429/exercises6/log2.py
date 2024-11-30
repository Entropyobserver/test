import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

def explain_linear_regression():
    """Explain basic concepts of linear regression"""
    print("""
====== Explanation of Basic Concepts of Linear Regression ======
1. Basic form of the linear regression model:
   y = β₀ + β₁x + ε
   where:
   - y is the dependent variable (predicted value)
   - x is the independent variable (predictor variable)
   - β₀ is the intercept (y-axis intercept)
   - β₁ is the slope (coefficient)
   - ε is the error term

2. Key statistical indicators:
   - R²: Represents the proportion of variance explained by the model (range from 0 to 1)
   - P-value: Indicates statistical significance, usually considered significant if less than 0.05
   - Standard error: Reflects the accuracy of the estimated values
""")

def check_log_transform(y):
    """
    Check if log transformation is needed based on skewness and other criteria
    """
    skewness = stats.skew(y)
    print("\n====== Log Transformation Requirement Check ======")
    print(f"• Skewness of residuals: {skewness:.4f}")
    if skewness > 1 or skewness < -1:
        print("  - Skewness greater than 1 or less than -1, log transformation is recommended")
    else:
        print("  - Skewness is within a reasonable range, log transformation is not needed")

def calculate_regression_parameters(x, y):
    """
    Calculate regression parameters with detailed steps
    """
    n = len(x)
    # Step 1: Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Step 2: Calculate sums of squares
    SS_xx = np.sum((x - x_mean)**2)
    SS_yy = np.sum((y - y_mean)**2)
    SS_xy = np.sum((x - x_mean)*(y - y_mean))
    
    # Step 3: Calculate slope (β₁)
    slope = SS_xy / SS_xx
    
    # Step 4: Calculate intercept (β₀)
    intercept = y_mean - slope * x_mean
    
    # Step 5: Calculate R-squared
    r_squared = (SS_xy)**2 / (SS_xx * SS_yy)
    
    # Step 6: Calculate residuals
    y_pred = slope * x + intercept
    residuals = y - y_pred
    
    # Step 7: Calculate standard error
    standard_error = np.sqrt(np.sum(residuals**2) / (n-2)) / np.sqrt(SS_xx)
    
    # Step 8: Calculate t-statistic and p-value
    t_stat = slope / standard_error
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), n-2))
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_squared,
        'standard_error': standard_error,
        'p_value': p_value,
        'residuals': residuals,
        'predicted': y_pred,
        'calculations': {
            'n': n,
            'x_mean': x_mean,
            'y_mean': y_mean,
            'SS_xx': SS_xx,
            'SS_yy': SS_yy,
            'SS_xy': SS_xy,
            't_stat': t_stat
        }
    }

def get_regression(path, x_par, y_par):
    print(f"\n====== Starting Regression Analysis ======")
    print(f"Analyzing variables:")
    print(f"Independent variable (x): {x_par}")
    print(f"Dependent variable (y): {y_par}")
    
    # Read data
    df = pd.read_csv(path)
    print(f"\nPreview of raw data:")
    print(df[[x_par, y_par]].head())
    
    # Descriptive statistics
    print(f"\nDescriptive statistics:")
    print(df[[x_par, y_par]].describe())
    
    # Plot regression graph
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df, x=x_par, y=y_par,
        scatter_kws={"s": 10},
        line_kws={"color": "blue", "linewidth": 0.8}
    )
    plt.xlabel(x_par)
    plt.ylabel(y_par)
    plt.title("Linear Regression Analysis")
    plt.savefig("regression_plot.png")
    print(f"\nRegression plot saved as 'regression_plot.png'")
    
    # Calculate regression parameters
    x = df[x_par].values
    y = df[y_par].values
    results = calculate_regression_parameters(x, y)
    
    # Check the need for log transformation
    check_log_transform(y)
    
    # Print detailed analysis results
    print("\n====== Regression Results ======")
    print(f"• Slope: {results['slope']:.4f}")
    print(f"• Intercept: {results['intercept']:.4f}")
    print(f"• R² value: {results['r_squared']:.4f}")
    print(f"• Standard error: {results['standard_error']:.4f}")
    print(f"• P-value: {results['p_value']:.4f}")

if __name__ == "__main__":
    path = sys.argv[1]
    x_par = sys.argv[2]
    y_par = sys.argv[3]
    explain_linear_regression()
    get_regression(path, x_par, y_par)
##python log2.py '/home/yaxi4987/exercises6/EcommerceCustomers.csv' 'Length of Membership' 'Yearly Amount Spent'