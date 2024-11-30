import sys
import random

# Constants for color coding
COLOR_GREEN = "\033[92m"  # Green color for correct answers
COLOR_RED = "\033[91m"    # Red color for incorrect answers
RESET = "\033[0m"         # Reset color

def read_file(path):
    """Reads the file at the specified path and returns a list of lines."""
    try:
        with open(path, 'r') as f:
            words = f.readlines()
        return words
    except FileNotFoundError:
        print(f"File at {path} not found")
        sys.exit(1)

def translate_dict(words):
    """Converts a list of comma-separated words into a dictionary."""
    translate_dict = {}
    for word in words:
        try:
            english_word, swedish_word = word.strip().split(",")
            translate_dict[english_word] = swedish_word
        except ValueError:
            print("File must contain words separated by comma")
    return translate_dict

def word_test(test_dict):
    """Quizzes the user on Swedish translations of English words."""
    incorrect = 0
    correct = 0
    total = 0
    english_words = list(test_dict.keys())
    random.shuffle(english_words)

    while True:  # Outer loop to allow retry option
        for english_word in english_words:
            swedish_word = test_dict[english_word]
            answer = input(f"Please enter the Swedish word for '{english_word}': ").strip()

            if answer.lower() == swedish_word.lower():
                correct += 1
                print(f"{COLOR_GREEN}Correct!{RESET}")
            else:
                incorrect += 1
                print(f"{COLOR_RED}Incorrect!{RESET} The correct answer is '{swedish_word}'.")

            total += 1

        # Asking user if they want to try again after completing all words
        retry = input("Do you want to try again? (y/n): ").strip().lower()  # 修改了提示信息
        if retry != "y":
            break  # Exit the outer loop if user doesn't want to retry

    # Final report outside the loop
    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Total words tested: {total}")

def main():
    """Main function to run the vocabulary test."""
    if len(sys.argv) < 2:  # Checking if filename is provided as argument
        print("Error: Please provide a CSV file as an argument.")
        sys.exit(1)

    path = sys.argv[1]
    words = read_file(path)
    word_dict = translate_dict(words) 
    word_test(word_dict)

if __name__ == "__main__":
    main()
#python test3.py '/home/yaxi4987/assignment_4/verb.csv'