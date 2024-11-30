import random

def get_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def prompt_user(lines):
    correct_answers = 0
    incorrect_answers = []
    total_questions = 0
    
    # Shuffle the lines to randomize the quiz
    random.shuffle(lines)
    
    for line in lines:
        english, swedish = line.strip().split(',')
        user_answer = input(f"What is the Swedish word for '{english}'? (or type 'quit' to exit): ").strip().lower()
        
        if user_answer == 'quit':
            break
        
        total_questions += 1
        
        if user_answer == swedish.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is '{swedish}'.")
            incorrect_answers.append((english, swedish))
    
    return correct_answers, incorrect_answers, total_questions

def main():
    file_path = 'eng_swe.txt'  # You can change this to 'short_eng_swe.txt' for testing
    lines = get_lines(file_path)
    
    score, to_practice, total_questions = prompt_user(lines)
    
    if total_questions > 0:
        print(f"\nYour score: {score} out of {total_questions}")
        print(f"Percentage: {(score / total_questions) * 100:.2f}%")
        
        if to_practice:
            print("\nWords to practice:")
            for english, swedish in to_practice:
                print(f"{english} - {swedish}")
        else:
            print("\nGreat job! You got all words correct.")
    else:
        print("\nQuiz ended. No questions were answered.")

if __name__ == "__main__":
    main()