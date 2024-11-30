import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

def explain_linear_regression():
    """Explain basic concepts of linear regression"""
    print("""
\n====== Linear Regression Explanation ======
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

def get_regression(path, x_par, y_par):
    print(f"\n====== Starting Regression Analysis ======")
    print(f"Variables analyzed:")
    print(f"Independent variable (x): {x_par}")
    print(f"Dependent variable (y): {y_par}")
    
    # Read the data
    df = pd.read_csv(path)
    print(f"\nPreview of original data:")
    print(df[[x_par, y_par]].head())
    
    # Descriptive statistics
    print(f"\nDescriptive statistics:")
    print(df[[x_par, y_par]].describe())
    
    # Plot regression
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
    
    # Calculate regression statistics
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])
    
    # Print detailed results
    print(f"\n====== Regression Results ======")
    print(f"""
1. Regression equation:
   y = {intercept:.4f} + {slope:.4f}x
   
2. Coefficient explanation:
   - Intercept (β₀) = {intercept:.4f}
     Meaning: Predicted value of y when x is 0
   
   - Slope (β₁) = {slope:.4f}
     Meaning: For every 1 unit increase in x, y is expected to increase by {slope:.4f} units
   
3. Model evaluation:
   - R-squared (R²) = {r_value**2:.4f}
     Interpretation: The model explains {r_value**2*100:.2f}% of the variance in the dependent variable
   
   - P-value = {p_value:.4e}
     Interpretation: {"The model is statistically significant" if p_value < 0.05 else "The model is not statistically significant"}
   
   - Standard error = {std_err:.4f}
     Interpretation: Precision of the coefficient estimate

4. Example application:
   If the independent variable increases by 10 units, the dependent variable is expected to increase by {slope*10:.2f} units
""")

if __name__ == "__main__":
    path = sys.argv[1]
    x_par = sys.argv[2]
    y_par = sys.argv[3]
    explain_linear_regression()
    get_regression(path, x_par, y_par)
#python q8e.py '/home/yaxi4987/exercises6/EcommerceCustomers.csv' 'Length of Membership' 'Yearly Amount Spent'