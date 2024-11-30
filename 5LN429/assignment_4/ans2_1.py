import sys
import csv

# Global constants for colors
COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'

def load_word_list(filename):
    """Load the word list from the CSV file."""
    word_list = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    english_word, swedish_word = row
                    word_list.append((english_word.strip(), swedish_word.strip()))
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
    return word_list

def quiz_user(word_list):
    """Quiz the user on the word list."""
    correct_count = 0
    incorrect_count = 0

    for english, swedish in word_list:
        user_answer = input(f"What is the Swedish word for '{english}'? ").strip()
        if user_answer.lower() == swedish.lower():
            print(COLOR_GREEN + "Correct!" + COLOR_RESET)
            correct_count += 1
        else:
            print(COLOR_RED + f"Incorrect. The correct answer is '{swedish}'." + COLOR_RESET)
            incorrect_count += 1

    print("\nQuiz finished!")
    print(f"{COLOR_GREEN}Correct answers: {correct_count}{COLOR_RESET}")
    print(f"{COLOR_RED}Incorrect answers: {incorrect_count}{COLOR_RESET}")

def main():
    """Main function to run the program."""
    if len(sys.argv) < 2:
        print("Usage: python quiz.py <filename.csv>")
        sys.exit(1)

    filename = sys.argv[1]
    word_list = load_word_list(filename)

    while True:
        quiz_user(word_list)
        retry = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
