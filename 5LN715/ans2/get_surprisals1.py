from nltk import sent_tokenize, word_tokenize
import random 
import re
from math import log

def get_lines(path):
    with open(path,'r',) as f:
        lines =  f.read()
    return lines

def get_unigrams(sentences):
    unigram_dict ={}
    for sentence in sentences:
        word = word_tokenize(sentence)
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
        words = [word.lower()for word in words]
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bi_word = (words[i],words[i+1])
            if  bi_word in bigram_dict:
                bigram_dict[bi_word] += 1
            else:
                bigram_dict[bi_word] = 1
        return bigram_dict

def get_surprisal(p):
    s = -log(p,2)
    return s

def get_sentences(train_sentences):
    random_sentences = random.sample(train_sentences,40)
    selected_sentence = []
    for i, sentence in enumerate(random_sentences):
        #sentence = re.sub(r'[^\w\s]','',sentence)
        if len(sentence.split()) > 20:
            #sentence = sentence.strip().lower()
            selected_sentence.append(sentence)
            if len(selected_sentence) == 20:
                break
    for i,sentence in enumerate(selected_sentence):
        print(f"Randomd sentence {i + 1}:{sentence}")
    return selected_sentences
"""
def get_bigram_surprisal(unigram_dict,biggram_dict):
    bi_sur_dict = {}
    first_word,second_word = bi_word
    unigram_count = unigram_dict.get(first_word,0)
    bigram_count = bigram_dict(bi_word,0)
    unigram_count_smooth = unigram_count + 1
    bigram_count_smooth = bigram_count + 1
    cond_p = bigram_count_smooth / unigram_count_smooth
    s = -log(cond_p,2)
    bi_sur_dict[bi_word] = s
    return bi_sur_dict
"""

def get_sentence_surprisal(sentence,unigram_dict,bigram_dict):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words]
    words = ['<s>'] + words + ['<e>']
    total_surprial = 0
    word_surprials = []
    for i in range(len(words)-1):
        first_word =  word[i]
        second_word = word[i+1]
        bi_word = (first_word,second_word)
        unigram_count = unigram_dict.get(first_word,0)
        biagram_count = biagram_dcit.get(bi_word,0)
        unigram_count_smooth = unigram_count + 1
        biagram_count_smooth = biagram_count + 1
        cond_p = biagram_count_smooth / unigram_count_smooth
        surprisal = get_surprisal(cond_p)
        word_surprials.append(bo_word,surprisal)
    return total_surprial,word_surprials

if __name__ == "__main__":
    path = ('/home/yaxi4987/5LN715/ans2/wiki.train.raw')
    train = get_lines(path)
    train_sentences = sent_tokenize(train)

    unigram_dict = get_bigrams(train_sentences)
    bigram_dict = get_bigrams(train_sentences)


    selected_sentences =  get_sentences(train_sentences)
    #print(selected_sentence)
    for i,sentence in enumerate(selected_sentences):
        total_surprial,word_surprials = get_sentence_surprisal(sentence,unigram_dict,bigram_dict)
        print(f"\nSentence {i + 1}:")
        print(f"Total surprisal: {total_surprisal:.2f}")
        print("Word-by-word surprisal:")
        for (w1, w2), surp in word_surprisals:
            print(f"  {w1} → {w2}: {surp:.2f}")
"""
    print(train_sentences[181])
    print(train_sentences[268])
    print(train_sentences[169])
    print(train_sentences[158])
    print(train_sentences[148])
    print()
    print(train_sentences[138])
    print(train_sentences[128])
    print(train_sentences[118])
    print(train_sentences[108])
    print(train_sentences[118])
    print(train_sentences[108])
    print(train_sentences[108])
    print(train_sentences[118])
    print(train_sentences[108])
    print(train_sentences[98])
    print(train_sentences[88])
    print(train_sentences[78])
    print(train_sentences[68])
    print(train_sentences[58])
    print(train_sentences[48])
    print(train_sentences[38])
    print(train_sentences[28])
    print(train_sentences[18])
    print(train_sentences[9])
"""