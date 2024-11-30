"""

    This is a fairly large exercise. Please put prestige aside and ask for
    help if you need it :D The TAs and me are PAID to help you!

    Write a function get_lines() that takes one parameter. The function
    should open a file, read the lines of that file, close the file, and
    return the lines.

    Write another function get_word_freq() that takes the lines from the
    file as an argument. Create an empty dictionary and add to that dictionary
    the words in the sentences from the lines. To get rid of punctuation marks,
    you can use .strip(".,") and to get only lower case you can use the .lower()
    method. Return the dictionary.

    Write a function main() that takes no parameters. In main(), assign to a
    variable the string sentences.txt, which is a file you can find here and
    that you should copy to some subdirectory under your home directory:

    /common/student/courses/programming-5LN429/lectures/L3/exercises/

    Start by looking at the contents of the file in the Terminal (i.e., not
    in Python). You can have another Terminal window for
    that. What command can you use? Here are some suggestions.

    REMEMBER TO USE TAB TO AUTOCOMPLETE YOUR COMMANDS!

    head -n 10 sentences.txt

    cat sentences.txt

    nl sentences.txt

    Additionally, you can simply open sentences.txt in Vim or Nano and look
    through the content. If you by mistake change the file, copy it again
    from the same place.

    Now, let's get back to the Python code.

    Assign to a variable, let's say you call it lines, a function call
    get_lines() and pass in the a string that is a path to sentences.txt

    You should now loop over that variable and print the loop variable to
    see what's in the file and that everything looks good.
    If you print the loop variable with .split(), you should see this:

['This', 'is', 'a', 'sentence.']

['This', 'is', 'another', 'sentence.']

['Linguists', 'are', 'interested', 'in', 'sentences.']

    Then get rid of the for-loop.

    Next, in the function main() you should assign a variable word_freq to
    a function call of get_word_freq() and pass in lines (or whatever you
    called the variable).

    What data type does word_freq have?

    To turn word_freq into a sorted list, you will do the following. Import
    the operator module. We have not talked much about imports 
    but we will later.
    At the top of your program, before your functions, type:


    import operator


    And then you can use the following on the line after word_freq:

    sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

    where d is your dictionary, and where sorted() returns a list that is
    sorted by the values in the the dictionary. It will be sorted descending,
    starting with the most frequent words. 

    Loop over sorted_d (or whatever you call that variable) and then use
    indexing to print the word and the frequency separated by a comma.

    Once you are done with all of this, you will run the program from the
    Terminal and redirect the output to a file. Here is how you do it:

solution4.py > word_freq.txt

    Use ls to see that the file was created. Inspect word_freq.txt

    You can also see just the first 10 lines of word_freq.txt like this:

    head -n 10 word_freq.csv

    This is the desired output:

language,19
is,11
of,9
the,9
in,8
not,8
for,7
that,7
a,6
this,5
    
"""
def get_lines(path):
    with open(path,'r') as f:
        lines = f.readlines()
    return lines

def get_word_freq(lines):
    word_freq_dict = {}
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            #word = word.strip('.,')
            if word in word_freq_dict:
                word_freq_dict[word] += 1
            else:
                word_freq_dict[word] = 1
    return word_freq_dict
import operator
def main():
    path  = '/common/student/courses/programming-5LN429/lectures/L3/exercises/sentences.txt'
    lines = get_lines(path)
    word_freq = get_word_freq(lines)
    sorted_d = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for word,freq in sorted_d:
        print(f"{word},{freq}")
if __name__ == "__main__":
    main()