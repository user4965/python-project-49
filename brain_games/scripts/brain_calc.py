
from brain_games.cli import greet, welcome_user
from brain_games.engine import run_game
from brain_games.games.calc import DESCRIPTION, make_round


def main():
    greet()
    name = welcome_user()
    run_game(make_round, DESCRIPTION, name)


if __name__ == '__main__':
    main()
