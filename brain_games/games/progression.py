from random import randint
from brain_games.talk import talk_game

case = 'What is the result of the expression?'

progression_length = 15


def get_progression(start, step, progression_length):
    end = start + (progression_length * step)
    progression = list(range(start, end, step))
    return progression


def get_question():
    start = randint(1, 100)
    step = randint(1, 10)
    miss_item_index = randint(1, progression_length - 1)
    progression = get_progression(start, step, progression_length)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def run_game():
    talk_game(get_question, case)
