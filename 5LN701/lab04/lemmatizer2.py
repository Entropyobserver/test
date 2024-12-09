import sys

def noun_lemma(word):
    #word = word.lower()
    if word.endswith("s"):
        return word[:-1]
    else:
        return word


def verb_lemma(word):
    #word = word.lower()
    if word.endswith("ing"):#1 0.7%
        return word[:-3]
    elif word.endswith("ed"):
        return word[:-2]
    elif word in ['has','had']:
        return "have"
    elif word in ['is','am','was','were','are']:
        return "be"
    else:
        return word

def adj_lemma(word):
    #word = word.lower()
    if word.endswith("er"):
        return word[:-2]
    elif word.endswith("est"):
        return word[:-3]
    else:
        return word


for line in sys.stdin:
    if line.strip():
        (word, tag) = line.strip().split("\t")
        lemma = word
        if tag == "NOUN":
            lemma = noun_lemma(word.lower())
        elif tag == "VERB":
            lemma = verb_lemma(word.lower())
        elif tag == "ADJ":
            lemma = adj_lemma(word.lower())
        else:
            lemma = word.lower()
        print("{0}\t{1}\t{2}".format(word, tag, lemma))
    else:
        print()

#python3 lemmatizer.py < ewt-dev-wt.txt > ewt-dev-out.txt
#python3 score.py lemma ewt-dev-wtl.txt ewt-dev-out.txt
#vimdiff ewt-dev-wtl.txt ewt-dev-out.txt