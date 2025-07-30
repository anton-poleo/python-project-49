import prompt

GAME_ROUNDS = 3


def play_round(generate_question):
    question, correct_answer = generate_question()
    print(f"Question: {question}")

    answer = prompt.string("Your answer: ")

    if answer != correct_answer:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        return False

    print("Correct!")
    return True


def run(generate_question, rules_text):
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")

    print(rules_text)

    for _ in range(GAME_ROUNDS):
        win = play_round(generate_question)
        if win is False:
            print(f"Let's try again, {name}!")
            return False

    print(f"Congratulations, {name}!")
    return True
