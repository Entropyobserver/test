# Constants for text colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

import sys

def load_csv_file(file_path):
    """
    Load and read the CSV file containing word translations.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of lines from the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def create_translation_dict(lines):
    """
    Create a dictionary of English-Swedish word pairs from CSV lines.
    
    Args:
        lines (list): List of strings from CSV file
        
    Returns:
        dict: Dictionary with English words as keys and Swedish translations as values
    """
    translations = {}
    try:
        for line in lines:
            if ',' in line:
                english, swedish = line.strip().split(',')
                translations[english.strip()] = swedish.strip()
        return translations
    except Exception as e:
        print(f"Error processing translations: {e}")
        sys.exit(1)

def conduct_test(translations):
    """
    Conduct the translation test and track results.
    
    Args:
        translations (dict): Dictionary of English-Swedish word pairs
        
    Returns:
        tuple: Lists of correct and incorrect answers
    """
    correct = []
    incorrect = []
    
    print("\nSwedish Word Test")
    print("-" * 20)
    
    for english, swedish in translations.items():
        try:
            answer = input(f"Translate '{english}' to Swedish: ").strip().lower()
            if answer == swedish.lower():
                print(f"{GREEN}Correct!{RESET}")
                correct.append(english)
            else:
                print(f"{RED}Incorrect. The correct answer is '{swedish}'{RESET}")
                incorrect.append(english)
        except KeyboardInterrupt:
            print("\nTest interrupted.")
            break
    
    return correct, incorrect

def display_results(correct, incorrect):
    """
    Display test results to the user.
    
    Args:
        correct (list): List of correctly answered words
        incorrect (list): List of incorrectly answered words
    """
    total = len(correct) + len(incorrect)
    if total > 0:
        correct_percent = (len(correct) / total) * 100
        print("\nTest Results:")
        print(f"Correct: {len(correct)} ({correct_percent:.1f}%)")
        print(f"Incorrect: {len(incorrect)} ({100 - correct_percent:.1f}%)")

def ask_retry():
    """
    Ask if the user wants to try again.
    
    Returns:
        bool: True if user wants to retry, False otherwise
    """
    while True:
        response = input("\nWould you like to try again? (y/n): ").strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' or 'n'")

def main():
    """
    Main function to run the Swedish word test program.
    """
    try:
        # Get file path from command line or user input
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
        else:
            file_path = input("Enter path to CSV file: ").strip()
        
        # Load translations
        lines = load_csv_file(file_path)
        translations = create_translation_dict(lines)
        
        # Main program loop
        while True:
            correct, incorrect = conduct_test(translations)
            display_results(correct, incorrect)
            
            if not ask_retry():
                print("\nThank you for practicing Swedish!")
                break
                
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

#python test2.py '/home/yaxi4987/assignment_4/all_three.csv'