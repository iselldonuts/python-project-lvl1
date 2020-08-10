#!/usr/bin/env python3
import prompt

VICTORY_SCORE = 3


def start(description, get_current_question_data):
    print('Welcome to the Brain Games!')
    print(description)
    print()

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!\n')

    score = 0
    while score < VICTORY_SCORE:
        question, correct_answer = get_current_question_data()
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(.',
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}")
            return

    print(f'Congratulations, {name}!')
