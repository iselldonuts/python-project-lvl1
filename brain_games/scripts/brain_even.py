#!/usr/bin/env python3
import random
import prompt

LOWER_BOUND = 0
UPPER_BOUND = 10000


def generate_number():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def get_correct_answer(question):
    return 'yes' if question % 2 == 0 else 'no'


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!\n')

    number = generate_number()
    score = 0

    while score < 3:
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(number)

        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(.',
                  f'Correct answer was "{correct_answer}".')
            print("Let's try again, Bill")
            return

        number = generate_number()

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
