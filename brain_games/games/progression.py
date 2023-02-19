from brain_games.utils import generate_num_2, generate_num_3, generate_item

CASE = 'What number is missing in the progression?'

PROGRESSION_LENGHT = 15


def get_progression(start, step, PROGRESSION_LENGHT):
    end = start + (PROGRESSION_LENGHT * step)
    progression = list(range(step, end, step))
    return progression


def get_question():
    start = generate_num_2()
    step = generate_num_3()
    miss_item_index = generate_item()
    progression = get_progression(start, step, PROGRESSION_LENGHT)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, answer
