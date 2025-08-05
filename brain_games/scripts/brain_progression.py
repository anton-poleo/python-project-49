from brain_games.games import progression
from brain_games.games.engine import run


def main():
    run(progression.generate_question, progression.RULES_TEXT)


if __name__ == '__main__':
    main()
