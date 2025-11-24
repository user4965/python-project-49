import random

from prompt import string

from brain_games.cli import greet, welcome_user


def is_even(n):
    return n % 2 == 0


def play_even_game(name):
    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number} ")
        answer = string("Your answer: ").lower().strip()
        if is_even(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if answer == correct_answer:
            print("Correct! ")
        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {correct_answer}."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


def main():
    greet()
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'")
    play_even_game(name)


if __name__ == '__main__':
    main()
