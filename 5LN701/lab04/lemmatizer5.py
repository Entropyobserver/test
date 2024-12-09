import sys

def lemmatize_noun(word):
    word = word.lower()  # 转为小写，确保一致性

    # 不规则复数词库
    irregular_nouns = {
        "children": "child",
        "mice": "mouse",
        "geese": "goose",
        "teeth": "tooth",
        "feet": "foot",
        "sheep": "sheep",
        "deer": "deer",
        "fish": "fish",
        "cacti": "cactus",
        "nuclei": "nucleus",
        "algae": "alga",
        "antennae": "antenna"
    }

    # 检查不规则复数
    if word in irregular_nouns:
        return irregular_nouns[word]

    # 处理 -ies 结尾的单词
    if word.endswith("ies"):
        # 示例：berries → berry, studies → study
        return word[:-3] + "y"

    # 处理 -ves 结尾的单词
    if word.endswith("ves"):
        # 示例：wolves → wolf, knives → knife
        if word[-4] in 'aeiou':  # 判断前一位是否为元音
            return word[:-3] + "fe"
        return word[:-3] + "f"

    # 处理 -oes 结尾的单词
    if word.endswith("oes"):
        # 示例：heroes → hero, potatoes → potato
        return word[:-2]

    # 处理 -es 结尾的单词
    if word.endswith("es"):
        # 示例：buses → bus, boxes → box
        return word[:-2]

    # 处理 -s 结尾的单词
    if word.endswith("s"):
        # 示例：cats → cat, dogs → dog
        return word[:-1]

    # 默认返回原始单词（用于单复数相同的情况）
    return word

def verb_lemma(word):
    word = word.lower()  # 转为小写，确保一致性
    
    # 不规则动词词库
    irregular_verbs = {
        'went': 'go', 
        'ran': 'run', 
        'saw': 'see', 
        'spoke': 'speak', 
        'took': 'take',
        'came': 'come',
        'found': 'find',
        'told': 'tell',
        'done': 'do',
        'been': 'be',
        'began': 'begin',
        'begun': 'begin',
        'drank': 'drink',
        'drunk': 'drink',
        'ate': 'eat',
        'eaten': 'eat',
        'gave': 'give',
        'given': 'give'
    }
    
    # 检查是否为不规则动词
    if word in irregular_verbs:
        return irregular_verbs[word]
    
    # 处理规则动词形式
    if word.endswith("ed"):
        # 以 -ied 结尾的动词 (e.g., "cried" → "cry")
        if word.endswith("ied"):
            return word[:-3] + "y"
        # 双写辅音后缀 (e.g., "stopped" → "stop")
        if len(word) > 3 and word[-3] == word[-4]:
            return word[:-3]
        # 普通过去式 (e.g., "played" → "play")
        return word[:-2]
    
    elif word.endswith("ing"):
        # 以 -ing 结尾的动词
        # 特殊情况：去掉 -ing 后需要恢复原始动词 (e.g., "hopping" → "hop")
        if len(word) > 4 and word[-4] == word[-5]:
            return word[:-4]
        # 普通现在分词 (e.g., "eating" → "eat")
        if word[-4:-3] not in 'aeiou':
            return word[:-3] + "e"
        return word[:-3]
    
    elif word.endswith("es"):
        # 特殊规则：第三人称单数形式 (e.g., "watches" → "watch")
        if word.endswith("ies"):  # 以 -ies 结尾的动词 (e.g., "cries" → "cry")
            return word[:-3] + "y"
        return word[:-2]
    
    # 处理常见助动词或状态动词变化
    if word in ['is', 'am', 'was', 'were', 'are', "'s"]:
        return "be"
    elif word in ['has', 'had']:
        return "have"
    elif word in ['does', 'did']:
        return "do"
    
    # 默认返回原始单词
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