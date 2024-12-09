from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
import csv

def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        train = f.read()
    return train

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

def get_bigrams(sentences):
    bigram_dict = {}
    for sentence in sentences:
        words = ['<s>'] + word_tokenize(sentence) + ['<e>']
        for i in range(len(words) - 1):
            bi_word = (words[i], words[i + 1])
            if bi_word in bigram_dict:
                bigram_dict[bi_word] += 1
            else:
                bigram_dict[bi_word] = 1
    return bigram_dict

def save_to_csv(data, file_path, header):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for key, value in data.items():
            writer.writerow([key, value])

def main():
    path = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.train.raw"
    train = get_lines(path)
    sentences = sent_tokenize(train)
    
    unigram_freq = get_unigrams(sentences)
    bigram_freq = get_bigrams(sentences)
    
    # Save unigram and bigram frequencies to CSV files
    save_to_csv(unigram_freq, 'unigram_freq.csv', ['Unigram', 'Frequency'])
    save_to_csv(bigram_freq, 'bigram_freq.csv', ['Bigram', 'Frequency'])
    
    print("Unigram and bigram frequencies have been saved to CSV files.")

main()
