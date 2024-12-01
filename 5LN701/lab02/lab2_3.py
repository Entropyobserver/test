import math
from nltk import sent_tokenize, word_tokenize, FreqDist
from collections import defaultdict
from math import log
import sys, time

def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.read()
    return lines

def get_unigrams(sentences):
    unigram = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = ['<s>'] + words + ['<e>']
        for word in words:
            unigram[word] += 1
    return unigram

def get_bigrams(sentences):
    bigram = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = ['<s>'] + words + ['<e>']
        for w1, w2 in zip(words, words[1:]):
            bigram[(w1.lower(), w2.lower())] += 1
    return bigram

def get_surprisal(prob):
    return -math.log2(prob)

def get_bigram_surprisal(unigram, bigram):
    bigram_surprisal = defaultdict(float)
    for key in bigram.keys():
        first_word = key[0]
        prob_first_word = unigram.get(first_word, 0) + 1
        bigram_freq = bigram.get(key, 0) + 1
        bigram_prob = bigram_freq / prob_first_word
        surprisal = get_surprisal(bigram_prob)
        bigram_surprisal[key] = surprisal
    return bigram_surprisal

def get_perplexity(bi_surprisal, test_set):
    total_surp = 0
    word_count = 0
    for sentence in test_set:
        words = word_tokenize(sentence)
        words = ['<s>'] + words + ['<e>']
        for w1, w2 in zip(words, words[1:]):
            surprise = bi_surprisal.get((w1.lower(), w2.lower()), get_surprisal(1 / len(bi_surprisal)))
            total_surp += surprise
            word_count += 1
    perplexity = math.pow(2, (total_surp / word_count))
    return perplexity

def main():
    filename = sys.argv[1]
    train = get_lines(filename)
    train_sentences = sent_tokenize(train)
    test_filename = sys.argv[2]
    test = get_lines(test_filename)
    test_sentences = sent_tokenize(test)

    unigram_freq = get_unigrams(train_sentences)
    bigram_freq = get_bigrams(train_sentences)
    raw_bigram_surprisal = get_bigram_surprisal(unigram_freq, bigram_freq)
    perplexity = get_perplexity(raw_bigram_surprisal, test_sentences)

    print(raw_bigram_surprisal.get(('this', 'is')))
    print(raw_bigram_surprisal.get(('this', 'issue')))
    print(raw_bigram_surprisal.get(('and', 'why')))
    print(raw_bigram_surprisal.get(('which', 'can')))
    print(perplexity)

if __name__ == "__main__":
    main()
#python lab2_3.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw' 
#python lab2_3.py '/home/yaxi4987/5LN701/lab02/wiki.test.raw' 
#python lab2_3.py '/home/yaxi4987/5LN701/lab02/wiki.train.raw' '/home/yaxi4987/5LN701/lab02/wiki.test.raw'  