from nltk import sent_tokenize, word_tokenize
import random 
import re
from math import log
import os
import get_duration

def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read()
    return lines

def get_unigrams(sentences):
    unigram_dict = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for word in words:
            unigram_dict[word] = unigram_dict.get(word, 0) + 1
    return unigram_dict

def get_bigrams(sentences):#bigram_dict
    bigram_dict = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bi_word = (words[i], words[i+1])
            bigram_dict[bi_word] = bigram_dict.get(bi_word, 0) + 1
    return bigram_dict

def get_surprisal(p):
    return -log(p, 2)

def get_bigram_surprisal(sentence, unigram_dict, bigram_dict):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words]
    words = ['<s>'] + words + ['<e>']
    word_surprisals = []
    
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i+1]
        bi_word = (first_word, second_word)
        
        unigram_count = unigram_dict.get(first_word, 0)
        bigram_count = bigram_dict.get(bi_word, 0)
        
        unigram_count_smooth = unigram_count + 1
        bigram_count_smooth = bigram_count + 1
        
        cond_p = bigram_count_smooth / unigram_count_smooth
        surprisal = get_surprisal(cond_p)
        
        word_surprisals.append((bi_word, surprisal))
    
    return word_surprisals

def get_test_surprisal(sentence, unigram_dict, bigram_dict):
    total_surprisal = 0
    sentence_surprisals = []
    for word, surprisal in get_bigram_surprisal(sentence, unigram_dict, bigram_dict):
        total_surprisal += surprisal
        sentence_surprisals.append((word, surprisal))
    return sentence_surprisals

if __name__ == "__main__":
    path = '/home/yaxi4987/5LN715/ans2/wiki.train.raw'
    path = r'D:\J\Desktop\language technology\s\5LN715\ans2\wiki.train.raw'
    train = get_lines(path)
    train_sentences = sent_tokenize(train)

    unigram_dict = get_unigrams(train_sentences)
    bigram_dict = get_bigrams(train_sentences)


    

    # 计算惊奇值
    word_surprisals = get_bigram_surprisal(sentence2, unigram_dict, bigram_dict)

    # 打印结果
    print(f"Total surprisal: {total_surprisal:.2f}")
    print("Word-by-word surprisal:")
    for (w1, w2), surp in word_surprisals:
        print(f"  {w1} → {w2}: {surp:.2f}")
    
    #durations = get_duration(sentence2)
    #print(durations)