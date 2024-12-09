from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys,time

def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        train = f.read()
    return train

def get_unigrams(sentences):
    unigram_dict = {}
    for sentence in sentences:
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
    bigram_dict = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words)-1):
            bi_word = (words[i] , words[i+1]) 
            if bi_word in bigram_dict:
                bigram_dict[bi_word] += 1
            else:
                bigram_dict[bi_word] = 1
    return bigram_dict

def get_surprisal(p):
    s = -log(p,2)
    return s

def get_bigram_surprisal(unigram_dict,bigram_dict):
    bi_sur_dict = {}
    #V = len(unigram_dict)  # 词汇表大小包括所有训练集的 unigram
    V = 1  # 添加一个未见 unigram 的概率
    
    # Debug: Print vocabulary size and some key stats
    print(f"\nTotal unique unigrams: {len(unigram_dict)}")
    print("First 10 unigrams:")
    for key in list(unigram_dict.keys())[:10]:
        print(f"{key}: {unigram_dict[key]}")
    
    print(f"\nTotal unique bigrams: {len(bigram_dict)}")
    print("First 10 bigrams:")
    for key in list(bigram_dict.keys())[:10]:
        print(f"{key}: {bigram_dict[key]}")
    
    for bi_word in bigram_dict:
        first_word,second_word = bi_word
        unigram_count = unigram_dict.get(first_word,0)
        bigram_count = bigram_dict.get(bi_word,0)

        if unigram_count == 0:
            cond_p = 1 / V
        else:
            cond_p = (bigram_count + 1) / (unigram_count + V)

        s = -log(cond_p,2)
        bi_sur_dict[bi_word] = s
    
    # Debug: Print some surprisal values
    print("\nSample Bigram Surprisal Values:")
    sample_bigrams = list(bi_sur_dict.keys())[:10]
    for bigram in sample_bigrams:
        print(f"{bigram}: {bi_sur_dict[bigram]}")
    
    return bi_sur_dict

def get_perplexity(bi_surp, test):
    total_surp = 0.0  # 累积的总惊奇值
    word_count = 0    # 测试数据中的总单词数量
    
    # 计算默认惊奇值，用于未见 bigram 的情况
    total_bigrams = len(bi_surp)
    default_surp = get_surprisal(1/total_bigrams)
    print(f"Default surprisal for unseen bigrams: {default_surp}")
    
    for sentence in test:
        # 第 1 步：对句子进行分词并添加 <s> 和 <e>
        words = word_tokenize(sentence)
        words = ['<s>'] + words + ['<e>']
        words = [word.lower() for word in words]
        word_count += len(words) - 1  # 更新总单词数 (不包括 <s>)
        print(f"Processed sentence: {words}")
        
        # 第 2 步：处理第一个 bigram (<s>, first_word)
        first_bigram = ('<s>', words[1])
        surprisal_value = bi_surp.get(first_bigram, default_surp)
        total_surp += surprisal_value
        print(f"Bigram: {first_bigram}, Surprisal: {surprisal_value}")
        
        # 第 3 步：处理句子中的所有 bigram
        for i in range(1, len(words) - 1):
            bigram = (words[i], words[i + 1])
            surprisal_value = bi_surp.get(bigram, default_surp)
            total_surp += surprisal_value
            print(f"Bigram: {bigram}, Surprisal: {surprisal_value}")
    
    # 第 4 步：计算平均惊奇值
    avg_surprisal = total_surp / word_count
    print(f"Average surprisal (entropy): {avg_surprisal}")
    
    # 第 5 步：计算困惑度
    perplexity = 2 ** avg_surprisal
    print(f"Calculated perplexity: {perplexity}")
    
    return perplexity

import csv
def save_to_csv(data, file_path, header): 
    with open(file_path, 'w', newline='', encoding='utf-8') as f: 
        writer = csv.writer(f) 
        writer.writerow(header) 
        for key, value in data.items(): 
            writer.writerow([key, value])

def main():
    path1 = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.train_1147.raw"
    train = get_lines(path1)
    path2 = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.test.raw"
    test = get_lines(path2)
    train_sentences = sent_tokenize(train)
    test_sentences = sent_tokenize(test)

    unigram_freq = get_unigrams(train_sentences)
    bigram_freq = get_bigrams(train_sentences)

    unigram_freq_test = get_unigrams(test_sentences) 
    bigram_freq_test = get_bigrams(test_sentences)

    save_to_csv(unigram_freq_test, 'unigram_freq_test.csv', ['Unigram', 'Frequency']) 
    save_to_csv(bigram_freq_test, 'bigram_freq_test.csv', ['Bigram', 'Frequency'])
    
    bi_sur_dict = get_bigram_surprisal(unigram_freq, bigram_freq)

    perplexity = get_perplexity(bi_sur_dict, test_sentences)
    print(f"\nPerplexity on Test Set: {perplexity}")

if __name__ == "__main__":
    main()
"""

Key points I've made:
1. Kept ALL of your original code logic intact
2. Added some debug print statements to help you understand what's happening
3. Preserved the `V = 1` setting you had in the original code

The main additions are print statements in `get_bigram_surprisal()` and `get_perplexity()` to show:
- Vocabulary size
- First 10 unigrams and their counts
- First 10 bigrams and their counts
- Sample bigram surprisal values

"""
