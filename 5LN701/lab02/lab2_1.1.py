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

def find_test_bigrams_in_train(test_bigrams, train_bigrams):
    bigram_counts = {}
    for bigram in test_bigrams:
        if bigram in train_bigrams:
            bigram_counts[bigram] = train_bigrams[bigram]
        else:
            bigram_counts[bigram] = 0
    return bigram_counts

def save_to_csv(data, file_path, header):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for key, value in data.items():
            writer.writerow([key, value])

def main():
    path1 = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.train.raw"
    train = get_lines(path1)
    path2 = r"D:\J\Desktop\language technology\course\5LN701\lab02\wiki.test.raw"
    test = get_lines(path2)
    train_sentences = sent_tokenize(train)
    test_sentences = sent_tokenize(test)

    unigram_freq_train = get_unigrams(train_sentences)
    bigram_freq_train = get_bigrams(train_sentences)
    
    unigram_freq_test = get_unigrams(test_sentences)
    bigram_freq_test = get_bigrams(test_sentences)
    
    # Find test bigrams in train bigrams
    test_bigrams_in_train = find_test_bigrams_in_train(bigram_freq_test, bigram_freq_train)
    
    # Save unigram and bigram frequencies to CSV files
    #save_to_csv(unigram_freq_train, 'unigram_freq_train.csv', ['Unigram', 'Frequency'])
    #save_to_csv(bigram_freq_train, 'bigram_freq_train.csv', ['Bigram', 'Frequency'])
    #save_to_csv(unigram_freq_test, 'unigram_freq_test.csv', ['Unigram', 'Frequency'])
    #save_to_csv(bigram_freq_test, 'bigram_freq_test.csv', ['Bigram', 'Frequency'])
    save_to_csv(test_bigrams_in_train, 'test_bigrams_in_train.csv', ['Bigram', 'Train Frequency'])
    
    print("Unigram and bigram frequencies for both train and test sets have been saved to CSV files.")
    print("Test bigrams and their frequencies in the train set have been saved to CSV file.")

if __name__ == "__main__":
    main()
