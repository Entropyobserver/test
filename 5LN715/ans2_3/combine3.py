import pandas as pd
import os

# Define file paths
file_paths = [
    r"D:\J\Desktop\language technology\course\output_sentences1.csv",
    r"D:\J\Desktop\language technology\course\output_sentences2.csv",
    r"D:\J\Desktop\language technology\course\output_sentences3.csv",
    r"D:\J\Desktop\language technology\course\output_sentences4.csv",
    r"D:\J\Desktop\language technology\course\output_sentences5.csv",
    r"D:\J\Desktop\language technology\course\output_sentences6.csv",
    r"D:\J\Desktop\language technology\course\output_sentences7.csv",
    r"D:\J\Desktop\language technology\course\output_sentences8.csv",
    r"D:\J\Desktop\language technology\course\output_sentences9.csv",
    r"D:\J\Desktop\language technology\course\output_sentences10.csv",
    r"D:\J\Desktop\language technology\course\output_sentences11.csv",
    r"D:\J\Desktop\language technology\course\output_sentences12.csv",
    r"D:\J\Desktop\language technology\course\output_sentences13.csv",
    r"D:\J\Desktop\language technology\course\output_sentences14.csv",
    r"D:\J\Desktop\language technology\course\output_sentences15.csv"   

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
output_file_path = r"D:\J\Desktop\language technology\course\combined_sentences.csv"
combined_df.to_csv(output_file_path, index=False)

print(f"Combined content saved to {output_file_path}")

