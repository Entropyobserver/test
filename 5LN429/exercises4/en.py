def preprocess_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # 示例预处理步骤：转换为小写
    text = text.lower()
    # 其他预处理步骤...
    return text

processed_text = preprocess_text('UNv1.0.testset.en')
print(processed_text[:100])
print(len(processed_text))