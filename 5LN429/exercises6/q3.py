"""

    Use the slides, the internet (e.g., ChatGPT, stackoverflow, YouTube etc.)
    to learn about using pandas.

    Play around with the data by visualizing it.
    Start with what seems most intuitive. A barchart? A scatterplot?
    This depends on what the data are.


"""
import pandas as pd
path = '/home/yaxi4987/exercises6/EcommerceCustomers.csv'
data = pd.read_csv(path)
print("step1:Reading data")
print(data.head())
print("step2:EDA analysis")
print(data.info()) 
print(".............................")
print(data.isnull().sum())
print(".............................")
print(data.describe())
print(".............................")
print(data.dtypes)
print(".............................")

num_data = data[['Avg. Session Length','Time on App','Time on Website','Length of Membership','Yearly Amount Spent']]
print(num_data.head(5))
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def get_scatterplot(path,x_axis,y_axis):
    df = pd.read_csv(path)
    plt.scatter(df[x_axis],df[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()

#plt.scatter(num_data['Length of Membership'],num_data['Yearly Amount Spent'])
#plt.xlabel('Length of Membership')
#plt.ylabel('Yearly Amount Spent')
#plt.show()
if __name__ == "__main__":
    path = sys.argv[1]
    x_axis = sys.argv[2]
    y_axis = sys.argv[3]
    get_scatterplot(path, x_axis, y_axis)
#python q3.py /home/yaxi4987/exercises6/EcommerceCustomers.csv 'Length of Membership' 'Yearly Amount Spent'
