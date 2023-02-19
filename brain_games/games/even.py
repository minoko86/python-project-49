#!/usr/bin/env python3
from random import randint

CASE = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0
END = 100


def generate_num():
    return randint(START, END)


def is_even(number):
    return number % 2 == 0


def get_question():
    question = generate_num()
    answer = is_even(question)
    return question, answer
