from nltk import sent_tokenize, word_tokenize
import random
import re
from math import log
import os
from get_duration import get_duration

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

def get_bigrams(sentences):
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
"""
def calculate_word_surprisal(word, prev_word, unigram_dict, bigram_dict):
    # Smooth the counts
    unigram_count = unigram_dict.get(prev_word, 0) + 1
    bigram_count = bigram_dict.get((prev_word, word), 0) + 1
    
    # Calculate conditional probability
    cond_p = bigram_count / unigram_count
    
    # Calculate surprisal
    return get_surprisal(cond_p)

def get_test_surprisal(sentence, unigram_dict, bigram_dict,durations = None):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words]
    #words = ['<s>'] + words + ['<e>']
    
    total_surprisal = 0
    word_surprisals = []

    for i in range(1, len(words)):
        prev_word = words[i-1]
        current_word = words[i]
        
        surprisal = calculate_word_surprisal(current_word, prev_word, unigram_dict, bigram_dict)
        
        total_surprisal += surprisal
        word_surprisals.append(((prev_word, current_word), surprisal))

    return total_surprisal, word_surprisals

def calculate_duration_surprisal(sentence, unigram_dict, bigram_dict, durations):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words]
    
    word_durations_surprisals = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1]
        current_word = words[i]
        
        # 获取持续时间
        duration = durations.get(current_word, 0)
        
        # 计算惊奇值
        surprisal = calculate_word_surprisal(current_word, prev_word, unigram_dict, bigram_dict)
        
        # 保存结果 (word, duration, surprisal)
        word_durations_surprisals.append((current_word, duration, surprisal))
    
    return word_durations_surprisals


if __name__ == "__main__":
    path = '/home/yaxi4987/5LN715/ans2/wiki.train.raw'
    train = get_lines(path)
    train_sentences = sent_tokenize(train)

    unigram_dict = get_unigrams(train_sentences)
    bigram_dict = get_bigrams(train_sentences)

    sentence2 = "Norman settlements were characterised by the establishment of baronies , manors , towns and the seeds of the modern county system ."
    
    # Calculate durations
    durations = {'': 0.15097916666666666, 'Norman': 0.032975, 'settlements': 0.05745833333333334, 'were': 0.0124875, 'characterised': 0.07895833333333335, 'by': 0.016991666666666665, 'the': 0.021975, 'establishment': 0.07595000000000002, 'of': 0.014983333333333335, 'baronies': 0.06697083333333333, 'manors': 0.05297916666666667, 'towns': 0.053983333333333335, 'and': 0.009991666666666668, 'seeds': 0.03698333333333334, 'modern': 0.042979166666666666, 'county': 0.033979166666666664, 'system': 0.054975}
    
    word_durations_surprisals = calculate_duration_surprisal(sentence2, unigram_dict, bigram_dict, durations)
    
    for word, duration, surprisal in word_durations_surprisals:
        print(f"Word: {word}, Duration: {duration}, Surprisal: {surprisal}")



