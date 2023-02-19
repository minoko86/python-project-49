from random import randint

CASE = 'What number is missing in the progression?'

PROGRESSION_LENGHT = 15
START = 1
END = 100
END_2 = 10


def generate_num():
    return randint(START, END)


def generate_num_2():
    return randint(START, END_2)


def generate_item():
    return randint(START, PROGRESSION_LENGHT - 1)


def get_progression(start, step, PROGRESSION_LENGHT):
    end = start + (PROGRESSION_LENGHT * step)
    progression = list(range(step, end, step))
    return progression


def get_question():
    start = generate_num()
    step = generate_num_2()
    miss_item_index = generate_item()
    progression = get_progression(start, step, PROGRESSION_LENGHT)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, answer
