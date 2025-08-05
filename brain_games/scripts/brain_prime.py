from brain_games.games import prime
from brain_games.games.engine import run


def main():
    run(prime.generate_question, prime.RULES_TEXT)


if __name__ == '__main__':
    main()
