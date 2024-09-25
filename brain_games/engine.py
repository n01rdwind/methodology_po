import random

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    return name

def run_game(game_module, rounds=3):
    name = welcome_user()
    print(game_module.DESCRIPTION)
    
    correct_answers = 0
    wrong_answers = []
    
    for i in range(rounds):
        question, correct_answer = game_module.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            wrong_answers.append((question, correct_answer, user_answer))
    
    if correct_answers == rounds:
        print(f"Congratulations, {name}!")
    else:
        print(f"You answered correctly {correct_answers} out of {rounds} questions.")