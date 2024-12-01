from nltk import word_tokenize
from math import log

def get_unigrams(sentences):
    words = ['<s>'] + word_tokenize(sentences) + ['</s>']
    unigram_dict = {}
    for word in words:
        unigram_dict[word] = unigram_dict.get(word, 0) + 1
    return unigram_dict

def get_bigrams(sentences):
    words = ['<s>'] + word_tokenize(sentences) + ['</s>']
    bigram_dict = {}
    for i in range(len(words)-1):
        bi_word = (words[i], words[i+1])
        bigram_dict[bi_word] = bigram_dict.get(bi_word, 0) + 1
    return bigram_dict

def get_bigram_surprisal(unigram_dict, bigram_dict):
    bi_sur_dict = {}  # 惊奇值字典
    bi_prob_dict = {}  # 概率字典
    total_words = sum(unigram_dict.values())

    for bi_word in bigram_dict:
        first_word, second_word = bi_word
        first_word_count = unigram_dict.get(first_word, 0)
        bigram_count = bigram_dict.get(bi_word, 0)

        # 加1平滑
        unigram_count_smooth = first_word_count + 1
        bigram_count_smooth = bigram_count + 1
        vocab_size = len(unigram_dict)

        # 条件概率计算
        cond_p = bigram_count_smooth / (first_word_count + vocab_size + 1)
        
        # 存储概率
        bi_prob_dict[bi_word] = cond_p
        
        # 计算惊奇值
        s = -log(cond_p, 2)
        bi_sur_dict[bi_word] = s

    return bi_sur_dict, bi_prob_dict

# 训练数据
train_sentences = "I would much rather eat pizza than ice cream ."

# 计算 unigram 和 bigram
unigram_freq = get_unigrams(train_sentences)
bigram_freq = get_bigrams(train_sentences)

# 计算惊奇值和概率
bi_sur_dict, bi_prob_dict = get_bigram_surprisal(unigram_freq, bigram_freq)

# 打印 unigram 频率
print("Unigram Frequencies:")
for word, freq in unigram_freq.items():
    print(f"{word}: {freq}")

# 打印 bigram 频率
print("\nBigram Frequencies:")
for bigram, freq in bigram_freq.items():
    print(f"{bigram}: {freq}")

# 打印概率和惊奇值
print("\nBigram Probabilities and Surprisal:")
for bigram, prob in bi_prob_dict.items():
    surprisal = bi_sur_dict[bigram]
    print(f"{bigram}: Prob = {prob:.6f}, Surprisal = {surprisal:.6f}")

# 测试句子
test_sentences = "I love anchovies on my pizza ."

# 计算测试句子的惊奇值
def calculate_sentence_perplexity(test_sentences, bi_sur_dict, bi_prob_dict):
    words = ['<s>'] + word_tokenize(test_sentences) + ['</s>']
    total_surprisal = 0
    word_count = len(words) - 1  # 不计算 <s>

    print("\nTest Sentence Bigram Analysis:")
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        
        # 默认概率（使用总 bigram 数作为基准）
        default_prob = 1 / len(bi_prob_dict)
        default_surprisal = -log(default_prob, 2)
        
        # 获取实际概率和惊奇值
        prob = bi_prob_dict.get(bigram, default_prob)
        surprisal = bi_sur_dict.get(bigram, default_surprisal)
        
        total_surprisal += surprisal
        print(f"Bigram: {bigram}, Prob = {prob:.6f}, Surprisal = {surprisal:.6f}")

    # 计算平均惊奇值（熵）
    avg_surprisal = total_surprisal / word_count
    print(f"\nAverage Surprisal (Entropy): {avg_surprisal:.6f}")

    # 计算困惑度
    perplexity = 2 ** avg_surprisal
    print(f"Perplexity: {perplexity:.6f}")

    return perplexity

# 计算困惑度
calculate_sentence_perplexity(test_sentences, bi_sur_dict, bi_prob_dict)