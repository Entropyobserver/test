import random

def get_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def prompt_user(lines):
    correct_answers = 0
    incorrect_answers = []
    
    # Shuffle the lines to randomize the quiz
    random.shuffle(lines)
    
    for line in lines:
        english, swedish = line.strip().split(',')
        user_answer = input(f"What is the Swedish word for '{english}'? ").strip().lower()
        
        if user_answer == swedish.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is '{swedish}'.")
            incorrect_answers.append((english, swedish))
    
    return correct_answers, incorrect_answers

def main():
    file_path = 'eng_swe.txt'  # You can change this to 'short_eng_swe.txt' for testing
    lines = get_lines(file_path)
    
    total_questions = len(lines)
    score, to_practice = prompt_user(lines)
    
    print(f"\nYour score: {score} out of {total_questions}")
    print(f"Percentage: {(score / total_questions) * 100:.2f}%")
    
    if to_practice:
        print("\nWords to practice:")
        for english, swedish in to_practice:
            print(f"{english} - {swedish}")
    else:
        print("\nGreat job! You got all words correct.")

if __name__ == "__main__":
    main()
