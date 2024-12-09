import nltk
from collections import defaultdict
nltk.download('punkt', quiet=True)

def get_bigram_stats(text):
    # 分句
    sentences = text.split('\n')
    sentences = [s.strip() for s in sentences if s.strip()]

    # 获取所有唯一词
    all_words = set()
    for sentence in sentences:
        words = nltk.word_tokenize(sentence.lower())
        all_words.update(words)

    # 计算bigram
    bigram_dict = defaultdict(int)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence.lower())
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bi_word = (words[i], words[i + 1])
            bigram_dict[bi_word] += 1

    # 计算零频率bigram数量
    zero_bigrams = 0
    for word1 in all_words:
        for word2 in all_words:
            if (word1, word2) not in bigram_dict:
                zero_bigrams += 1

    return {
        'total_unique_words': len(all_words),
        'total_bigrams': len(all_words) * len(all_words),
        'zero_frequency_bigrams': zero_bigrams
    }

# 读取文本
with open('paste.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 分析
result = get_bigram_stats(text)
print(f"总唯一词数: {result['total_unique_words']}")
print(f"总可能bigram数: {result['total_bigrams']}")
print(f"零频率bigram数: {result['zero_frequency_bigrams']}")
print(f"零频率比例: {result['zero_frequency_bigrams'] / result['total_bigrams'] * 100:.2f}%")