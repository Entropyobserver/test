from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys,time

def get_lines(path):
    with open(path,'r') as f:
        train = f.read()
    return train

def main():
    path = sys.argv[1]
    train = get_lines(path)


    sentences = sent_tokenize(train)
    #print((len(train)))
    #print(train.split()[1])
    #print(sentences[181])


    unigram_freq = get_unigrams(sentences)
    #print(unigram_freq.get('around'))
    #print(unigram_freq.get('select'))
    #print(unigram_freq.get('<s>'))
    #print(unigram_freq.get('<e>'))


    #print("Vocabulary size (with <s>, <e>):", len(unigram_freq))
    #print("Vocabulary size (without <s>, <e>):", len(unigram_freq) - 2)
    #print("Frequency of <s>:", unigram_freq.get('<s>', 0))
    #print("Frequency of <e>:", unigram_freq.get('<e>', 0))


    #from itertools import islice
    #for key,value in islice(unigram_freq.items(),10):
    #    print(f"{key}:{value}")


    bigram_freq = get_bigrams(sentences)
    #print(bigram_freq.get(('agreed','to')))
    #print(bigram_freq.get(('into','aspects')))
    #print(bigram_freq.get(('<s>','while')))
    #print(bigram_freq.get(('.','<e>')))

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


    #print(f"bi_sur_dict.get(('this','is')): {bi_sur_dict.get(('this','is'))}")
    #print(f"bi_sur_dict.get(('this','issue')): {bi_sur_dict.get(('this','issue'))}")
    #print(f"bi_sur_dict.get(('and','why')): {bi_sur_dict.get(('and','why'))}")
    #print(f"bi_sur_dict.get(('which','can')): {bi_sur_dict.get(('which','can'))}")


    #prob3 = bi_sur_dict.get((('this','is')), None)
    #print(f"Method 2 Surprisal: {prob3} -> Converted Probability: {2 ** -prob3}")


    #print("Vocabulary size (with <s>, <e>):", len(unigram_freq))
    #print("Vocabulary size (without <s>, <e>):", len(unigram_freq) - 2)
    #print("Frequency of <s>:", unigram_freq.get('<s>', 0))
    #print("Frequency of <e>:", unigram_freq.get('<e>', 0))



    perplexity = get_perplexity(bi_sur_dict, sentences)
    print(f"\nPerplexity on Test Set: {perplexity}")


def get_unigrams(sentences):
    unigram_dict = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        #words = ['<s>'] + word_tokenize(sentence) + ['<e>']
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
        #words = ['<s>'] + word_tokenize(sentence) + ['<e>']
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
    #p(wi+1|wi) = count(wi,wi+1) / count(wi)
    sur_dict = {}
    for bi_word in bigram_dict:
        if bi_word in bigram_dict:
            con_p = bigram_dict.get(bi_word) / unigram_dict.get()
            s = get_surprisal(con_p)
            sur_dict[bi_word] += 1
        else:
            sur_dict[bi_word] = 1
    return sur_dict

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

def get_perplexity(bi_surp, test):

    total_surp = 0.0
    word_count = 0
    total_bigrams = len(bi_surp)
    default_surp = -log(1/total_bigrams, 2)

    for sentence in test:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        word_count += len(words) - 1
        
        first_bigram = ('<s>', words[1])
        total_surp += bi_surp.get(first_bigram, default_surp)

        for i in range(1, len(words)-1):
            bigram = (words[i], words[i+1])
            total_surp += bi_surp.get(bigram, default_surp)

    avg_surprisal = total_surp / word_count
    perplexity = 2 ** avg_surprisal
    
    return perplexity 

if __name__ == "__main__":
    main()

#python lab2.py '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw'
