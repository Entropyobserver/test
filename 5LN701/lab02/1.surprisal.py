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
    #for sentence in sentences:
        #words = word_tokenize(sentence)
        #words = [word.lower() for word in words]
        #words = ['<s>'] + words + ['<e>']
    words = ['<s>'] + sentences.split() + ['</s>']
    for word in words:
        if word in unigram_dict:
            unigram_dict[word] += 1
        else:
            unigram_dict[word] = 1
    return unigram_dict

def get_bigrams(sentences):
    bigram_dict = {}
    #for sentence in sentences:
        #words = word_tokenize(sentence)
        #words = [word.lower() for word in words]
        #words = ['<s>'] + words + ['</s>']
        #words = ['<s>'] + word_tokenize(sentence) + ['</e>']
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
        unigram_count_smooth = unigram_count + 1
        bigram_count_smooth = bigram_count + 1
        cond_p = bigram_count_smooth / unigram_count_smooth
        s = -log(cond_p,2)
        bi_sur_dict[bi_word] = s
    return bi_sur_dict

def main():
    #path = sys.argv[1]
    #train = get_lines(path)
    #path = sys.argv[2]
    #test = get_lines(path)
    #train_sentences = sent_tokenize(train)
    #test_sentences = sent_tokenize(test)
    train_sentences = "I would much rather eat pizza than ice cream ."
    test_sentences ="I love anchovies on my pizza . "
    unigram_freq = get_unigrams(train_sentences)
    for key,value in unigram_freq.items():
        print(f"{key},{value}")
    bigram_freq = get_bigrams(train_sentences)
    for key,value in bigram_freq.items():
        print(f"{key},{value}")
    bi_sur_dict = get_bigram_surprisal(unigram_freq, bigram_freq)
    for key,value in bi_sur_dict.items():
        print({key},{value})
    #perplexity = get_perplexity(bi_sur_dict, test_sentences)
    #print(f"\nPerplexity on Test Set: {perplexity}")


if __name__ == "__main__":
    main()

#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw' 
#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 
#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw' '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 
#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train.raw' '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 