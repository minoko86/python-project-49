from random import randrange

START = 1
END = 100
STEP = 2
TRUE = 'yes'
FALSE = 'no'


def generate_number():
    return randrange(START, END, STEP)


def transform_answer(answer):
    if type(answer) is int:
        return str(answer)
    elif type(answer) is str:
        return answer
    elif type(answer) is bool:
        if answer is True:
            return TRUE
        return FALSE
