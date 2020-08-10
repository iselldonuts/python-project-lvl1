#!/usr/bin/env python3
import random
import operator
from ..game import start

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}
LOWER_BOUND = 0
UPPER_BOUND = 100
UPPER_BOUND_MULT = UPPER_BOUND // 10


def get_question_data():
    operator = random.choice(list(OPERATORS.keys()))
    number1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    number2 = random.randint(
        LOWER_BOUND,
        UPPER_BOUND_MULT if operator == '*' else UPPER_BOUND
    )
    title = f'{number1} {operator} {number2}'
    answer = str(OPERATORS.get(operator)(int(number1), int(number2)))
    return title, answer


def main():
    description = 'What is the result of the expression?'
    start(description, get_question_data)


if __name__ == '__main__':
    main()
