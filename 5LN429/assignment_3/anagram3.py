import sys
from collections import defaultdict

# 读取文件并返回文件内容的列表
def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines

# 读取词汇表文件并去掉空白字符
def get_lexicon(path):
    lexicon = []
    lines = get_lines(path)
    for line in lines:
        line = line.strip()
        lexicon.append(line)
    return lexicon

# 对字符串中的字母排序
def get_sorted(lst):
    sorted_lst = sorted(lst)
    return sorted_lst

# 生成一个字典，字典的键是排序后的单词，值是相同字母组合的单词列表
def get_dict(lexicon):
    anagram_dict = defaultdict(list)
    for word in lexicon:
        sorted_word = ''.join(get_sorted(word))
        anagram_dict[sorted_word].append(word)
    return anagram_dict

# 找到输入单词的所有字母异序词
def get_anagram(anagram_dict, input_word):
    sorted_input_word = ''.join(sorted(input_word))
    anagram_lst = []
    if sorted_input_word in anagram_dict:
        for word in anagram_dict[sorted_input_word]:
            if word != input_word:
                anagram_lst.append(word)
    return anagram_lst

# 主函数

def main():
    lexicon = get_lexicon('sv-utf8.txt')
    
    # 确保词汇表不是空的
    if not lexicon:
        print("Lexicon is empty or file could not be read.")
        return
    
    anagram_dict = get_dict(lexicon)
    
    # 接收命令行输入的单词
    if len(sys.argv) < 2:
        print("Please provide an input word.")
        return
    
    input_word = sys.argv[1]
    
    # 查找字母异序词
    anagrams = get_anagram(anagram_dict, input_word)
    
    # 输出结果
    if anagrams:
        print("Anagrams found:")
        for i in anagrams:
            print(i)
    else:
        print("No anagrams found for the word:", input_word)

if __name__ == '__main__':
    main()