from brain_games.utils import generate_number

RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    while num_2 != 0:
        (num_1, num_2) = (num_2, num_1 % num_2)
    return num_1


def get_the_data_for_the_round():
    num_1 = generate_number()
    num_2 = generate_number()
    question = f"{num_1} {num_2}"
    answer = get_gcd(num_1, num_2)
    return question, answer
