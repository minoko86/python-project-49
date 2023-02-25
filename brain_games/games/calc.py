from brain_games.utils import generate_number
from random import choice

RULE = 'What is the result of the expression?'
SUMMA = "+"
DIFF = "-"
PROD = "*"


def get_operator():
    return choice([SUMMA, DIFF, PROD])


def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    return result


def get_the_data_for_the_round():
    operator = get_operator()
    num1 = generate_number()
    num2 = generate_number()
    answer = calculate(num1, num2, operator)
    question = f"{num1} {operator} {num2}"
    return question, answer
