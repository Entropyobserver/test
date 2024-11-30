def get_next_word(s):
    words = s.split()
    next_words = []
    for i in range(len(words)-1):
        next_words.append((words[i],words[i+1]))
    return next_words

chomsky = "Hi how are you"

#chomsky = 'If we do not believe in freedom of expression for people we despise we do not believe in it at all'

print(get_next_word(chomsky))
