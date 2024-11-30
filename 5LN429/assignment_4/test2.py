import csv
import sys
import random

# Global constants for color coding
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def load_words(filename):
    """Load words from a CSV file and return them as a list of tuples (English, Swedish)."""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    words.append((row[0].strip(), row[1].strip()))
    except FileNotFoundError:
        print(f"{RED}Error: File '{filename}' not found.{RESET}")
        sys.exit(1)
    return words

def quiz_user(words):
    """Quiz the user on Swedish words and track the score."""
    correct_count = 0
    incorrect_count = 0
    
    # Shuffle words for random order
    random.shuffle(words)

    for english, swedish in words:
        print(f"What is the Swedish word for '{english}'?")
        answer = input("Your answer: ").strip()

        if answer.lower() == swedish.lower():
            print(f"{GREEN}Correct!{RESET}")
            correct_count += 1
        else:
            print(f"{RED}Incorrect.{RESET} The correct answer is '{swedish}'.")
            incorrect_count += 1
        
        # Ask if user wants to try another word
        try_again = input("Do you want to try another word? (yes/no): ").strip().lower()
        if try_again != 'yes':
            break
    
    # Show final results
    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}")

def main():
    # Check for CSV filename in command line arguments
    if len(sys.argv) < 2:
        print(f"{RED}Error: Please provide a CSV file as an argument.{RESET}")
        sys.exit(1)

    filename = sys.argv[1]
    words = load_words(filename)
    
    if words:
        quiz_user(words)

if __name__ == "__main__":
    main()
