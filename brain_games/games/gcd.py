from random import choices
from brain_games.talk import talk_game

case = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    while num_2 != 0:
        (num_1, num_2) = (num_2, num_1 % num_2)
    return num_1


def get_question():
    num_1, num_2 = choices(range(1, 30), k=2)
    question = "{} {}".format(num_1, num_2)
    answer = get_gcd(num_1, num_2)
    return question, str(answer)


def run_game():
    talk_game(get_question, case)
