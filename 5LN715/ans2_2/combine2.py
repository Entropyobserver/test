import pandas as pd
import os

# 定义文件路径
file_paths = [
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_1.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_4.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_5.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_6.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_7.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_8.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_9.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_10.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_11.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_12.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_13.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_14.csv",
    r"D:\J\Desktop\language technology\course\ans2 copy\sentence_15.csv"
]

# 合并CSV文件内容
combined_df = pd.DataFrame()
for file_path in file_paths:
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# 将合并后的内容写入新文件
output_file_path = r"D:\J\Desktop\language technology\course\ans2 copy\combined_sentences.csv"
combined_df.to_csv(output_file_path, index=False)

print(f"Combined content saved to {output_file_path}")
