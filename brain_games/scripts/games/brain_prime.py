#!/usr/bin/env python3
import random
import math
from ..game import start

LOWER_BOUND = 0
UPPER_BOUND = 100


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_question_data():
    number = random.randint(LOWER_BOUND, UPPER_BOUND)
    answer = 'yes' if is_prime(number) else 'no'
    title = str(number)
    return title, answer


def main():
    description = ('Answer "yes" if given number is prime. '
                   'Otherwise answer "no".')
    start(description, get_question_data)


if __name__ == '__main__':
    main()
