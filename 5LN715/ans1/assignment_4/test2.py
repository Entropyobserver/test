import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the CSV file
file_path = r'D:\J\Desktop\language technology\s\5LN715\ans1\assignment_4\bubble_sort_times.csv'
data = pd.read_csv(file_path)

# Display the first few rows
print("Dataset Preview:")
print(data.head())

# Check the structure of the data
print("\nDataset Info:")
print(data.info())

import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot with linear regression
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.regplot(x="size", y="time", data=data, scatter_kws={'s': 10}, line_kws={"color": "red"})

# Add labels and title
plt.xlabel("Size of List", fontsize=12)
plt.ylabel("Time Taken (seconds)", fontsize=12)
plt.title("Bubble Sort Time vs. List Size", fontsize=14)
plt.show()
plt.savefig('bubble_sort_times.png')