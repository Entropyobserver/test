import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# 下载必要的 NLTK 资源
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

# 初始化 Lemmatizer
lemmatizer = WordNetLemmatizer()

# NLTK 词性标签到 WordNet 词性的映射
def get_wordnet_pos(treebank_tag):
    """
    将 NLTK 词性标签映射到 WordNet 词性
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # 默认为名词

def comprehensive_lemmatize(word, tag):
    """
    根据词性进行更精确的词形还原
    """
    # 特殊处理的不规则词
    irregular_words = {
        # 动词
        'is': 'be', 'are': 'be', 'was': 'be', 'were': 'be', 
        'has': 'have', 'had': 'have', 
        'does': 'do', 'did': 'do',
        # 代词
        'him': 'he', 'her': 'she', 'them': 'they',
        # 其他
        "n't": 'not'
    }

    # 检查不规则词
    if word.lower() in irregular_words:
        return irregular_words[word.lower()]

    # 使用 WordNet lemmatizer 进行词形还原
    wordnet_pos = get_wordnet_pos(tag)
    return lemmatizer.lemmatize(word.lower(), pos=wordnet_pos)

def lemmatize_text(text):
    """
    对整个文本进行词形还原
    """
    # 分词和词性标注
    words = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(words)

    # 词形还原
    lemmatized_words = [
        comprehensive_lemmatize(word, tag) 
        for word, tag in tagged_words
    ]

    return lemmatized_words

# 测试示例
test_sentences = [
    "The cats are running quickly to their homes.",
    "He has studied better than her.",
    "I went to the store and bought some apples.",
    "They were happily dancing in the rain."
]

print("词形还原结果：")
for sentence in test_sentences:
    print(f"\n原句: {sentence}")
    print("还原后: ", " ".join(lemmatize_text(sentence)))