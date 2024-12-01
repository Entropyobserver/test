import re, sys

def read_lines(path):
   with open(path,'r') as f:
       lines = f.readlines()
       return lines

def tokenize(text):
   # 处理缩略语
   text = re.sub(r"\b(\w+)n't\b", r"\1 n't ", text)  # can't -> ca n't
   text = re.sub(r"\b(\w+)'s\b", r"\1 's ", text)    # it's -> it 's
   
   # 定义需要匹配的模式, 注意括号匹配
   pattern = r"(?:\w+\.(?:\w+\.)+|\w+\.|(?:\w+\.\w+\.(?:\w+)*)|(?:\d+\.\d+)|(?:\w+(?:-\w+)*)|(?:\b\w+\b)|(?:[%#$""''.,:;!?'']))"
   
   # 使用findall找出所有匹配
   tokens = re.findall(pattern, text)
   return tokens

def main():
   path = sys.argv[1]
   lines = read_lines(path)
   
   for line in lines:
       # 对每行进行分词
       tokens = tokenize(line.strip())
       # 打印每个token
       for token in tokens:
           print(token)

if __name__ == "__main__":
   main()
#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt'
#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev1-tok.txt'
#vimdiff dev1-gold.txt dev1-tok.txt
#python3 score-tokens.py dev1-gold.txt dev1-tok.txt

#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev2-tok.txt'
#vimdiff dev1-gold.txt dev2-tok.txt
#python3 score-tokens.py dev1-gold.txt dev2-tok.txt

#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt'
#python nlp5LN701tokenizer2.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev3-tok.txt'
#vimdiff dev1-gold.txt dev3-tok.txt
#python3 score-tokens.py dev1-gold.txt dev3-tok.txt