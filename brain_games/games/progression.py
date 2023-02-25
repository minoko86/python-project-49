from random import randint

RULE = 'What number is missing in the progression?'

PROGRESSION_LENGHT = 15
START = 1
END = 100
END_2 = 10


def get_progression(start, step, PROGRESSION_LENGHT):
    end = start + (PROGRESSION_LENGHT * step)
    progression = list(range(step, end, step))
    return progression


def get_the_data_for_the_round():
    start = randint(START, END)
    step = randint(START, END_2)
    item_index = randint(START, PROGRESSION_LENGHT - 1)
    progression = get_progression(start, step, PROGRESSION_LENGHT)
    answer = progression.pop(item_index)
    progression.insert(item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, answer
