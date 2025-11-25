
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def make_round():
    first_n = random.randint(1, 100)
    second_n = random.randint(1, 100)
    result = gcd(first_n, second_n)
    question = f"{first_n} {second_n}"
    correct_answer = str(result)
    return question, correct_answer
