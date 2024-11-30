import subprocess

def create_file_with_text(filename, text):
    # 使用 subprocess 调用 echo 命令，并将输出重定向到文件
    with open(filename, 'w') as file:
        subprocess.run(['echo', text], stdout=file)

# 示例用法
create_file_with_text('output.txt', 'This is a single line of text.')
