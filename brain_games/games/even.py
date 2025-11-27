
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def make_round():
    number = random.randint(1, 100)
    if is_even(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    question = str(number)
    return question, correct_answer
