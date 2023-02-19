from brain_games.utils import generate_number, get_operator

CASE = 'What is the result of the expression?'


def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    return result


def get_question():
    operator = get_operator()
    num1 = generate_number()
    num2 = generate_number()
    answer = calculate(num1, num2, operator)
    question = "{} {} {}".format(num1, operator, num2)
    return question, answer
