from random import randint
from brain_games.talk import talk_game

CASE = 'What number is missing in the progression?'

PROGRESSION_LENGHT = 15

START = randint(1, 100)
STEP = randint(1, 10)


def get_progression(START, STEP, PROGRESSION_LENGHT):
    end = START + (PROGRESSION_LENGHT * STEP)
    progression = list(range(START, end, STEP))
    return progression


def get_question():
    miss_item_index = randint(1, PROGRESSION_LENGHT - 1)
    progression = get_progression(START, STEP, PROGRESSION_LENGHT)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def run_game():
    talk_game(get_question, CASE)
