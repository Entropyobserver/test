import os

# 定义文件路径
file_paths = [
    "output/sentence_1.txt",
    "output/sentence_2.txt",
    "output/sentence_3.txt",
    "output/sentence_4.txt",
    "output/sentence_5.txt",
    "output/sentence_6.txt",
    "output/sentence_7.txt",
    "output/sentence_8.txt",
    "output/sentence_9.txt",
    "output/sentence_10.txt",
    "output/sentence_11.txt",
    "output/sentence_12.txt",
    "output/sentence_13.txt",
    "output/sentence_14.txt",
    "output/sentence_15.txt"
]

# 合并文件内容
combined_content = ""
for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        combined_content += file.read().strip() + " "

# 将合并后的内容写入新文件
output_file_path = "output/combined_sentences.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combined_content.strip())

print(f"Combined content saved to {output_file_path}")
