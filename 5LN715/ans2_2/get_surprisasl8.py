import nltk
from nltk import word_tokenize
from math import log
import csv
import json

# 下载NLTK资源
nltk.download('punkt', quiet=True)

def get_lines(file_path):
    """
    从文件中读取所有行
    
    :param file_path: 输入文件路径
    :return: 文件行列表
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_unigrams(lines):
    """
    从输入行生成一元语法（单词）频率字典
    
    :param lines: 输入字符串列表
    :return: 单词及其频率的字典
    """
    unigram_counts = {}
    for line in lines:
        # 分词并转换为小写
        words = word_tokenize(line.strip().lower())
        # 添加句子开始和结束标记
        words = ['<s>'] + words + ['<e>']
        for word in words:
            word = word.strip()
            unigram_counts[word] = unigram_counts.get(word, 0) + 1
    return unigram_counts

def get_bigrams(lines):
    """
    从输入行生成二元语法（词对）频率字典
    
    :param lines: 输入字符串列表
    :return: 词对及其频率的字典
    """
    bigram_counts = {}
    for line in lines:
        # 分词并转换为小写
        words = word_tokenize(line.strip().lower())
        # 添加句子开始和结束标记
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            first_word = words[i].strip()
            second_word = words[i + 1].strip()
            bigram = (first_word, second_word)
            bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts

def get_surprisal(probability):
    """
    根据概率计算惊讶度（-log2(p)）
    
    :param probability: 概率值
    :return: 惊讶度值
    """
    return -log(probability, 2)

def get_test_surprisal(sentence, unigram_dict, bigram_dict, durations):
    """
    计算测试句子的平均惊讶度
    
    :param sentence: 输入句子
    :param unigram_dict: 训练数据的一元语法词典
    :param bigram_dict: 训练数据的二元语法词典
    :param durations: 单词持续时间的字典
    :return: 句子的平均惊讶度，以及每个单词的惊讶度和持续时间
    """
    V = len(unigram_dict)  # 词汇表大小
    words = word_tokenize(sentence.strip().lower())
    words = ['<s>'] + words + ['<e>']
    
    total_surprisal = 0
    word_count = 0
    word_results = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1].strip()
        current_word = words[i].strip()
        
        # 获取前一个词的一元语法计数
        unigram_count = unigram_dict.get(prev_word, 0)
        
        # 获取前一个词和当前词的二元语法计数
        bigram_count = bigram_dict.get((prev_word, current_word), 0)
        
        # 使用拉普拉斯平滑估计概率
        unigram_count_smooth = unigram_count + V
        bigram_count_smooth = bigram_count + 1
        
        # 使用拉普拉斯平滑计算条件概率
        if unigram_count == 0:
            cond_p = 1 / V
        else:
            cond_p = bigram_count_smooth / unigram_count_smooth
        
        # 计算惊讶度
        word_surprisal = get_surprisal(cond_p)
        
        # 获取单词持续时间
        duration = durations.get(current_word, 0)
        
        # 记录单词级别的详细信息
        word_results.append((current_word, duration, word_surprisal))
        
        total_surprisal += word_surprisal
        word_count += 1
    
    # 返回平均惊讶度和单词级别结果
    avg_surprisal = total_surprisal / word_count if word_count > 0 else 0
    return avg_surprisal, word_results

def main():
    """
    主函数，处理文本并计算惊讶度
    """
    # 输入文件路径（请根据实际情况修改）
    training_path = r'D:\J\Desktop\language technology\course\ans2 copy\wiki.train.raw'  # 训练数据路径
    test_path = r'D:\J\Desktop\language technology\course\ans2 copy\sentence_1.txt'  # 测试句子路径
    
    # 读取训练数据
    training_lines = get_lines(training_path)
    
    # 获取一元和二元语法频率
    unigram_dict = get_unigrams(training_lines)
    bigram_dict = get_bigrams(training_lines)
    
    # 读取测试句子
    test_sentences = get_lines(test_path)
    
    # 加载单词持续时间（可选）
    try:
        with open('D:\\J\\Desktop\\language technology\\course\\ans2 copy\\durations.json', 'r') as f:
            durations = json.load(f)
    except FileNotFoundError:
        print("持续时间文件未找到，将使用默认持续时间0")
        durations = {}
    
    # 处理每个测试句子
    sentence_results = []
    all_word_results = []
    
    for sentence in test_sentences:
        # 计算句子的平均惊讶度和单词级别结果
        avg_surprisal, word_results = get_test_surprisal(sentence, unigram_dict, bigram_dict, durations)
        
        # 记录句子结果
        sentence_results.append((sentence.strip(), avg_surprisal))
        all_word_results.extend(word_results)
        
        # 打印结果
        print(f"句子: {sentence.strip()}")
        print(f"平均惊讶度: {avg_surprisal}\n")
        
        print("单词结果:")
        for word, duration, surprisal in word_results:
            print(f"单词: {word}, 持续时间: {duration}, 惊讶度: {surprisal}")
        print("-" * 50)
    
    # 将结果写入CSV文件
    with open('output_sentences1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        sentence_writer = csv.writer(csvfile)
        sentence_writer.writerow(['Sentence', 'Average Surprisal'])
        sentence_writer.writerows(sentence_results)
    
    with open('output_words1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        word_writer = csv.writer(csvfile)
        word_writer.writerow(['Word', 'Duration', 'Surprisal'])
        word_writer.writerows(all_word_results)

if __name__ == "__main__":
    main()



