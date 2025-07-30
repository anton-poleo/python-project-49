from brain_games.games import even
from brain_games.games.engine import run


def main():
    run(even.generate_question, even.RULES_TEXT)


if __name__ == '__main__':
    main()
