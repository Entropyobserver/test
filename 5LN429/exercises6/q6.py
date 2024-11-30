"""

    Now, it is time to go beyond programming even more. Use the internet
    to find out what a linear regression is telling you. 

    Here is some code:

from scipy import stats

    Then last in your function (I assume you have a function where you
    did the plot), add this:


    slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])

    return {
        'Intercept': intercept,
        'Coefficient': slope,
        'R-squared': r_value**2,
        'P-value': p_value
    }

    To know you got the numbers right, you can replicate your code
    on the howell1.csv data. Then you should get this:

{'Intercept': -7.956016781808177, 'Coefficient': 2.3244783070055894, 'R-squared': 0.9520874138862362, 'P-value': 0.0}

    Go on to the last task!
"""
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
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys
def get_regression(path, x_par, y_par):
    df = pd.read_csv(path)
    df[x_par] = np.log(df[x_par])
    df[y_par] = np.log(df[y_par])
    
    sns.regplot(
        data=df, x=x_par, y=y_par,
        scatter_kws={"s": 10},
        line_kws={"color": "blue", "linewidth": 0.8}
    )
    plt.xlabel(f"Log({x_par})")
    plt.ylabel(f"Log({y_par})")
    plt.savefig("log_reg_plot.png")
    
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
    get_regression(path, x_par, y_par)

#python q6.py '/home/yaxi4987/exercises6/EcommerceCustomers.csv' 'Length of Membership' 'Yearly Amount Spent'
#python /home/yaxi4987/q6.py '/home/yaxi4987/EcommerceCustomers.csv' 'Length of Membership' 'Yearly Amount Spent'

"""