from random import randint

from brain_games.games.transforms import bool_to_string

MIN_NUMBER = 0
MAX_NUMBER = 100
RULES_TEXT = "Answer 'yes' if the number is even, otherwise answer 'no'."


def _is_even(number):
    return number % 2 == 0


def generate_question():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = bool_to_string(_is_even(question))

    return question, answer
