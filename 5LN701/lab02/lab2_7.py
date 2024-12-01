from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys,time

def get_lines(path):
    with open(path,'r',encoding='utf-8') as f:
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

def main():
    #path = sys.argv[1]
    path1 = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.train_1147.raw"
    train = get_lines(path1)
    #path = sys.argv[2]
    path2 = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.test.raw"
    test = get_lines(path2)
    train_sentences = sent_tokenize(train)
    test_sentences = sent_tokenize(test)
    print((len(train)))
    print(train.split()[1])
    print(train_sentences[181])


    unigram_freq = get_unigrams(train_sentences)
    print(unigram_freq.get('around'))
    print(unigram_freq.get('select'))
    print(unigram_freq.get('<s>'))
    print(unigram_freq.get('<e>'))


    #print("Vocabulary size (with <s>, <e>):", len(unigram_freq))
    #print("Vocabulary size (without <s>, <e>):", len(unigram_freq) - 2)
    #print("Frequency of <s>:", unigram_freq.get('<s>', 0))
    #print("Frequency of <e>:", unigram_freq.get('<e>', 0))


    #from itertools import islice
    #for key,value in islice(unigram_freq.items(),10):
    #    print(f"{key}:{value}")


    bigram_freq = get_bigrams(train_sentences)
    print(bigram_freq.get(('agreed','to')))
    print(bigram_freq.get(('into','aspects')))
    print(bigram_freq.get(('<s>','while')))
    print(bigram_freq.get(('.','<e>')))

    #for key,value in islice(bigram_freq.items(),10):
    #    print(f"{key}:{value}")
    
    bi_sur_dict = get_bigram_surprisal(unigram_freq, bigram_freq)

    #prob1 = (bigram_freq.get(('<s>', '=')) + 1) / (unigram_freq.get('<s>') + 1)
    #print(f"Method 1 Probability: {prob1}")
    #prob2 = bi_sur_dict.get(('<s>', '='), None)
    #print(f"Method 2 Surprisal: {prob2} -> Converted Probability: {2 ** -prob2}")

    #for key, value in islice(sur_dict.items(), 10):
    #    print(f"{key}: {value}")

    
    #print(get_surprisal(1))
    #print(get_surprisal(0.5))
    #print(get_surprisal(0.3))
    #print(get_surprisal(0.1))


    print(f"bi_sur_dict.get(('this','is')): {bi_sur_dict.get(('this','is'))}")
    print(f"bi_sur_dict.get(('this','issue')): {bi_sur_dict.get(('this','issue'))}")
    print(f"bi_sur_dict.get(('and','why')): {bi_sur_dict.get(('and','why'))}")
    print(f"bi_sur_dict.get(('which','can')): {bi_sur_dict.get(('which','can'))}")


    #prob3 = bi_sur_dict.get((('this','is')), None)
    #print(f"Method 2 Surprisal: {prob3} -> Converted Probability: {2 ** -prob3}")


    #print("Vocabulary size (with <s>, <e>):", len(unigram_freq))
    #print("Vocabulary size (without <s>, <e>):", len(unigram_freq) - 2)
    #print("Frequency of <s>:", unigram_freq.get('<s>', 0))
    #print("Frequency of <e>:", unigram_freq.get('<e>', 0))



    perplexity = get_perplexity(bi_sur_dict, test_sentences)
    print(f"\nPerplexity on Test Set: {perplexity}")


if __name__ == "__main__":
    main()

#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw' 
#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 
#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw' '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 
#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train.raw' '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 

#python lab_7.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw' '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 