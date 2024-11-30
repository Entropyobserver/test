import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

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
    
    # Print detailed analysis results with comprehensive explanations
    print(f"\n====== DETAILED REGRESSION ANALYSIS RESULTS ======\n")
    
    print("1. BASIC STATISTICAL MEASURES")
    print("-------------------------------------------")
    print(f"• Mean of {x_par}: {df[x_par].mean():.4f}")
    print("  - This represents the average membership duration in the dataset")
    print(f"• Mean of {y_par}: {df[y_par].mean():.4f}")
    print("  - This represents the average yearly spending amount")
    print(f"• Covariance: {df[x_par].cov(df[y_par]):.4f}")
    print("  - Indicates the strength and direction of the linear relationship")
    print("  - Positive value shows that variables tend to increase together\n")

    print("2. REGRESSION EQUATION ANALYSIS")
    print("-------------------------------------------")
    print(f"• Equation: y = {slope:.4f}x + {intercept:.4f}")
    print("• Interpretation:")
    print(f"  - Slope ({slope:.4f}):")
    print("    * For each additional year of membership")
    print(f"    * Spending increases by ${slope:.2f}")
    print(f"  - Intercept ({intercept:.4f}):")
    print("    * Theoretical spending when membership length is 0")
    print("    * Baseline spending amount\n")

    print("3. MODEL EVALUATION METRICS")
    print("-------------------------------------------")
    print(f"• Correlation Coefficient (R): {r_value:.4f}")
    print("  - Measures the strength and direction of the relationship")
    print("  - Range: -1 to +1 (current value indicates strong positive correlation)")
    
    print(f"\n• R-squared (R²): {r_value**2:.4f}")
    print("  - Explains the percentage of variance accounted for by the model")
    print(f"  - {r_value**2*100:.2f}% of spending variation is explained by membership length")
    print("  - Remaining variance may be due to other factors")
    
    print(f"\n• P-value: {p_value:.4e}")
    print("  - Measures statistical significance")
    print("  - Extremely low value (<0.05) indicates high statistical significance")
    print("  - Current value suggests the relationship is not due to chance")
    
    print(f"\n• Standard Error: {std_err:.4f}")
    print("  - Measures the average distance between predicted and actual values")
    print("  - Lower values indicate more precise predictions")

    print("\n4. RESIDUAL ANALYSIS")
    print("-------------------------------------------")
    # Calculate residuals
    y_pred = slope * df[x_par] + intercept
    residuals = df[y_par] - y_pred
    sum_squared_residuals = np.sum(residuals ** 2)
    
    print(f"• Sum of Squared Residuals: {sum_squared_residuals:.4f}")
    print("  - Measures the total prediction error")
    print("  - Lower values indicate better model fit")
    
    # Create residuals plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_pred, y=residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.title("Residuals Plot")
    plt.savefig("residuals_plot.png")
    print("\n• Residuals plot saved as 'residuals_plot.png'")

    print("\n5. PRACTICAL IMPLICATIONS")
    print("-------------------------------------------")
    print("• Business Insights:")
    print("  - Strong positive relationship between membership length and spending")
    print(f"  - Each year of membership adds ${slope:.2f} in yearly spending")
    print(f"  - Model explains {r_value**2*100:.2f}% of spending variation")
    print("  - High statistical significance suggests reliable predictions")
    
    print("\n6. PREDICTION EXAMPLE")
    print("-------------------------------------------")
    print(f"• If membership length increases by 10 units:")
    print(f"  - Expected spending increase: ${slope*10:.2f}")
    print("• Note: Predictions are most reliable within the observed range of data")

if __name__ == "__main__":
    path = sys.argv[1]
    x_par = sys.argv[2]
    y_par = sys.argv[3]
    explain_linear_regression()
    get_regression(path, x_par, y_par)

#python q9.py '/home/yaxi4987/exercises6/EcommerceCustomers.csv' 'Length of Membership' 'Yearly Amount Spent'
