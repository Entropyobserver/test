"""

    Use the slides, the internet (e.g., ChatGPT, stackoverflow, YouTube etc.)
    to learn about using pandas.

    Play around with the data by visualizing it.
    Start with what seems most intuitive. A barchart? A scatterplot?
    This depends on what the data are.


"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def get_scatterplot(path,x_axis,y_axis):
    df = pd.read_csv(path)
    plt.scatter(df[x_axis],df[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show
test = get_scatterplot(sys.argv[1],sys.argv[2],sys.argv[3])

#plt.scatter(num_data['Length of Membership'],num_data['Yearly Amount Spent'])
#plt.xlabel('Length of Membership')
#plt.ylabel('Yearly Amount Spent')
#plt.show()
