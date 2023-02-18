from random import randrange
from brain_games.talk import talk_game

CASE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
QUESTION = randrange(1, 40, 2)


def is_prime(num):
    index = 1
    count = 0
    while index <= num // 2:
        if num % index == 0:
            count += 1
        index += 1
    return count == 1


def get_question():
    answer = "yes" if is_prime(QUESTION) else "no"
    return QUESTION, answer


def run_game():
    talk_game(get_question, CASE)
