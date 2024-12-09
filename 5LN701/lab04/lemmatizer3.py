import sys

def noun_lemma(word):
    word = word.lower()
    if word.endswith("s"):
        return word[:-1]
    else:
        return word

def verb_lemma(word):
    word = word.lower()
    if word.endswith("ed"):
        return word[:-2]
    elif word.endswith("ing"):
        return word[:-3] + "e"
    elif word.endswith('es'):
        return word[:-1]
    #elif word.endwith('e'):
    #    return word[:-1]
    elif word in ['has','had']:
        return "have"
    elif word in ['is','am','was','were','are']:
        return "be"
    else:
        return word

def adj_lemma(word):
    word = word.lower()
    if word.endswith("er"):
        return word[:-2]
    elif word.endswith("est"):
        return word[:-3]
    else:
        return word

def aux_lemma(word):
    word = word.lower()

        
def adp_lemma(word):
    word = word.lower()
    return word

def det_lemma(word):
    word = word.lower()
    return word

def pron_lemma(word):
    word = word.lower()
    if word == 'his':
        return "he"
    elif word == 'her':
        return "she"
    else:
        return word


for line in sys.stdin:
    if line.strip():
        (word, tag) = line.strip().split("\t")
        lemma = word
        if tag == "NOUN":
            lemma = noun_lemma(word)
        elif tag == "VERB":
            lemma = verb_lemma(word)
        elif tag == "ADJ":
            lemma = adj_lemma(word)
        elif tag == "ADP":
            lemma == adp_lemma(word)
        elif tag == "DET":
            lemma == det_lemma(word)
        elif tag == 'PRON':
            lemma ==pron_lemma(word)
        else:
            lemma = word
        print("{0}\t{1}\t{2}".format(word, tag, lemma))
    else:
        print()


#python3 lemmatizer.py < ewt-dev-wt.txt > ewt-dev-out.txt
#python3 score.py lemma ewt-dev-wtl.txt ewt-dev-out.txt
#vimdiff ewt-dev-wtl.txt ewt-dev-out.txt