from random import randint

RULES_TEXT = "Find the greatest common divisor of given numbers."

MIN_GCD = 1
MAX_GCD = 10
MIN_TERM = 2
MAX_TERM = 100


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_terms_by_gcd(gcd_value):
    factor_a = randint(MIN_TERM, MAX_TERM // gcd_value)
    factor_b = randint(MIN_TERM, MAX_TERM // gcd_value)
    while gcd(factor_a, factor_b) != 1:
        factor_b = randint(MIN_TERM, MAX_TERM // gcd_value)

    return factor_a * gcd_value, factor_b * gcd_value


def generate_gcd_with_terms():
    gcd_value = randint(MIN_GCD, MAX_GCD)
    terms = generate_terms_by_gcd(gcd_value)

    return *terms, gcd_value


def generate_question():
    *terms, gcd_value = generate_gcd_with_terms()
    return f"{terms[0]} {terms[1]}", str(gcd_value)
