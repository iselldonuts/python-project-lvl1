#!/usr/bin/env python3
import random
from ..game import start

LOWER_BOUND = 0
UPPER_BOUND = 100


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def get_question_data():
    number1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    number2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    answer = str(nod(number1, number2))
    title = f'{number1} {number2}'
    return title, answer


def main():
    description = 'Find the greatest common divisor of given numbers.'
    start(description, get_question_data)


if __name__ == '__main__':
    main()
