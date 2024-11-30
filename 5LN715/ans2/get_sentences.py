import os
import re
import random
from nltk import sent_tokenize, word_tokenize

def get_lines(path):
    """
    Args:
        path (str)
    Returns:
        str: content
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.read()
        return lines

    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return ""

    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def get_sentences(train_sentences, num_sentences=20, min_length=15, max_length=50):
    """
    从句子列表中随机选择符合条件的句子
    
    Args:
        train_sentences (list): 原始句子列表
        num_sentences (int): 要选择的句子数量
        min_length (int): 句子最小单词数
        max_length (int): 句子最大单词数
    
    Returns:
        list: 处理后的句子列表
    """
    try:
        # 随机抽样
        random_sentences = random.sample(train_sentences, min(num_sentences, len(train_sentences)))
        
        # 句子过滤和处理
        selected_sentences = []
        for i, sentence in enumerate(random_sentences):
            # 移除标点
            sentence = re.sub(r'[^\w\s]', '', sentence) 
            # 分词并检查长度
            words = sentence.split()
            if min_length <= len(words) <= max_length:
                sentence = ' '.join(words).lower().strip()
                selected_sentences.append(sentence)
                print(f"Random sentence {i + 1}: {sentence}")
        
        return selected_sentences
    
    except Exception as e:
        print(f"Error selecting sentences: {e}")
        return []

def save_sentences(sentences, output_dir='output'):
    """
    将句子保存到文件
    
    Args:
        sentences (list): 要保存的句子列表
        output_dir (str): 输出目录
    """
    try:
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存句子
        for i, sentence in enumerate(sentences, 1):
            file_path = os.path.join(output_dir, f"sentence_{i}.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(sentence)
            print(f"Sentence {i} saved to {file_path}")
    
    except Exception as e:
        print(f"Error saving sentences: {e}")

def main():
    """
    主程序入口
    """
    # 文件路径
    path = '/home/yaxi4987/5LN715/ans2/wiki.train.raw'
    
    # 读取文件内容
    train_text = get_lines(path)
    
    if not train_text:
        print("No text to process.")
        return
    
    # 分句
    train_sentences = sent_tokenize(train_text)
    
    # 选择句子
    selected_sentences = get_sentences(train_sentences)
    
    # 打印选中的句子
    print("\nSelected Sentences:")
    for sentence in selected_sentences:
        print(sentence)
    
    # 保存句子
    save_sentences(selected_sentences)

if __name__ == "__main__":
    main()