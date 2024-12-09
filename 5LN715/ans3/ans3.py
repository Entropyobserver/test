from collections import defaultdict
from nltk import sent_tokenize, word_tokenize
from math import log



class AutoCorrect:

    def __init__(self, word_list,alpha='abcdefghijklmnopqrstuvwxyz'):
        self.word_list = word_list
        self.alpha = alpha

    def insertion(self,word):
    #insert in the beginning："acat", "bcat", "ccat" i=0
    #insert in the middle："caat", "cbat", "ccat" i=1
    #insert in the end:"cata", "catb", "catc" i=3
        for i in range(len(word)+1):
            for char in self.alpha:
                new_word = word[:i] + char + word[i:]
                if new_word in self.word_list:
                    return new_word
                
    def deletion(self,word):
        #delete in the beginning:"at", "bt", "ct" i=0 word[:0] = ""
        #delete in the middle:"ct", "ca", "cb" i=1
        #delete in the end:"ca", "ct", "ct" i=2
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in self.word_list:
                return new_word
            
    def substitution(self,word):
        #substitute in the beginning:"bat", "cat", "dat" i=0
        #substitute in the middle:"cct", "cat", "cct" i=1
        #substitute in the end:"cab", "cat", "cad" i=2
        for i in range(len(word)):
            for char in self.alpha:
                new_word = word[:i] + char + word[i+1:]
                if new_word in self.word_list:
                    return new_word
                
    def swapping(self,word):
        #swap the first two characters:"act"
        #swap the last two characters:"cta"
        for i in range(len(word)-1):
            new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
            if new_word in self.word_list:
                return new_word
            
    def suggest(self,word):
        suggest = set()
        suggest.update(self.insertion(word),self.deletion(word),self.substitution(word),self.swapping(word))
        return suggest
    

    def get_lines(self,path):
        with open(path,'r',encoding='utf-8') as file:
            text = file.read()
            word_list = word_tokenize(text)
        return word_list

    def biagram(self,lines):
        bigram = defaultdict(int)
        for i in range(len(lines)-1):
            bigram[lines[i],lines[i+1]] += 1
        return bigram

    def autocorrect(self,word):
        if word in self.word_list:
            return word
        if self.insertion(word):
            return self.insertion(word)
        if self.deletion(word):
            return self.deletion(word)
        if self.substitution(word):
            return self.substitution(word)
        if self.swapping(word):
            return self.swapping(word)
        return word 
    
word_list = ['cat']
auto = AutoCorrect(word_list)
print(auto.insertion('acat'))
print(auto.deletion('ct'))
print(auto.substitution('bat'))
print(auto.swapping('cta'))