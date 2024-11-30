COLOR_RESET = "\033[0m"        # Reset color
COLOR_GREEN = "\033[92m"       # Green color for correct answers
COLOR_RED = "\033[91m"         # Red color for incorrect answers
COLOR_YELLOW = "\033[93m"      # Yellow for instructions or prompts


import sys
def read_file(path):
    try:
        with open(path,'r',) as f:
            words = f.readlines()
        return words
    except FileNotFoundError:
        print(f"File at {path} not found")
        sys.exit(1)

#path = '/home/yaxi4987/assignment_4/verb.csv'
#print(read_file(path))
#words = read_file(path)
#print(len(words))
#print(words)


def translate_dict(words):
    translate_dict = {}
    for word in words:
        try:
            english_word,swedish_word = word.strip().split(",")
            translate_dict[english_word] = swedish_word
        except ValueError:
            print("File must contain words separated by comma")
    return translate_dict
#print(translate_dict(read_file(path)))


import sys
import random
"""
def word_test(test_dict):
    incorrect_lst = []
    correct_lst = []
    english_words = list(test_dict.keys())
    for english_word in english_words:
        swedish_word = test_dict[english_word]
        user_answer = input(f"please enter swedish translation for '{english_word}':")
        if user_answer.lower() == swedish_word.lower():
            correct_lst.append(english_word)
            print(f"{COLOR_GREEN}correct!")
        else:
            incorrect_lst.append(english_word)
            print(f"{COLOR_RED}Incorrect.The correct answer is'{swedish_word}'.")
    print(f"\nResults: {len(correct_lst)} correct, {len(incorrect_lst)} incorrect.")
"""
def word_test(test_dict):
    incorrect = 0
    correct = 0
    total = 0
    while True:
        english_word = random.chioce(list(test_dict.keys()))
        #for enlgish_word in english_words:
        swedish_word = test_dict[english_word]
        answer = input(f"please enter swedish word for '{english_word}':")
        if answer.lower() == swedish_word.lower():
            correct += 1
            print(f"{COLOR_GREEN}correct!")
        else:
            print(f"Incorrect!The correct answer is '{swedish_word}'.")
            incorrect += 1
        total += 1
        retry = input("Do you want to try again? y/n").lower()
        if retry != "y":
            break
    print(f"You got {correct} words right and {total} words in total")
"""
def word_test(test_dict):
    incorrect = 0
    correct = 0
    total = 0
    while True:
        english_word = random.chioce(list(test_dict.keys()))
        #for enlgish_word in english_words:
            swedish_word = test_dict[enlgish_word]
            answer = input("please enter swedish word for '{english_word}':")
            if answer.lower() == swedish_word.lower():
                correct += 1
                print(f"{COLOR_GREEN}correct!")
            else:
                print(f"Incorrect!The correct answer is '{swedish_word}'.")
                incorrect += 1
            total += 1
            retry = input("Do you want to try again? y/n").lower()
            if retry != "y":
                break
        print(f"You got {correct} words right and {total} words in total")

"""
def main():
    path = sys.argv[1]
    #path = '/home/yaxi4987/assignment_4/verb.csv'
    words = read_file(path)
    test_dict = translate_dict(words) 
    word_test = word_test(test_dict)

if __name__ == "__main__":
    main()
#python ans2_2.py '/home/yaxi4987/assignment_4/verb.csv'
#python ans2_2.py '/home/yaxi4987/assignment_4/body.csv'
#python ans2_2.py '/home/yaxi4987/assignment_4/colors.csv'
#python ans2_2.py '/home/yaxi4987/assignment_4/all_three.csv'