from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0
END = 100


def generate_num():
    return randint(START, END)


def is_even(number):
    return number % 2 == 0


def get_the_data_for_the_round():
    question = generate_num()
    answer = is_even(question)
    return question, answer
