import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\J\Desktop\language technology\course\5LN715\ans2\output.csv')

df = pd.DataFrame(data)


plt.hist(df['Duration'], bins=10, edgecolor='black')

plt.title('Histogram of Word Durations')
plt.xlabel('Duration (rounded)')
plt.ylabel('Frequency')

plt.show()
