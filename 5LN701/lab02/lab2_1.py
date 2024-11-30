from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys,time


#import nltk
#nltk.download('punkt')

def get_lines(path):
    with open(path,'r') as f:
        train = f.read()
    return train

def main():
    path = sys.argv[1]
    train = get_lines(path)
    sentences = sent_tokenize(train)
    print((len(train)))
    print(train.split()[1])
    print(sentences[181])
    unigram_freq = get_unigrams(sentences)
    print(unigram_freq.get('around'))
    print(unigram_freq.get('select'))
    print(unigram_freq.get('<s>'))
    print(unigram_freq.get('<e>'))
    bigram_freq = get_bigrams(sentences)
    print(bigram_freq.get(('agreed','to')))
    print(bigram_freq.get(('into','aspects')))
    print(bigram_freq.get(('<s>','while')))
    print(bigram_freq.get(('.','<e>')))

def get_unigrams(sentences):
    unigram_dict = {}
    for sentence in sentences:
        words = ['<s>'] + word_tokenize(sentence) + ['<e>']
        for word in words:
            if word in unigram_dict:
                unigram_dict[word] += 1
            else:
                unigram_dict[word] = 1
    return unigram_dict
"""
def get_bigrams(sentences):
    bigram_dict = {}
    for word in range(len(sentences)-1):
        bi_word = (sentences[word],sentences[word+1]) 
        if bi_word in bigram_dict:
            bigram_dict[bi_word] += 1
        else:
            bigram_dict[bi_word] = 1
    return bigram_dict
"""
def get_bigrams(sentences):
    bigram_dict = {}
    for sentence in sentences:
        words = ['<s>'] + word_tokenize(sentence) + ['<e>']
        for i in range(len(words)-1):
            bi_word = (words[i] , words[i+1]) 
            if bi_word in bigram_dict:
                bigram_dict[bi_word] += 1
            else:
                bigram_dict[bi_word] = 1
    return bigram_dict

main()


