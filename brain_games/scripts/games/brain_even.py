#!/usr/bin/env python3
import random
from ..game import start

LOWER_BOUND = 0
UPPER_BOUND = 10000


def get_question_data():
    number = random.randint(LOWER_BOUND, UPPER_BOUND)
    answer = 'yes' if number % 2 == 0 else 'no'
    title = str(number)
    return title, answer


def main():
    description = 'Answer "yes" if number even otherwise answer "no",'
    start(description, get_question_data)


if __name__ == '__main__':
    main()
