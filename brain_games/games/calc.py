from random import choice, choices
from brain_games.talk import talk_game

case = 'What is the result of the expression?'

operator = choice(["+", "-", "*"])


def calculated(num_1, num_2, operator):
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    return result


def get_question():
    num1, num2 = choices(range(1, 100), k=2)
    answer = calculated(num1, num2, operator)
    question = "{} {} {}".format(num1, operator, num2)
    return question, str(answer)


def run_game():
    talk_game(get_question, case)
