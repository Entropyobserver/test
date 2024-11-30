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

def parse_words(words):
    """Converts a list of comma-separated words into a dictionary."""
    word_dict = {}
    for word in words:
        try:
            english_word, swedish_word = word.strip().split(",")
            word_dict[english_word] = swedish_word
        except ValueError:
            print("File must contain words separated by comma.")
    return word_dict

def word_test(word_dict):
    """Quizzes the user on Swedish translations of English words."""
    correct = 0
    incorrect = 0
    total = 0

    english_words = list(word_dict.keys())
    random.shuffle(english_words)

    for english_word in english_words:
        swedish_word = word_dict[english_word]
        answer = input(f"Please enter the Swedish word for '{english_word}': ").strip()

        if answer.lower() == swedish_word.lower():
            correct += 1
            print(f"{COLOR_GREEN}Correct!{RESET}")
        else:
            incorrect += 1
            print(f"{COLOR_RED}Incorrect!{RESET} The correct answer is '{swedish_word}'.")

        total += 1

        # Ask user if they want to continue
        retry = input("Do you want to try another word? (y/n): ").strip().lower()
        if retry != 'y':
            break

    # Final report
    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Total words tested: {total}")

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a CSV file as an argument.")
        sys.exit(1)

    path = sys.argv[1]
    words = read_file(path)
    word_dict = parse_words(words)
    word_test(word_dict)

if __name__ == "__main__":
    main()