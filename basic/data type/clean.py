import string
import re

def clean_text_translate(text):
    """
    方法一：使用str.maketrans()和translate()方法清理文本
    优点：效率高，适合处理大量文本
    """
    # 创建翻译表，将所有标点符号映射到None
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def clean_text_regex(text):
    """
    方法二：使用正则表达式清理文本
    优点：灵活性强，可以自定义匹配模式
    """
    # \w: 匹配字母、数字、下划线
    # \s: 匹配空白字符
    # [^\w\s]: 匹配除了字母、数字、下划线和空白字符之外的所有字符
    return re.sub(r'[^\w\s]', '', text)

def clean_text_loop(text):
    """
    方法三：使用循环和条件判断清理文本
    优点：逻辑清晰，容易理解和修改
    """
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return ''.join(char for char in text if char not in punctuations)

def clean_text_replace(text):
    """
    方法四：使用str.replace()方法清理文本
    优点：代码简单，直观
    """
    cleaned_text = text
    for char in string.punctuation:
        cleaned_text = cleaned_text.replace(char, '')
    return cleaned_text

def test_cleaning_functions():
    """
    测试所有清理函数
    """
    # 测试用例
    test_texts = [
        "Hello, World!",
        "This is a test... with some punctuation!!!",
        "Email: test@example.com, Phone: (123) 456-7890",
        "Multiple    spaces    and...    dots!",
        ""  # 空字符串测试
    ]
    
    # 测试每个函数
    for i, text in enumerate(test_texts, 1):
        print(f"\n测试用例 {i}: {text}")
        print("-" * 50)
        print(f"方法一 (translate): {clean_text_translate(text)}")
        print(f"方法二 (regex):     {clean_text_regex(text)}")
        print(f"方法三 (loop):      {clean_text_loop(text)}")
        print(f"方法四 (replace):   {clean_text_replace(text)}")
        print("=" * 50)

if __name__ == "__main__":
    test_cleaning_functions()