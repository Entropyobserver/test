from nltk import sent_tokenize, word_tokenize
import random 
import re
from math import log
import os

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
def get_sentences(train_sentences):
    random_sentences = random.sample(train_sentences, 40)
    selected_sentences = []
    for sentence in random_sentences:
        if len(sentence.split()) > 20:
            selected_sentences.append(sentence)
            if len(selected_sentences) == 20:
                break
    
    for i, sentence in enumerate(selected_sentences):
        print(f"Random sentence {i + 1}: {sentence}")
    return selected_sentences
"""
def get_sentence_surprisal(sentence, unigram_dict, bigram_dict):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words]
    words = ['<s>'] + words + ['<e>']
    total_surprisal = 0
    word_surprisals = []
    
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i+1]
        bi_word = (first_word, second_word)
        
        unigram_count = unigram_dict.get(first_word, 0)
        bigram_count = bigram_dict.get(bi_word, 0)
        
        unigram_count_smooth = unigram_count + 1
        bigram_count_smooth = bigram_count + 1
        
        cond_p = bigram_count_smooth / unigram_count_smooth
        surprisal = get_surprisal(cond_p)
        
        total_surprisal += surprisal
        word_surprisals.append((bi_word, surprisal))
    
    return total_surprisal, word_surprisals
"""
def save_sentences(sentences, output_dir='output'):
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        for i, sentence in enumerate(sentences, 1):
            file_path = os.path.join(output_dir, f"sentence_{i}.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(sentence)
            print(f"Sentence {i} saved to {file_path}")
   
    except Exception as e:
        print(f"Error saving sentences: {e}")
"""
if __name__ == "__main__":
    path = '/home/yaxi4987/5LN715/ans2/wiki.train.raw'
    train = get_lines(path)
    train_sentences = sent_tokenize(train)

    unigram_dict = get_unigrams(train_sentences)
    bigram_dict = get_bigrams(train_sentences)

    #selected_sentences = get_sentences(train_sentences)
    
    #for i, sentence in enumerate(selected_sentences):
    #    total_surprisal, word_surprisals = get_sentence_surprisal(sentence, unigram_dict, bigram_dict)
    #    print(f"\nSentence {i + 1}:")
    #    print(f"Total surprisal: {total_surprisal:.2f}")
    #    print("Word-by-word surprisal:")
    #    for (w1, w2), surp in word_surprisals:
    #        print(f"  {w1} → {w2}: {surp:.2f}")
    #save_sentences(selected_sentences)
    sentence2 = "Norman settlements were characterised by the establishment of baronies , manors , towns and the seeds of the modern county system ."
    print(f"\nSentence: {sentence2}")

    # 计算惊奇值
    total_surprisal, word_surprisals = get_sentence_surprisal(sentence2, unigram_dict, bigram_dict)

    # 打印结果
    print(f"Total surprisal: {total_surprisal:.2f}")
    print("Word-by-word surprisal:")
    for (w1, w2), surp in word_surprisals:
        print(f"  {w1} → {w2}: {surp:.2f}")