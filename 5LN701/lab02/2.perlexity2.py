from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys, time

def get_lines(path):
    with open(path, 'r') as f:
        train = f.read()
    return train

def get_unigrams(sentences):
    unigram_dict = {}
    words = ['<s>'] + word_tokenize(sentences) + ['</s>']
    for word in words:
        unigram_dict[word] = unigram_dict.get(word, 0) + 1
    return unigram_dict

def get_bigrams(sentences):
    bigram_dict = {}
    words = ['<s>'] + word_tokenize(sentences) + ['</s>'] 
    for i in range(len(words)-1):
        bi_word = (words[i], words[i+1]) 
        bigram_dict[bi_word] = bigram_dict.get(bi_word, 0) + 1
    return bigram_dict

def get_surprisal(p):
    s = -log(p, 2)
    return s

def get_bigram_surprisal(unigram_dict, bigram_dict):
    bi_sur_dict = {}
    bi_prob_dict = {}  # 新增一个概率字典
    for bi_word in bigram_dict:
        first_word, second_word = bi_word
        unigram_count = unigram_dict.get(first_word, 0)
        bigram_count = bigram_dict.get(bi_word, 0) 
        unigram_count_smooth = unigram_count + 1
        bigram_count_smooth = bigram_count + 1
        
        # 计算条件概率
        cond_p = bigram_count_smooth / unigram_count_smooth
        
        # 存储概率
        bi_prob_dict[bi_word] = cond_p
        
        # 计算惊奇值
        s = -log(cond_p, 2)
        bi_sur_dict[bi_word] = s
    
    return bi_sur_dict, bi_prob_dict  # 返回惊奇值和概率字典

def get_perplexity(bi_surp, bi_prob, test):
    """
    使用 bigram 的惊奇值计算测试数据的困惑度 (perplexity)。
    
    参数:
    - bi_surp: 字典，键为 bigram，值为对应的惊奇值 (surprisal)。
    - bi_prob: 字典，键为 bigram，值为对应的概率。
    - test: 测试数据列表，每个句子为一个字符串。
    
    返回:
    - perplexity: 测试数据的困惑度值。
    """
    total_surp = 0.0  # 累积的总惊奇值
    word_count = 0    # 测试数据中的总单词数量
    
    # 计算默认惊奇值，用于未见 bigram 的情况
    total_bigrams = len(bi_surp)
    default_surp = get_surprisal(1/total_bigrams)
    default_prob = 1/total_bigrams
    print(f"Default surprisal for unseen bigrams: {default_surp}")
    print(f"Default probability for unseen bigrams: {default_prob}")
    
    for sentence in test:
        # 使用 word_tokenize 分词
        words = ['<s>'] + word_tokenize(sentence) + ['</s>'] 
        word_count += len(words) - 1  # 更新总单词数 (不包括 <s>)
        print(f"Processed sentence: {words}")
        
        # 第 2 步：处理第一个 bigram (<s>, first_word)
        first_bigram = ('<s>', words[1])
        surprisal_value = bi_surp.get(first_bigram, default_surp)
        probability_value = bi_prob.get(first_bigram, default_prob)
        total_surp += surprisal_value
        print(f"Bigram: {first_bigram}, Probability: {probability_value:.6f}, Surprisal: {surprisal_value:.6f}")
        
        # 第 3 步：处理句子中的所有 bigram
        for i in range(1, len(words) - 1):
            bigram = (words[i], words[i + 1])
            surprisal_value = bi_surp.get(bigram, default_surp)
            probability_value = bi_prob.get(bigram, default_prob)
            total_surp += surprisal_value
            print(f"Bigram: {bigram}, Probability: {probability_value:.6f}, Surprisal: {surprisal_value:.6f}")
    
    # 第 4 步：计算平均惊奇值
    avg_surprisal = total_surp / word_count
    print(f"Average surprisal (entropy): {avg_surprisal:.6f}")
    
    # 第 5 步：计算困惑度
    perplexity = 2 ** avg_surprisal
    print(f"Calculated perplexity: {perplexity:.6f}")
    
    return perplexity

def main():
    train_sentences = "I would much rather eat pizza than ice cream ."
    test_sentences = "I love anchovies on my pizza ."
    
    unigram_freq = get_unigrams(train_sentences)
    print("Unigram Frequencies:")
    for key, value in unigram_freq.items():
        print(f"{key}, {value}")
    
    bigram_freq = get_bigrams(train_sentences)
    print("\nBigram Frequencies:")
    for key, value in bigram_freq.items():
        print(f"{key}, {value}")
    
    bi_sur_dict, bi_prob_dict = get_bigram_surprisal(unigram_freq, bigram_freq)
    print("\nBigram Probabilities:")
    for key, value in bi_prob_dict.items():
        print(f"{key}, {value:.6f}")
    
    perplexity = get_perplexity(bi_sur_dict, bi_prob_dict, [test_sentences])
    print(f"\nPerplexity on Test Set: {perplexity:.6f}")

if __name__ == "__main__":
    main()