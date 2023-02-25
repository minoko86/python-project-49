from brain_games.utils import generate_number

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    index = 1
    count = 0
    while index <= num // 2:
        if num % index == 0:
            count += 1
        index += 1
    return count == 1


def get_the_data_for_the_round():
    question = generate_number()
    answer = is_prime(question)
    return question, answer
