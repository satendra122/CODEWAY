import random

def load_questions():
    # Define your quiz questions and answers here
    questions = [
        {"question": "What is the capital of France?", "options": ["A. London", "B. Paris", "C. Berlin"], "correct": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Mars", "B. Venus", "C. Jupiter"], "correct": "A"},
        {"question": "What is the largest mammal in the world?", "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe"], "correct": "B"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen"], "correct": "B"},
        {"question": "What is the capital of Japan?", "options": ["A. Seoul", "B. Tokyo", "C. Beijing"], "correct": "B"},
        {"question": "Which element has the chemical symbol 'O'?", "options": ["A. Oxygen", "B. Gold", "C. Carbon"], "correct": "A"},
        {"question": "What is the currency of Brazil?", "options": ["A. Peso", "B. Real", "C. Yen"], "correct": "B"},
        {"question": "In which year did the Titanic sink?", "options": ["A. 1912", "B. 1923", "C. 1905"], "correct": "A"},
        {"question": "Who painted the Mona Lisa?", "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci"], "correct": "C"},
        {"question": "What is the capital of Australia?", "options": ["A. Sydney", "B. Melbourne", "C. Canberra"], "correct": "C"},
        # Add more questions as needed
    ]
    return questions

def present_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Your answer: ").upper()
    return user_answer

def evaluate_answer(user_answer, correct_answer, score):
    if user_answer == correct_answer:
        print("Correct! Well done.")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
    return score

def display_results(final_score):
    print(f"\nYour final score is:{final_score} out of 10")

def play_quiz():
    print("Welcome to the Quiz Game!")
    print("Answer each question with the corresponding letter (A, B, C).")
    
    questions = load_questions()
    score = 0

    for question in random.sample(questions, len(questions)):
        user_answer = present_question(question)
        score = evaluate_answer(user_answer, question["correct"], score)

    display_results(score)

if __name__ == "__main__":
    play_again = "yes"

    while play_again.lower() == "yes":
        play_quiz()
        play_again = input("Do you want to play again? (yes/no): ")
    
    print("Thank you for playing the Quiz Game!")