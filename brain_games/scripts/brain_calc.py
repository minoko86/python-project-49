#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.talk import talk_game


def main():
    talk_game(calc.get_question, calc.CASE)


if __name__ == "__name__":
    main()
