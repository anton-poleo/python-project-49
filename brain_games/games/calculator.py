from random import choice, randint

RULES_TEXT = "What is the result of the expression?"

MIN_NUMBER = 1
MAX_NUMBER = 20

OPERATORS = ['*', '+', '-']


def solve(left, right, op):
    match op:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case _:
            return


def generate_question():
    left = randint(MIN_NUMBER, MAX_NUMBER)
    right = randint(MIN_NUMBER, MAX_NUMBER)
    op = choice(OPERATORS)

    answer = str(solve(left, right, op))

    return f"{left} {op} {right}", answer

