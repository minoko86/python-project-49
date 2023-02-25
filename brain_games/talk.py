from brain_games.utils import transform_answer
import prompt

ATTEMPT_COUNT = 3


def run_game(get_question, RULE):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(RULE)
    for i in range(ATTEMPT_COUNT):
        question, correct_answer = get_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        user_answer = user_answer.lower()
        if transform_answer(correct_answer) != user_answer:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer, transform_answer(correct_answer)))
            print("Let's try again, {user_name}!")
            return
        print("Correct!")
    print(f"Congratulations, {user_name}!")
