
import random

DESCRIPTION = "What is the result of the expression?"


def make_round():
    first_n = random.randint(1, 100)
    second_n = random.randint(1, 100)
    math_operation = random.choice(['+', '-', '*'])
    if math_operation == '+':
        result = first_n + second_n
    elif math_operation == '-':
        result = first_n - second_n
    elif math_operation == '*':
        result = first_n * second_n
    question = f"{first_n} {math_operation} {second_n}"
    correct_answer = str(result)
    return question, correct_answer
