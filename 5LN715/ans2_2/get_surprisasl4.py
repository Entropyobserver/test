from nltk import sent_tokenize, word_tokenize
from math import log
from get_duration import get_duration
import csv

# 读取文件内容
def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

# 构建 unigram 词频表
def build_unigram_counts(sentences):
    unigram_counts = {}
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        words = ['<s>'] + words + ['<e>']
        for word in words:
            unigram_counts[word] = unigram_counts.get(word, 0) + 1
    return unigram_counts

# 构建 bigram 词频表
def build_bigram_counts(sentences):
    bigram_counts = {}
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bigram = (words[i], words[i + 1])
            bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts

# 计算惊奇值
def calculate_surprisal(probability):
    return -log(probability, 2)

# 根据 unigram 和 bigram 词频表计算某个单词的惊奇值
def get_bigram_surprisal(unigram_dict,bigram_dict):
    bi_sur_dict = {}
    for bi_word in bigram_dict:
        first_word,second_word = bi_word
        unigram_count = unigram_dict.get(first_word,0)
        bigram_count = bigram_dict.get(bi_word,0) 
        #unigram_count_smooth = unigram_count + len(bigram_dict)
        unigram_count_smooth = unigram_count + 1
        bigram_count_smooth = bigram_count + 1
        cond_p = bigram_count_smooth / unigram_count_smooth
        s = -log(cond_p,2)
        bi_sur_dict[bi_word] = s
    return bi_sur_dict

# 为句子中的每个单词计算惊奇值和持续时间
def calculate_surprisal_with_duration(sentence,word_surprise,durations):
    words = word_tokenize(sentence.lower())
    results = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1]
        current_word = words[i]
        
        duration = durations.get(current_word, 0)  # 获取持续时间
        surprisal = calculate_word_surprisal(current_word, prev_word, unigram_counts, bigram_counts)  # 计算惊奇值
        
        results.append((current_word, duration, surprisal))  # 保存结果
    
    return results

# 主函数
if __name__ == "__main__":
    # 读取训练数据
    #path = '/home/yaxi4987/5LN715/ans2/wiki.train.raw'
    path = r'D:\J\Desktop\language technology\s\5LN715\ans2\wiki.train.raw'
    training_data = read_file(path)
    training_sentences = sent_tokenize(training_data)

    # 构建 unigram 和 bigram 词频表
    unigram_counts = build_unigram_counts(training_sentences)
    bigram_counts = build_bigram_counts(training_sentences)

    # 测试句子
    #file_path = '/home/yaxi4987/5LN715/ans2/merged.txt' 
    file_path = r'D:\J\Desktop\language technology\s\5LN715\ans2\merged.txt'
    test_sentence = read_file(file_path)
    #test_sentence = "Norman settlements were characterised by the establishment of baronies , manors , towns and the seeds of the modern county system ."
    
    # 持续时间字典
    durations = jason.dump(/home/yaxi4987/5LN715/ans2/durations.json)
  
    
   
    # 计算测试句子的每个单词的惊奇值和持续时间
    results = calculate_surprisal_with_duration(test_sentence, unigram_counts, bigram_counts, durations)
    
    # 打印结果
    #for word, duration, surprisal in results:
    #    print(f"Word: {word}, Duration: {duration:.4f}, Surprisal: {surprisal:.4f}")
    #print(results)
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Duration', 'Surprisal'])
        writer.writerows(results)
