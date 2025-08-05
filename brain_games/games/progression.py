from random import randint

RULES_TEXT = "What number is missing in the progression?"

MIN_START_VALUE = 1
MAX_START_VALUE = 20

MIN_STEP_VALUE = 2
MAX_STEP_VALUE = 9

SEQUENCE_SIZE = 10


def generate_arithmetic_sequence():
    sequence = []
    start_value = randint(MIN_START_VALUE, MAX_START_VALUE)
    step_value = randint(MIN_STEP_VALUE, MAX_STEP_VALUE)
    end_value = start_value + SEQUENCE_SIZE * step_value

    for value in range(start_value, end_value, step_value):
        sequence.append(str(value))

    return sequence


def generate_question():
    sequence = generate_arithmetic_sequence()
    answer_index = randint(0, len(sequence) - 1)

    answer = sequence[answer_index]
    sequence[answer_index] = ".."
    question = " ".join(sequence)

    return question, answer
