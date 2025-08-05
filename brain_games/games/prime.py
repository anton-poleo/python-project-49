from random import randint

from brain_games.games.transforms import bool_to_string

RULES_TEXT = """Answer "yes" if given number is prime. Otherwise answer "no"."""

MIN_NUMBER = 1
MAX_NUMBER = 50


def is_prime_number(value):
    if value <= 1:
        return False
    elif value == 2:
        return True

    last_check_item = int(value ** 0.5) + 1
    for item in range(2, last_check_item):
        if value % item == 0:
            return False

    return True


def generate_question():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = bool_to_string(is_prime_number(question))
    return question, answer
