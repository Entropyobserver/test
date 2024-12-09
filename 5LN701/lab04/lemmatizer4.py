import sys

def noun_lemma(word):
    word = word.lower()
    # 处理更多不规则名词复数
    irregular_nouns = {
        'children': 'child', 
        'feet': 'foot', 
        'teeth': 'tooth', 
        'men': 'man', 
        'women': 'woman',
        'mice': 'mouse',
        'geese': 'goose'
    }
    if word in irregular_nouns:
        return irregular_nouns[word]
    
    if word.endswith("s"):
        # 特殊处理
        if word.endswith("ies") and len(word) > 3:
            return word[:-3] + "y"
        elif word.endswith("es") and len(word) > 2:
            # 处理 "churches" → "church" 等情况
            return word[:-2] if not word.endswith("sses") else word
        return word[:-1]
    return word

def verb_lemma(word):
    word = word.lower()
    # 扩展不规则动词列表
    irregular_verbs = {
        'went': 'go', 
        'ran': 'run', 
        'saw': 'see', 
        'spoke': 'speak', 
        'took': 'take',
        'came': 'come',
        'found': 'find',
        'told': 'tell'
    }
    
    if word in irregular_verbs:
        return irregular_verbs[word]
    
    if word.endswith("ed"):
        # 处理特殊情况，如 "stopped" → "stop"
        if word.endswith("ied"):
            return word[:-3] + "y"
        return word[:-2]
    elif word.endswith("ing"):
        # 处理特殊情况 
        if len(word) > 4 and word[-4:-3] not in 'aeiou':
            return word[:-3] + "e"
        return word[:-3]
    elif word.endswith('es'):
        return word[:-2]
    
    # 扩展常见动词变化
    if word in ['is','am','was','were','are',"'s"]:
        return "be"
    elif word in ['has','had']:
        return "have"
    
    return word

def adj_lemma(word):
    word = word.lower()
    # 处理更多不规则形容词
    irregular_adjs = {
        'worse': 'bad', 
        'better': 'good',
        'best': 'good',
        'worst': 'bad'
    }
    
    if word in irregular_adjs:
        return irregular_adjs[word]
    
    if word.endswith("er"):
        # 处理特殊情况，如 "happier" → "happy"
        if word.endswith("ier"):
            return word[:-3] + "y"
        return word[:-2]
    elif word.endswith("est"):
        # 处理特殊情况
        if word.endswith("iest"):
            return word[:-4] + "y"
        return word[:-3]
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

# 其他函数保持不变

# 主处理逻辑
for line in sys.stdin:
    if line.strip():
        try:
            (word, tag) = line.strip().split("\t")
            lemma = word
            
            # 统一处理逻辑
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
            
            # 其他词性处理保持不变
            
            print("{0}\t{1}\t{2}".format(word, tag, lemma))
        except ValueError:
            # 处理可能的输入错误
            print(f"Error processing line: {line.strip()}")
    else:
        print()
#python3 lemmatizer4.py < ewt-dev-wt.txt > ewt-dev-out.txt
#python3 score.py lemma ewt-dev-wtl.txt ewt-dev-out.txt
#vimdiff ewt-dev-wtl.txt ewt-dev-out.txt