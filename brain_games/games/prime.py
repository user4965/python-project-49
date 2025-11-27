
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


def make_round():
    number = random.randint(1, 100)
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    question = str(number)
    return question, correct_answer
