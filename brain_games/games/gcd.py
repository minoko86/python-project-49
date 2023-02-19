from brain_games.utils import generate_number

CASE = 'Find the greatest common divisor of given numbers.'
# NUM_1, NUM_2 = choices(range(1, 30), k=2)


def get_gcd(num_1, num_2):
    while num_2 != 0:
        (num_1, num_2) = (num_2, num_1 % num_2)
    return num_1


def get_question():
    num_1 = generate_number()
    num_2 = generate_number()
    question = "{} {}".format(num_1, num_2)
    answer = get_gcd(num_1, num_2)
    return question, answer
