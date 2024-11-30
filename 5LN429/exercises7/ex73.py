"""
    Write a function get_word_index() that takes a string as input.
    The string should be made into a list so that each item in the
    list is a word. The function should then return a list of tuples.
    Each tuple will have to items: The word index of the word in the list
    and the word. Use list comprehension and enumerate.

    Test case:

test = "This is not a Kafka quote as far as I know"
print(get_word_index(test))
   
    The output should be:

[(0, 'This'), (1, 'is'), (2, 'not'), (3, 'a'), (4, 'Kafka'), (5, 'quote'), (6, 'as'), (7, 'far'), (8, 'as'), (9, 'I'), (10, 'know')]


def get_word_index(lst):
    new_tuple = set()
    return [new_tuple.add(i) for i in enumerate(lst) ]
test = "This is not a Kafka quote as far as I know"
print(get_word_index(test))

def get_word_index(lst):
    words = lst.split()
    return [(index,word) for index,word in enumerate(words)]
test = "This is not a Kafka quote as far as I know"
print(get_word_index(test))


def get_word_index(lst):
    words = lst.split()
    new_lst = []
    for word in lst:
        for i in len(lst):
            new_lst(i,word)
    return new_lst
test = "This is not a Kafka quote as far as I know"
print(get_word_index(test))

"""
def get_word_index(s):
    words = s.split()
    new_lst = []
    for i in range(len(words)):
        new_lst.append((i, words[i]))
    return new_lst

test = "This is not a Kafka quote as far as I know"
print(get_word_index(test))

