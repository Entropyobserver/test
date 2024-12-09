import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\J\Desktop\language technology\course\combined_words.csv')


df = pd.DataFrame(data)

df = df[df['Duration'] != 0] 

plt.hist(df['Duration'], bins=10, edgecolor='black')

plt.title('Histogram of Word Durations')
plt.xlabel('Duration (rounded)')
plt.ylabel('Frequency')

#plt.savefig('word-level_his.png')
plt.show()
