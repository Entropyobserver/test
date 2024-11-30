"""


    By now, you should be familiar with your data. Try to think up
    a research question. It does not have to be groundbreaking. You
    saw in the lecture that we tried to see if there was a linear
    relation between weight and height. What variables (and here I
    am using "variable" to mean "column name in your data" -- not
    "Python variable") could potentially be correlated.

"""
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def get_regression(path,x_axis,y_axis):
    df = pd.read_csv(path)
    sns.regplot(
    data = df,x = x_axis, y = y_axis,
    scatter_kws={"s":10},
    line_kws={"color":"blue","linewidth":0.8})

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    plt.show()

if __name__ == "__main__":
    path = sys.argv[1]
    x_axis = sys.argv[2]
    y_axis = sys.argv[3]
    get_regression(path, x_axis, y_axis)
    