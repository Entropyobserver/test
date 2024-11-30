import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV files
quick_sort_df = pd.read_csv('/home/yaxi4987/5LN715/ans1/assignment_4/quick_sort_times.csv')
bubble_sort_df = pd.read_csv('/home/yaxi4987/5LN715/ans1/assignment_4/bubble_sort_times.csv')

# Create the plot
plt.figure(figsize=(12, 6))

# Plot actual measured times
plt.plot(quick_sort_df['size'], quick_sort_df['time'], label='Quick Sort Actual', color='blue', marker='o', linestyle='')
plt.plot(bubble_sort_df['size'], bubble_sort_df['time'], label='Bubble Sort Actual', color='red', marker='x', linestyle='')

# Fit theoretical complexity curves
# For Quick Sort (expected O(n log n))
quick_sort_fit = np.polyfit(quick_sort_df['size'], quick_sort_df['time'], 2)
quick_sort_curve = np.poly1d(quick_sort_fit)

# For Bubble Sort (expected O(n^2))
bubble_sort_fit = np.polyfit(bubble_sort_df['size'], bubble_sort_df['time'], 2)
bubble_sort_curve = np.poly1d(bubble_sort_fit)

# Generate smooth curve for plotting
size_range = np.linspace(min(quick_sort_df['size']), max(quick_sort_df['size']), 100)
plt.plot(size_range, quick_sort_curve(size_range), label='Quick Sort Trend', color='blue', linestyle='--')
plt.plot(size_range, bubble_sort_curve(size_range), label='Bubble Sort Trend', color='red', linestyle='--')

# Customize the plot
plt.title('Sorting Algorithms Time Complexity Comparison', fontsize=16)
plt.xlabel('Input Size (n)', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Use logarithmic scale for better visualization
plt.xscale('log')
plt.yscale('log')

# Show the plot
plt.tight_layout()
plt.savefig('time_complexity_comparison.png')
plt.show()