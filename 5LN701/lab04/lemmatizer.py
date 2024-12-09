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
    elif word in ['has','had']:
        return "have"
    elif word in ['is','am','was','were','are',"'s"]:
        return "be"
    elif word == 'got':
        return "get"
    elif word == 'came':
        return "come"
    elif word == 'did':
        return "do"
    elif word == "lost":
        return "lose"
    else:
        return word

def adj_lemma(word):
    word = word.lower()
    if word.endswith("er"):
        return word[:-2]
    elif word.endswith("est"):
        return word[:-3]
    elif word == 'best':
        return "best"
    else:
        return word

def aux_lemma(word):
    word = word.lower()
    if word == "has" or word == "had":
        return "have"
    elif word == "been":
        return "be"
    else:
        return word

        
def adp_lemma(word):
    word = word.lower()
    return word

def adv_lemma(word):
    word = word.lower()
    return word

def det_lemma(word):
    if word == 'an':
        return "a"
    word = word.lower()
    return word

def pron_lemma(word):
    word = word.lower()
    if word == 'his':
        return "he"
    elif word == 'her':
        return "she"
    elif word == "their":
        return "they"
    elif word == "i" or word == 'me':
        return "I"
    else:
        return word

def part_lemma(word):
    word = word.lower()
    if word == "n't":
        return "not"
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
            lemma = adp_lemma(word)
        elif tag == "DET":
            lemma = det_lemma(word)
        elif tag == 'PRON':
            lemma = pron_lemma(word)
        elif tag == "AUX":
            lemma = aux_lemma(word)
        elif tag == "ADV":
            lemma = adv_lemma(word)
        elif tag == "Part":
            lemma = part_lemma(word)
        else:
            lemma = word
        print("{0}\t{1}\t{2}".format(word, tag, lemma))
    else:
        print()


#python3 lemmatizer.py < ewt-dev-wt.txt > ewt-dev-out.txt
#python3 score.py lemma ewt-dev-wtl.txt ewt-dev-out.txt
#vimdiff ewt-dev-wtl.txt ewt-dev-out.txt