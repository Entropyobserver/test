import sys
import csv
import random

# Color constants (optional)
CORRECT_COLOR = '\033[92m'  # Green
INCORRECT_COLOR = '\033[91m'  # Red
RESET_COLOR = '\033[0m'  # Reset color

def load_word_data(file_path):
    """
    Load word data from a CSV file.
    Returns a dictionary where the keys are English words and the values are the corresponding Swedish words.
    """
    word_data = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                english_word, swedish_word = row
                word_data[english_word] = swedish_word
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    return word_data

def play_game(word_data):
    """
    Game logic:
    1. Randomly select an English word from the word data.
    2. Prompt the user to enter the corresponding Swedish word.
    3. Check if the user's answer is correct and record the result.
    4. Output the final score.
    """
    correct_answers = 0
    total_questions = 0
    while True:
        english_word = random.choice(list(word_data.keys()))
        swedish_word = word_data[english_word]
        user_answer = input(f"Enter the Swedish translation for '{english_word}': ")
        if user_answer.lower() == swedish_word.lower():
            print(f"{CORRECT_COLOR}Correct!{RESET_COLOR}")
            correct_answers += 1
        else:
            print(f"{INCORRECT_COLOR}Incorrect, the correct answer is '{swedish_word}'.{RESET_COLOR}")
        total_questions += 1
        play_again = input("Do you want to continue? (Enter 'y' to continue, any other key to exit) ").lower()
        if play_again != 'y':
            break
    print(f"You got {correct_answers} out of {total_questions} questions right.")

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a CSV file as an argument.")
        sys.exit(1)
    file_path = sys.argv[1]
    word_data = load_word_data(file_path)
    play_game(word_data)

if __name__ == "__main__":
    main()

# To run the script: python test3.py '/home/yaxi4987/assignment_4/verb.csv'
