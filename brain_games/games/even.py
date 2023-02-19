#!/usr/bin/env python3
from brain_games.utils import generate_num

CASE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question():
    question = generate_num()
#    answer = "yes" if is_even(question) else "no"
    answer = is_even(question)
    return question, answer
#    return question
