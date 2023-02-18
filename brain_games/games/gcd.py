from random import choices
from brain_games.talk import talk_game

CASE = 'Find the greatest common divisor of given numbers.'
NUM_1, NUM_2 = choices(range(1, 30), k=2)


def get_gcd(NUM_1, NUM_2):
    while NUM_2 != 0:
        (NUM_1, NUM_2) = (NUM_2, NUM_1 % NUM_2)
    return NUM_1


def get_question():
    question = "{} {}".format(NUM_1, NUM_2)
    answer = get_gcd(NUM_1, NUM_2)
    return question, str(answer)


def run_game():
    talk_game(get_question, CASE)
