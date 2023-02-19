from random import randrange, randint, choice

PROGRESSION_LENGHT = 15
START = 1
START_2 = 0
END = 100
END_2 = 10
STEP = 2


def generate_number():
    return randrange(START, END, STEP)


def generate_num():
    return randint(START_2, END)


def generate_num_2():
    return randint(START, END)


def generate_num_3():
    return randint(START, END_2)


def generate_item():
    return randint(START, PROGRESSION_LENGHT - 1)


def get_operator():
    return choice(["+", "-", "*"])


def transform_answer(answer):
    if  type(answer) is int:
        return str(answer)
    elif type(answer) is str:
        return str
    elif type(answer) is bool:
        if answer is True:
            return 'yes'
        return 'no'