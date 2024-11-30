def bigram(str):
    words = str.split()
    bigram_dict = {}
    for i in words:
        big_str = ''.join(words[i],words[i+1])
        bigram_dict.add(big_str)
        if big_str not in bigram_dict:
            bigram_dict[big_str] += 1
        else:
            bigram_dict[big_str] = 1
string = "I am walking and I am talking and I an walking"
#print(bigram(string))

def f3(str):
    words = str.split()
    bigram_dict = {}
    for i in range(len(words) - 1):
        bigram = (words[i],words[i+1])
        #big_str = ''.join(bigram)
        #bigram_dict.add(big_str)
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    return bigram_dict
string = "I am walking and I am talking and I an walking"
print(f3(string))

def get_bigrams_1(text):
    text = text.lower()
    text = text.replace(".","")
    text = text.split()
    bi_dict = {}
    for i in range(len(text)-1):
        bigram = (text[i],text[i+1])
        bi_str = "".join(bigram)
        if bi_str in bi_dict:
            bi_dict[bi_str] += 1
        else:
            bi_dict[bi_str] = 1
    return bi_dict
#print("test for funcation 1 is  running")
#lst1 = " I love the sun. I love the sun and the sun is a star. I love a star."
