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
        insertion = []
        for i in range(len(word)+1):
            for char in self.alpha:
                new_word = word[:i] + char + word[i:]
                if new_word in self.word_list:
                    insertion.append(new_word)
        return insertion
                
    def deletion(self,word):
        #delete in the beginning:"at", "bt", "ct" i=0 word[:0] = ""
        #delete in the middle:"ct", "ca", "cb" i=1
        #delete in the end:"ca", "ct", "ct" i=2
        deletion = []
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in self.word_list:
                deletion.append(new_word)
        return deletion
            
    def substitution(self,word):
        #substitute in the beginning:"bat", "cat", "dat" i=0
        #substitute in the middle:"cct", "cat", "cct" i=1
        #substitute in the end:"cab", "cat", "cad" i=2
        substitution = []
        for i in range(len(word)):
            for char in self.alpha:
                new_word = word[:i] + char + word[i+1:]
                if new_word in self.word_list:
                    substitution.append(new_word)
        return substitution
                
    def swapping(self,word):
        #swap the first two characters:"act"
        #swap the last two characters:"cta"
        swapping = []
        for i in range(len(word)-1):
            new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
            if new_word in self.word_list:
                swapping.append(new_word)
        return swapping
            
    def suggest(self, word):
        methods = [
        self.insertion, 
        self.deletion, 
        self.substitution, 
        self.swapping
        ]
    
        suggestions = set()
        for method in methods:
            result = method(word)
            if result:
                suggestions.update(result)

        result = []
        for suggestion in suggestions:
            if suggestion in self.word_list:
                result.append(suggestion)
        return result


    def get_lexion(self,path1):
        lexion = set()
        with open(path1,'r',encoding='utf-8') as file:
            for word in file:
                lexion.add(word.strip())
        return lexion

    def biagram_frequnency(self,path2):
        bigram_freq = defaultdict(int)
        with open(path2,'r',encoding='utf-8') as file:
            text = file.read()
            lines = word_tokenize(text)
        for i in range(len(lines)-1):
            bigram_freq[lines[i],lines[i+1]] += 1
        return bigram_freq

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
"""
word_list = ['cat','bat','act','cta','at']
auto = AutoCorrect(word_list)
print(auto.insertion('acat'))#because 'acat' is not in the word_list
print(auto.deletion('ct'))#because 'ct' is not in the word_list
print(auto.substitution('bat'))
print(auto.swapping('cta'))
print(auto.suggest('at'))
"""
