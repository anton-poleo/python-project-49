from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100
RULES_TEXT = "Answer 'yes' if the number is even, otherwise answer 'no'."


def _is_even(number):
    return number % 2 == 0


def _string_to_bool(string):
    if string == "yes":
        return True
    elif string == "no":
        return False


def _bool_to_string(string):
    if string is True:
        return "yes"
    elif string is False:
        return "no"


def generate_question():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = _bool_to_string(_is_even(question))

    return question, answer
