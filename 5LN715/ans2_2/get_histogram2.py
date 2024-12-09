import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data with a different encoding
try:
    data = pd.read_csv(r'D:\J\Desktop\language technology\course\combined_sentences.csv', encoding='latin1')
except UnicodeDecodeError:
    data = pd.read_csv(r'D:\J\Desktop\language technology\course\combined_sentences.csv', encoding='cp1252')

# Create a DataFrame
df = pd.DataFrame(data)

# Remove rows where 'Duration' is 0
df = df[df['Duration'] != 0]

# Plot the histogram
plt.hist(df['Duration'], bins=10, edgecolor='black')

plt.title('Histogram of Word Durations')
plt.xlabel('Duration (rounded)')
plt.ylabel('Frequency')

plt.show()
