


# 导入所需的库
from collections import Counter, defaultdict
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# 示例文本
text = """The quick brown fox jumps over the lazy dog. 
          The fox is quick and brown, and the dog is lazy.
          The quick fox jumps again."""

print("原始文本：")
print(text)
print("\n" + "="*50 + "\n")

print("1. 使用for循环和字典：")
# 预处理文本
words = text.lower().split()
print("分词结果：", words)

# 使用普通字典
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("词频统计结果：")
for word, freq in sorted(word_freq.items()):
    print(f"'{word}': {freq}")
print("\n" + "="*50 + "\n")

print("2. 使用collections.Counter：")
# 直接使用Counter
counter_freq = Counter(words)
print("Counter对象：", counter_freq)
print("\n最常见的3个词：", counter_freq.most_common(3))
print("\n" + "="*50 + "\n")

print("3. 使用defaultdict：")
# 使用defaultdict
default_freq = defaultdict(int)
for word in words:
    default_freq[word] += 1

print("defaultdict对象：", dict(default_freq))
print("\n按频率排序：")
sorted_freq = sorted(default_freq.items(), key=lambda x: x[1], reverse=True)
for word, freq in sorted_freq:
    print(f"'{word}': {freq}")
print("\n" + "="*50 + "\n")

print("4. 使用pandas DataFrame：")
# 创建DataFrame
df = pd.DataFrame(words, columns=['word'])
print("DataFrame头部：")
print(df.head())
print("\n词频统计：")
word_counts = df['word'].value_counts()
print(word_counts)
print("\n" + "="*50 + "\n")

print("5. 使用正则表达式：")
# 使用正则表达式清理文本
cleaned_words = re.findall(r'\b\w+\b', text.lower())
print("清理后的词列表：", cleaned_words)
regex_freq = Counter(cleaned_words)
print("\n词频统计：")
for word, freq in regex_freq.most_common():
    print(f"'{word}': {freq}")
print("\n" + "="*50 + "\n")

print("9. 使用numpy统计：")
# 使用numpy的unique函数
words_array = np.array(words)
unique_words, counts = np.unique(words_array, return_counts=True)
print("唯一词列表：", unique_words)
print("对应频数：", counts)
print("\n合并结果：")
np_freq = dict(zip(unique_words, counts))
for word, freq in sorted(np_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"'{word}': {freq}")
print("\n" + "="*50 + "\n")

print("10. 使用TfidfVectorizer：")
# 使用TfidfVectorizer
vectorizer = TfidfVectorizer(use_idf=False, norm=None)
X = vectorizer.fit_transform([text])
feature_names = vectorizer.get_feature_names_out()
frequencies = X.toarray().sum(axis=0)

print("特征词列表：", feature_names)
print("对应频数：", frequencies)
print("\n合并结果：")
tfidf_freq = dict(zip(feature_names, frequencies))
for word, freq in sorted(tfidf_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"'{word}': {freq}")

print("\n" + "="*50 + "\n")

print("各方法比较：")
print("\n1. 普通字典方法：")
print("- 优点：直观，易于理解")
print("- 缺点：需要手动处理键的存在性检查")

print("\n2. Counter方法：")
print("- 优点：简洁，自带most_common()等实用方法")
print("- 缺点：无")

print("\n3. defaultdict方法：")
print("- 优点：无需键检查，代码更简洁")
print("- 缺点：打印时可能显示defaultdict对象信息")

print("\n4. pandas方法：")
print("- 优点：强大的数据分析功能")
print("- 缺点：对简单任务可能过于重量级")

print("\n5. 正则表达式方法：")
print("- 优点：可以处理复杂的文本清理")
print("- 缺点：正则表达式编写可能较复杂")

print("\n9. numpy方法：")
print("- 优点：高效的数组操作")
print("- 缺点：主要用于数值计算，文本处理不是其强项")

print("\n10. TfidfVectorizer方法：")
print("- 优点：适合文档集的分析，可扩展到TF-IDF计算")
print("- 缺点：对单个文本的简单词频统计可能过于复杂")