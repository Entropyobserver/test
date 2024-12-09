from nltk import word_tokenize 
from collections import defaultdict 
import nltk

# 确保下载punkt
nltk.download('punkt', quiet=True)

def get_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            train = f.read()
        return train
    except FileNotFoundError:
        print(f"文件 {path} 未找到")
        return ""
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return ""

def get_unigrams(sentences):
    unigram_dict = {}
    for sentence in sentences:
        if not sentence.strip():  # 跳过空行
            continue
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for word in words:
            if word in unigram_dict:
                unigram_dict[word] += 1
            else:
                unigram_dict[word] = 1
    return unigram_dict

def get_bigrams(sentences):
    bigram_dict = defaultdict(int)
    for sentence in sentences:
        if not sentence.strip():  # 跳过空行
            continue
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bi_word = (words[i], words[i + 1])
            bigram_dict[bi_word] += 1
    return bigram_dict

def count_zero_bigrams(unigram_dict, bigram_dict):
    zero_bigrams = 0
    for word1 in unigram_dict:
        for word2 in unigram_dict:
            if (word1, word2) not in bigram_dict:
                zero_bigrams += 1
    return zero_bigrams

# Example usage
path = r'D:\J\Desktop\language technology\course\5LN701\lab02\wiki.train.raw'
sentences = [s.strip() for s in get_lines(path).split('\n') if s.strip()]  # 过滤空行

unigram_dict = get_unigrams(sentences) 
bigram_dict = get_bigrams(sentences)  

zero_bigrams_count = count_zero_bigrams(unigram_dict, bigram_dict) 
print(f"Number of bigrams with zero frequency: {zero_bigrams_count}")