from collections import defaultdict
import string

def get_bigrams_3(text):
    print(f"原始文本: '{text}'")
    
    print("\n步骤1: 转换为小写")
    text = text.lower()
    print(f"转换后: '{text}'")
    
    print("\n步骤2: 移除标点符号")
    text = text.translate(str.maketrans('','',string.punctuation))
    print(f"移除标点后: '{text}'")
    
    print("\n步骤3: 分割成单词列表")
    text = text.split()
    print(f"单词列表: {text}")
    
    print("\n步骤4: 创建bigram字典")
    bigram_dict = defaultdict(list)
    
    print("\n步骤5: 遍历单词列表，创建bigrams")
    for i in range(len(text) - 1):
        bigram = (text[i], text[i+1])
        bistr = "".join(bigram)
        print(f"  处理bigram: {bigram}, 连接后: '{bistr}'")
        
        if bistr in bigram_dict:
            bigram_dict[bistr] += 1
            print(f"    '{bistr}' 已存在，计数增加到 {bigram_dict[bistr]}")
        else:
            bigram_dict[bistr] = 1
            print(f"    '{bistr}' 是新的bigram，计数设为 1")
    
    print("\n最终的bigram字典:")
    return dict(bigram_dict)  # 转换为普通字典以便打印

print("test for function 3 is running")
lst1 = " I love the sun. I love the sun and the sun is a star. I love a star."
result = get_bigrams_3(lst1)
print(result)