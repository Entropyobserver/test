import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_csv("/home/yaxi4987/5LN715/ans1/assignment_2/bubble_sort_times.csv")
print(data.head())
x = data['time']
y = data['size']
plt.plot(x,y)
x_label = 'time'
y_label = 'size'
plt.title('Bubble Sort Times') # Save the figure 
plt.savefig('bubble_sort_times_plot.png')
plt.show()
