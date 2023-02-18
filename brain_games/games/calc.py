from random import choice, randrange
from brain_games.talk import talk_game
from brain_games.talk import generate_number

CASE = 'What is the result of the expression?'
NUM1 = generate_number()
NUM2 = generate_number()


operator = choice(["+", "-", "*"])


def calculate(NUM1, NUM2, operator):
    if operator == "+":
        result = NUM1 + NUM2
    elif operator == "-":
        result = NUM1 - NUM2
    elif operator == "*":
        result = NUM1 * NUM2
    return result


def get_question():
    answer = calculate(NUM1, NUM2, operator)
    question = "{} {} {}".format(NUM1, operator, NUM2)
    return question, str(answer)


def run_game():
    talk_game(get_question, CASE)
