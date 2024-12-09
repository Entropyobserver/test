class AutoCorrect:
    def __init__(self, word_list, alpha='abcdefghijklmnopqrstuvwxyz'):
        self.word_list = set(word_list)
        self.alpha = alpha
    
    def insertion(self, word):
        insertions = []
        for i in range(len(word) + 1):
            for char in self.alpha:
                new_word = word[:i] + char + word[i:]
                insertions.append(new_word)
        return insertions or []  # 确保始终返回列表
    
    def deletion(self, word):
        deletions = []
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            deletions.append(new_word)
        return deletions or []  # 确保始终返回列表
    
    def substitution(self, word):
        substitutions = []
        for i in range(len(word)):
            for char in self.alpha:
                new_word = word[:i] + char + word[i+1:]
                substitutions.append(new_word)
        return substitutions or []  # 确保始终返回列表
    
    def swapping(self, word):
        swaps = []
        for i in range(len(word) - 1):
            new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
            swaps.append(new_word)
        return swaps or []  # 确保始终返回列表
    
    def suggest(self, word):
        suggest = set()
        suggest.update(
            self.insertion(word)|
            self.deletion(word)|
            self.substitution(word)|
            self.swapping(word)
        )
        return suggest
    

    