"""
    Write a program that writes every second word in a sentence to file,
    using either with open or open. The words should include no punctuation
    marks and be lower case. You should have at least two functions
    (or three if you have a main()). The first function should return a list
    of every second word in its input, a string. The second function should
    take this list as input and write the words separated by newline \n to
    a file. Name the file evey_second.txt

    Here is an example:

sentences = "This, friends, is an example. This is another one. Do you like these short sentences?"   
 
    Hence, if you give this command:

cat every_second.txt

    The output should be:

this
is
example
is
one
you
these
sentences

"""
import string

def clean_text(text):
    text = text.lower()
    text = text.strip()
    text = text.translate(str.maketrans('','',string.punctuation))
    clean_text = text.split()
    return clean_text

def second_word(lst):
    second_word = []
    for i in range(len(lst)):
        if i % 2 == 0:
            second_word.append(lst[i])
    return second_word

def main():
    sentences = "This, friends, is an example. This is another one. Do you like these short sentences?"   
    clean_sentences = clean_text(sentences)
    second = second_word(clean_sentences)
    write_file(second,' every_second.txt')

def write_file(lst,filename):
    with open(filename,'w') as f:
        for word in lst:
            f.write(word + '\n')
            
if __name__ == "__main__":
    main()