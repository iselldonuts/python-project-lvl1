#!/usr/bin/env python3
import random
from ..game import start

LOWER_BOUND = 0
UPPER_BOUND = 100
LOWER_BOUND_STEP = 1
UPPER_BOUND_STEP = 10
LENGTH = 10


def get_question_data():
    start = random.randint(LOWER_BOUND, UPPER_BOUND)
    step = random.randint(LOWER_BOUND_STEP, UPPER_BOUND_STEP)
    progression = list(range(start, start + step * LENGTH, step))
    position = random.randint(0, LENGTH - 1)

    def remove_target_element(iv):
        i, v = iv
        return '..' if i == position else str(v)

    title = ' '.join(map(remove_target_element, enumerate(progression)))
    answer = str(progression[position])
    return title, answer


def main():
    description = 'What number is missing in the progression?'
    start(description, get_question_data)


if __name__ == '__main__':
    main()
