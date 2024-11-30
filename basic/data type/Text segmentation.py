import string
def clean_text_translate(text):
    """
    方法一：使用str.maketrans()和translate()方法清理文本
    优点：效率高，适合处理大量文本
    """
    # 创建翻译表，将所有标点符号映射到None
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
"""
def text_segmentation_5(string):
    text = string.split()
    chunk_size = 5
    chunks= []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks
test = "This is a very long text that needs to be processed in smaller parts."
if __name__ == "__main__":
    cleaned_string = clean_text_translate(test)
    print(text_segmentation_5(cleaned_string))
"""
def text_segmentation(string):
    text = string.split()
    chunks= []
    for i in range(0,len(text),3):
        chunk = text[i + 2:i + 3]
        chunks.append(chunk)
    return chunks
test = "This is a very long text that needs to be processed in smaller parts."
if __name__ == "__main__":
    cleaned_string = clean_text_translate(test)
    print(text_segmentation(cleaned_string))

def text_segmentation(string):
    text = string.split()
    chunks= []
    for i in range(0,len(text),-2):
        chunk = text[i + 2:i + 3]
        chunks.append(chunk)
    return chunks
test = "This is a very long text that needs to be processed in smaller parts."
if __name__ == "__main__":
    cleaned_string = clean_text_translate(test)
    print(text_segmentation(cleaned_string))





