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

def check_log_transformation(x, y):
    """
    Check if log transformation would improve the linear relationship
    Returns dictionary with transformation recommendations and statistics
    """
    # Calculate correlations for different transformations
    correlations = {
        'original': np.corrcoef(x, y)[0, 1],
        'log_x': np.corrcoef(np.log1p(x), y)[0, 1],
        'log_y': np.corrcoef(x, np.log1p(y))[0, 1],
        'log_both': np.corrcoef(np.log1p(x), np.log1p(y))[0, 1]
    }
    
    # Check skewness
    skewness = {
        'x': stats.skew(x),
        'y': stats.skew(y),
        'log_x': stats.skew(np.log1p(x)),
        'log_y': stats.skew(np.log1p(y))
    }
    
    # Create transformation recommendation
    best_corr = max(correlations.items(), key=lambda x: abs(x[1]))
    
    # Visualization of distributions
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Original distributions
    sns.histplot(x, ax=axes[0, 0], kde=True)
    axes[0, 0].set_title('Original X Distribution')
    sns.histplot(y, ax=axes[0, 1], kde=True)
    axes[0, 1].set_title('Original Y Distribution')
    
    # Log-transformed distributions
    sns.histplot(np.log1p(x), ax=axes[1, 0], kde=True)
    axes[1, 0].set_title('Log-transformed X Distribution')
    sns.histplot(np.log1p(y), ax=axes[1, 1], kde=True)
    axes[1, 1].set_title('Log-transformed Y Distribution')
    
    plt.tight_layout()
    plt.savefig('distribution_plots.png')
    plt.close()
    
    return {
        'correlations': correlations,
        'skewness': skewness,
        'best_transformation': best_corr[0],
        'best_correlation': best_corr[1]
    }

def make_predictions(model_params, x_new):
    """
    Make predictions using the fitted model parameters
    """
    return model_params['intercept'] + model_params['slope'] * x_new

def calculate_prediction_intervals(x_new, x, y, model_params, confidence=0.95):
    """
    Calculate prediction intervals for new observations
    """
    n = len(x)
    x_mean = np.mean(x)
    
    # Calculate MSE
    y_pred = make_predictions(model_params, x)
    mse = np.sum((y - y_pred)**2) / (n - 2)
    
    # Calculate standard error of prediction
    x_new = np.array(x_new)
    se_pred = np.sqrt(mse * (1 + 1/n + (x_new - x_mean)**2 / np.sum((x - x_mean)**2)))
    
    # Calculate t-value
    t_value = stats.t.ppf((1 + confidence) / 2, n - 2)
    
    # Calculate prediction intervals
    y_pred_new = make_predictions(model_params, x_new)
    pi_lower = y_pred_new - t_value * se_pred
    pi_upper = y_pred_new + t_value * se_pred
    
    return {
        'predictions': y_pred_new,
        'pi_lower': pi_lower,
        'pi_upper': pi_upper,
        'confidence': confidence
    }

def calculate_regression_parameters(x, y):
    """
    Calculate regression parameters with detailed steps
    """
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    SS_xx = np.sum((x - x_mean)**2)
    SS_yy = np.sum((y - y_mean)**2)
    SS_xy = np.sum((x - x_mean)*(y - y_mean))
    
    slope = SS_xy / SS_xx
    intercept = y_mean - slope * x_mean
    
    r_squared = (SS_xy)**2 / (SS_xx * SS_yy)
    
    y_pred = slope * x + intercept
    residuals = y - y_pred
    
    standard_error = np.sqrt(np.sum(residuals**2) / (n-2)) / np.sqrt(SS_xx)
    
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
    """Explain the detailed calculation process"""
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
    """Perform detailed residual analysis"""
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
    
    dw_stat = np.sum(np.diff(residuals)**2) / np.sum(residuals**2)
    print(f"\n• Durbin-Watson statistic: {dw_stat:.4f}")
    print("  - Tests for autocorrelation in residuals")
    print("  - Values near 2 suggest no autocorrelation")

def get_regression(path, x_par, y_par):
    print(f"\n====== Starting Regression Analysis ======")
    print(f"Variables analyzed:")
    print(f"Independent variable (x): {x_par}")
    print(f"Dependent variable (y): {y_par}")
    
    # Read the data
    df = pd.read_csv(path)
    print(f"\nPreview of original data:")
    print(df[[x_par, y_par]].head())
    
    x = df[x_par].values
    y = df[y_par].values
    
    # Check for log transformation
    print("\n====== Checking Log Transformation ======")
    log_check = check_log_transformation(x, y)
    print("\nCorrelation coefficients:")
    for transform, corr in log_check['correlations'].items():
        print(f"• {transform}: {corr:.4f}")
    print(f"\nBest transformation: {log_check['best_transformation']}")
    print(f"Best correlation: {log_check['best_correlation']:.4f}")
    print("\nSkewness statistics:")
    for var, skew in log_check['skewness'].items():
        print(f"• {var}: {skew:.4f}")
    
    # Calculate regression parameters
    results = calculate_regression_parameters(x, y)
    
    # Make predictions for example values
    x_new = np.linspace(min(x), max(x), 100)
    pred_intervals = calculate_prediction_intervals(x_new, x, y, results)
    
    # Plot regression with prediction intervals
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', alpha=0.5, label='Data points')
    plt.plot(x_new, pred_intervals['predictions'], color='red', label='Regression line')
    plt.fill_between(x_new, 
                    pred_intervals['pi_lower'], 
                    pred_intervals['pi_upper'], 
                    color='gray', 
                    alpha=0.2, 
                    label=f'{pred_intervals["confidence"]*100}% Prediction Interval')
    plt.xlabel(x_par)
    plt.ylabel(y_par)
    plt.title("Linear Regression with Prediction Intervals")
    plt.legend()
    plt.savefig("regression_with_intervals.png")
    plt.close()
    
    # Print detailed analysis results
    explain_calculations(results)
    analyze_residuals(results['residuals'], results['predicted'])
    
    # Create diagnostic plots
    plt.figure(figsize=(15, 10))
    
    plt.subplot(221)
    sns.scatterplot(x=results['predicted'], y=results['residuals'])
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel("Fitted values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted")
    
    plt.subplot(222)
    stats.probplot(results['residuals'], dist="norm", plot=plt)
    plt.title("Normal Q-Q Plot")
    
    plt.subplot(223)
    sns.scatterplot(x=results['predicted'], y=np.sqrt(np.abs(stats.zscore(results['residuals']))))
    plt.xlabel("Fitted values")
    plt.ylabel("√|Standardized residuals|")
    plt.title("Scale-Location")
    
    plt.subplot(224)
    leverage = np.diag(x[:, np.newaxis] @ np.linalg.inv(x[:, np.newaxis].T @ x[:, np.newaxis]) @ x[:, np.newaxis].T)
    sns.scatterplot(x=leverage, y=stats.zscore(results['residuals']))
    plt.xlabel("Leverage")
    plt.ylabel("Standardized residuals")
    plt.title("Residuals vs Leverage")
    
    plt.tight_layout()
    plt.savefig("diagnostic_plots.png")
    print("\n• Diagnostic plots saved as 'diagnostic_plots.png'")
    
    return results, log_check, pred_intervals

if __name__ == "__main__":
    #path = r"D:\J\Desktop\ecommerce\1\Ecommerce Customers.csv"
    path = r"/home/yaxi4987/5LN429/exercises6/EcommerceCustomers.csv"
    x_par = 'Length of Membership'
    y_par = 'Yearly Amount Spent'
    explain_linear_regression()
    results, log_check, predictions = get_regression(path, x_par, y_par)