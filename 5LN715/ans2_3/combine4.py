import pandas as pd
import os

# Define file paths
file_paths = [
    r"D:\J\Desktop\language technology\course\output_words1.csv",
    r"D:\J\Desktop\language technology\course\output_words2.csv",
    r"D:\J\Desktop\language technology\course\output_words3.csv",
    r"D:\J\Desktop\language technology\course\output_words4.csv",
    r"D:\J\Desktop\language technology\course\output_words5.csv",
    r"D:\J\Desktop\language technology\course\output_words6.csv",
    r"D:\J\Desktop\language technology\course\output_words7.csv",
    r"D:\J\Desktop\language technology\course\output_words8.csv",
    r"D:\J\Desktop\language technology\course\output_words9.csv",
    r"D:\J\Desktop\language technology\course\output_words10.csv",
    r"D:\J\Desktop\language technology\course\output_words11.csv",
    r"D:\J\Desktop\language technology\course\output_words12.csv",
    r"D:\J\Desktop\language technology\course\output_words13.csv",
    r"D:\J\Desktop\language technology\course\output_words14.csv",
    r"D:\J\Desktop\language technology\course\output_words15.csv"
]

# Combine CSV file contents
combined_df = pd.DataFrame()
for file_path in file_paths:
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    else:
        print(f"File not found: {file_path}")

# Write the combined content to a new file
output_file_path = r"D:\J\Desktop\language technology\course\combined_words.csv"
combined_df.to_csv(output_file_path, index=False)

print(f"Combined content saved to {output_file_path}")

