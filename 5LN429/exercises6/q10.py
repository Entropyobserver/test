import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

def calculate_regression_parameters(x, y):
    """
    Calculate regression parameters with detailed steps
    """
    n = len(x)
    # Step 1: Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Step 2: Calculate sums of squares
    # Sum of squares for x
    SS_xx = np.sum((x - x_mean)**2)
    # Sum of squares for y
    SS_yy = np.sum((y - y_mean)**2)
    # Sum of cross products
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
    n = len(x)
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

def explain_calculations(calc_results):
    """
    Explain the detailed calculation process
    """
    print("\n====== DETAILED CALCULATION PROCESS ======")
    print("\n1. PARAMETER CALCULATIONS")
    print("-------------------------------------------")
    print("Step 1: Calculate Means")
    print(f"  x̄ = {calc_results['calculations']['x_mean']:.4f}")
    print(f"  ȳ = {calc_results['calculations']['y_mean']:.4f}")
    
    print("\nStep 2: Calculate Sum of Squares")
    print(f"  SS_xx = Σ(x - x̄)² = {calc_results['calculations']['SS_xx']:.4f}")
    print(f"  SS_yy = Σ(y - ȳ)² = {calc_results['calculations']['SS_yy']:.4f}")
    print(f"  SS_xy = Σ(x - x̄)(y - ȳ) = {calc_results['calculations']['SS_xy']:.4f}")
    
    print("\nStep 3: Calculate Slope (β₁)")
    print(f"  β₁ = SS_xy / SS_xx = {calc_results['slope']:.4f}")
    
    print("\nStep 4: Calculate Intercept (β₀)")
    print(f"  β₀ = ȳ - β₁x̄ = {calc_results['intercept']:.4f}")

def analyze_residuals(residuals, y_pred):
    """
    Perform detailed residual analysis
    """
    print("\n====== DETAILED RESIDUAL ANALYSIS ======")
    print("\n1. RESIDUAL STATISTICS")
    print("-------------------------------------------")
    print(f"• Mean of residuals: {np.mean(residuals):.4f}")
    print("  - Should be close to 0 for unbiased model")
    
    print(f"\n• Standard deviation of residuals: {np.std(residuals):.4f}")
    print("  - Measures the spread of prediction errors")
    
    print(f"\n• Skewness of residuals: {stats.skew(residuals):.4f}")
    print("  - Measures asymmetry of residual distribution")
    print("  - Values close to 0 indicate symmetrical distribution")
    
    print(f"\n• Kurtosis of residuals: {stats.kurtosis(residuals):.4f}")
    print("  - Measures the 'tailedness' of residual distribution")
    print("  - Positive values indicate heavy tails")
    
    # Durbin-Watson statistic
    dw_stat = np.sum(np.diff(residuals)**2) / np.sum(residuals**2)
    print(f"\n• Durbin-Watson statistic: {dw_stat:.4f}")
    print("  - Tests for autocorrelation in residuals")
    print("  - Values near 2 suggest no autocorrelation")

def get_regression(path, x_par, y_par):
    # [Previous code remains the same until regression statistics calculation]
    
    df = pd.read_csv(path)
    x = df[x_par].values
    y = df[y_par].values
    
    # Calculate regression parameters with detailed steps
    results = calculate_regression_parameters(x, y)
    
    # Original results printing remains the same...
    [Previous printing code]
    
    # Add detailed calculation explanation
    explain_calculations(results)
    
    # Add detailed residual analysis
    analyze_residuals(results['residuals'], results['predicted'])
    
    # Add diagnostic plots
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Residuals vs Fitted
    plt.subplot(221)
    sns.scatterplot(x=results['predicted'], y=results['residuals'])
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel("Fitted values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted")
    
    # Plot 2: Q-Q plot
    plt.subplot(222)
    stats.probplot(results['residuals'], dist="norm", plot=plt)
    plt.title("Normal Q-Q Plot")
    
    # Plot 3: Scale-Location
    plt.subplot(223)
    sns.scatterplot(x=results['predicted'], y=np.sqrt(np.abs(stats.zscore(results['residuals']))))
    plt.xlabel("Fitted values")
    plt.ylabel("√|Standardized residuals|")
    plt.title("Scale-Location")
    
    # Plot 4: Residuals vs Leverage
    plt.subplot(224)
    leverage = np.diag(x[:, np.newaxis] @ np.linalg.inv(x[:, np.newaxis].T @ x[:, np.newaxis]) @ x[:, np.newaxis].T)
    sns.scatterplot(x=leverage, y=stats.zscore(results['residuals']))
    plt.xlabel("Leverage")
    plt.ylabel("Standardized residuals")
    plt.title("Residuals vs Leverage")
    
    plt.tight_layout()
    plt.savefig("diagnostic_plots.png")
    print("\n• Diagnostic plots saved as 'diagnostic_plots.png'")

if __name__ == "__main__":
    path = sys.argv[1]
    x_par = sys.argv[2]
    y_par = sys.argv[3]
    explain_linear_regression()
    get_regression(path, x_par, y_par)
    #python script.py '/home/yaxi4987/exercises6/EcommerceCustomers.csv' 'Length of Membership' 'Yearly Amount Spent'