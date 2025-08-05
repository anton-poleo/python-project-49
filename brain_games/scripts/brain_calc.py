from brain_games.games import calculator
from brain_games.games.engine import run


def main():
    run(calculator.generate_question, calculator.RULES_TEXT)


if __name__ == '__main__':
    main()
