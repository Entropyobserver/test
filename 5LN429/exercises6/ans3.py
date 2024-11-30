import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys

def get_regression(path, x_par, y_par):
    df = pd.read_csv(path)
    
    sns.regplot(
        data=df, x=x_par, y=y_par,
        scatter_kws={"s": 10},
        line_kws={"color": "blue", "linewidth": 0.8}
    )
    plt.xlabel(x_par)
    plt.ylabel(y_par)
    plt.savefig("reg_plot.png")
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])
    return {
        'Intercept': intercept,
        'Coefficient': slope,
        'R-squared': r_value**2,
        'P-value': p_value
    }

if __name__ == "__main__":
    path = sys.argv[1]
    x_par = sys.argv[2]
    y_par = sys.argv[3]
    result = get_regression(path, x_par, y_par)
    print(result)