from nltk import sent_tokenize, word_tokenize
def get_token(path):
    with open(path,'r',encoding='utf-8') as file:
        text = file.read()
        token = word_tokenize(text)
    return token
def main():
    path1 = r"D:\J\Desktop\language technology\course\5LN715\ans3\usenglish-utf8.txt"
    path2 = r"D:\J\Desktop\language technology\course\5LN715\ans3\UNv1.0.testset.en"
    text = get_token(path1)
    token = get_token(path2)
    #print(text[:100])
    print(token[:100])
main()