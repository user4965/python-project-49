from prompt import string


def run_game(make_round, description, name):
    print(description)
    for _ in range(3):
        question, correct_answer = make_round()
        print(f"Question: {question} ")
        answer = string("Your answer: ").lower().strip()
        if answer == correct_answer:
            print("Correct! ")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
