import sys
import random

COLOR_RESET = "\033[0m"        # Reset color
COLOR_GREEN = "\033[92m"       # Green color for correct answers
COLOR_RED = "\033[91m"         # Red color for incorrect answers

def read_file(path):
    try:
        with open(path,'r',) as f:
            words = f.readlines()
        return words
    except FileNotFoundError:
        print(f"File at {path} not found")
        sys.exit(1)


def translate_dict(words):
    translate_dict = {}
    for word in words:
        try:
            english_word,swedish_word = word.strip().split(",")
            translate_dict[english_word] = swedish_word
        except ValueError:
            print("File must contain words separated by comma")
    return translate_dict


def word_test(test_dict):
    incorrect = 0
    correct = 0
    total = 0
    english_words = list(test_dict.keys())
    random.shuffle(english_words)

    while True:

        for english_word in english_words:
            swedish_word = test_dict[english_word]
            user_answer = input(f"please enter swedish translation for '{english_word}':")
            if user_answer.lower() == swedish_word.lower():
                correct += 1
                print(f"{COLOR_GREEN}Correct!{COLOR_RESET}")
            else:
                print(f"{COLOR_RED}Incorrect. The correct answer is '{swedish_word}'.{COLOR_RESET}")
                incorrect += 1
            total += 1
        
        retry = input("Would you like to try again? (y/n): ").strip().lower()
        if retry != 'y':
            print("Thank you for playing!")
            break

    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Total words tested: {total}")


def main():
    path = sys.argv[1]
    #path = '/home/yaxi4987/assignment_4/verb.csv'
    words = read_file(path)
    test_dict = translate_dict(words) 
    word_test(test_dict)


if __name__ == "__main__":
    main()
#python ans2_6.py '/home/yaxi4987/assignment_4/verb.csv'
#python ans2_6.py '/home/yaxi4987/assignment_4/body.csv'
#python ans2_6.py '/home/yaxi4987/assignment_4/colors.csv'
#python ans2_6.py '/home/yaxi4987/assignment_4/all_three.csv'