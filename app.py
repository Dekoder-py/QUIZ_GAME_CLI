#!./.venv/bin/python3

import utils.questions as q
import utils.answers as a

questions = q.list_of_questions
answers = a.list_of_answers

num_correct = 0

for i in range(len(questions)):
    user_a = input(f"{questions[i]} ")
    correct_a = answers[i]
    if user_a.upper() == correct_a.upper():
        num_correct += 1
        print(f"Correct! Correct answers: {num_correct}")
    else:
        print("Sorry, that wasn't quite right.")
