#!/usr/bin/env python3
from brain_games.utils import transform_answer
from random import randrange
import prompt

ATTEMPT_COUNT = 3


def talk_game(get_question, case):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(user_name))
    print(case)
    for i in range(ATTEMPT_COUNT):
 #       question, correct_answer = get_question()
        question, correct_answer = get_question()
        print("Question: {}".format(question))
        user_answer = input("Your answer: ")
        # if correct_answer() == user_answer:
        if transform_answer(correct_answer) == user_answer:
            print("Correct!")
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            #        user_answer, correct_answer))
                     user_answer, correct_answer))
            print("Let's try again, {}!".format(user_name))
            return
    print("Congratulations, {}!".format(user_name))
