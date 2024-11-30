
import difflib

def compare_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file1, tofile=file2, lineterm='')
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for line in diff:
            out_file.write(line + '\n')

# 示例文件路径
file1 = '/home/yaxi4987/5LN701/lab01/dev1-tok.txt'
file2 = '/home/yaxi4987/5LN701/lab01/dev1-gold.txt'
output_file = '/home/yaxi4987/5LN701/lab01/diff.txt'

compare_files(file1, file2, output_file)
