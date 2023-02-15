#!/usr/bin/env python3

from random import randint
from brain_games.talk import talk_game

case = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer


def run_game():
    talk_game(get_question, case)
