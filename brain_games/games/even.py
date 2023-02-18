#!/usr/bin/env python3

from random import randint
from brain_games.talk import talk_game

CASE = 'Answer "yes" if the number is even, otherwise answer "no".'
QUESTION = randint(0, 100)


def is_even(number):
    return number % 2 == 0


def get_question():
    answer = "yes" if is_even(QUESTION) else "no"
    return QUESTION, answer


def run_game():
    talk_game(get_question, CASE)
