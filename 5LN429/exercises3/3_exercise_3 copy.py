def get_clean(word):
    return word.lower().strip(".")

def get_bigrams(lst):
    bigrams_freq = {}
    for i in range(len(lst)-1):
        current_word = get_clean(lst[i])
        next_word = get_clean(lst[i+1])
        bigram = (current_word, next_word)
        if bigram in bigrams_freq:
            bigrams_freq[bigram] += 1
        else:
            bigrams_freq[bigram] = 1
    return bigrams_freq

sentence = "I love the sun. I love the sun and the sun is a star. I love a star"

my_bigrams = get_bigrams(sentence.split())

for bigram, frequency in my_bigrams.items():
    print(bigram, frequency)




