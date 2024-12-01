from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys,time

def get_lines(path):
    with open(path,'r') as f:
        train = f.read()
    return train

def get_unigrams(sentences):
    unigram_dict = {}
    words = ['<s>'] + sentences.split() + ['</s>']
    for word in words:
        if word in unigram_dict:
            unigram_dict[word] += 1
        else:
            unigram_dict[word] = 1
    return unigram_dict

def get_bigrams(sentences):
    bigram_dict = {}
    words = ['<s>'] + sentences.split() + ['</s>'] 
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
    for bi_word in bigram_dict:
        first_word,second_word = bi_word
        unigram_count = unigram_dict.get(first_word,0)
        bigram_count = bigram_dict.get(bi_word,0) 
        unigram_count_smooth = unigram_count + 1#
        bigram_count_smooth = bigram_count + 1#   
        cond_p = bigram_count_smooth / unigram_count_smooth
        s = -log(cond_p,2)
        bi_sur_dict[bi_word] = s
    return bi_sur_dict

def get_perplexity(bi_surp, test):
    """
    使用 bigram 的惊奇值计算测试数据的困惑度 (perplexity)。
    
    参数:
    - bi_surp: 字典，键为 bigram，值为对应的惊奇值 (surprisal)。
    - test: 测试数据列表，每个句子为一个字符串。
    
    返回:
    - perplexity: 测试数据的困惑度值。
    """
    total_surp = 0.0  # 累积的总惊奇值
    word_count = 0    # 测试数据中的总单词数量
    
    # 计算默认惊奇值，用于未见 bigram 的情况
    total_bigrams = len(bi_surp)
    default_surp = get_surprisal(1/total_bigrams)
    
    # 输出默认惊奇值信息
    print(f"Default surprisal for unseen bigrams: {default_surp}")
    
    # 处理测试语料中的每个句子
    for sentence in [test]:  # 使用列表解析
        # 分词并添加句子开始和结束标记
        words = ['<s>'] + sentence.split() + ['</s>']
        
        # 更新总词数
        word_count += len(words) - 1
        
        # 输出处理的句子
        print(f"Processed sentence: {words}")
        
        # 处理第一个 bigram（从句子开始到第一个词）
        first_bigram = ('<s>', words[1])
        surprisal_value = bi_surp.get(first_bigram, default_surp)
        total_surp += surprisal_value
        print(f"Bigram: {first_bigram}, Surprisal: {surprisal_value}")
        
        # 处理句子中的所有后续 bigram
        for i in range(1, len(words) - 1):
            bigram = (words[i], words[i + 1])
            surprisal_value = bi_surp.get(bigram, default_surp)
            total_surp += surprisal_value
            print(f"Bigram: {bigram}, Surprisal: {surprisal_value}")
    
    # 计算平均惊奇值
    avg_surprisal = total_surp / word_count
    print(f"Average surprisal (entropy): {avg_surprisal}")
    
    # 计算并返回困惑度
    perplexity = 2 ** avg_surprisal
    print(f"Calculated perplexity: {perplexity}")
    
    return perplexity

def main():
    train_sentences = "I would much rather eat pizza than ice cream ."
    test_sentences = "I love anchovies on my pizza . "
    unigram_freq = get_unigrams(train_sentences)
    bigram_freq = get_bigrams(train_sentences)
    for key,value in unigram_freq.items():
        print(f"{key},{value}")
    for key,value in bigram_freq.items():
        print(f"{key},{value}")
    bi_sur_dict = get_bigram_surprisal(unigram_freq, bigram_freq)
    perplexity = get_perplexity(bi_sur_dict, test_sentences)
    print(f"\nPerplexity on Test Set: {perplexity}")

if __name__ == "__main__":
    main()