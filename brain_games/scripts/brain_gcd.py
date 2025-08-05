from brain_games.games import gcd
from brain_games.games.engine import run


def main():
    run(gcd.generate_question, gcd.RULES_TEXT)


if __name__ == '__main__':
    main()
