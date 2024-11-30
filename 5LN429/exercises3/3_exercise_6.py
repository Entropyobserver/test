"""

    You will write a vocuabulary quiz, using a file with English-Swedish
    word pairs. Use the file eng_swe.txt. It can be found in the
    same directory as the exercises. While testing your program, it is smart
    to create a shorter version of eng_swe.txt, which can be done in the
    command line by using head. The command head takes a file as an argument
    and prints the first 10 lines by default. If you want more or fewer than
    10 lines, you can specify it with that is called a flag. For example,
    to get the first three lines of a file, you can use:

head -n 3 some_file.txt

    The command is head, the -n is the flag, the 3 is an argument to the 
    flat, and some_file.txt is the argument to the command.

    The command line prints things by default, but you can re-direct the
    output to a file using the larger-than-symbol > and then give a file
    name. Be sure to use a file name that you do not already have because
    otherwise you risk overwriting an existing file.

head -5 eng_swe.txt > short_eng_swe.txt

    In other words, to get the three first lines of eng_swe.txt, you can do:

head -n 3 eng_swe.txt > eng_swe_3.txt

    Back to the Python exercise.

    Implement three functions:

    get_lines()
    prompt_user()
    main()

    In get_lines(), pass in one argument, a path to a file. Open
    the file using open or with open and return a variable calling
    the .readlines() method. (Remember to close the file if you are
    using open; this is not necessary when using with open.)

    In prompt_user(), pass in the lines from the file. Prompt the
    user to answer what an English word is in Swedish. Return an
    int that corresponds to the number of correct answers, and
    a list with the incorrect answers. In other words, you will return
    a tuple with two items, an integer and a list.

    In main(), call upp the other functions with variable assignment.
    Print the user's score.
    Print the score in percentage.
    Print the words that need to be practiced.

"""
def get_lines(path):
    with open(path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        return lines
        
def prompt_user(lines):
    incorrect_words = []
    correct_count = 0
    for i,line in enumerate(lines):
        english_word,swedish_word = line.strip().split(',')
        answer = input(f"what is the swedish translation of'{english_word}'?")
        if answer.lower() == swedish_word.lower():
            correct_count += 1
        else:
            incorrect_words.append((english_word,swedish_word))
            return (correct_count,incorrect_words) 
    
def main():
    lines = get_lines('/home/yaxi4987/exercises3/eng_swe.txt')
    correct_count,incorrect_words = prompt_user(lines)
    print("your score is",correct_count)
    print("score percentage",correct_count/len(lines))
    for english_word,swedish_word in incorrect_words:
        print(f"{english_word} - {swedish_word}")

if __name__ == "__main__":
    main()