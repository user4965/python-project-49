
import random

DESCRIPTION = "What number is missing in the progression?"


def progression(start, size, step):
    new_list = []
    for i in range(size):
        element = (start + i * step)
        new_list.append(element)
    return new_list


def make_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    size = random.randint(5, 10)
    new_list = progression(start, size, step)
    hidden_index = random.randint(0, len(new_list) - 1)
    correct_answer = new_list[hidden_index]
    new_list[hidden_index] = ".."
    new_list = [str(x) for x in new_list]
    question = " ".join(new_list)
    correct_answer = str(correct_answer)
    return question, correct_answer
