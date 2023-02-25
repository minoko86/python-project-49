#!/usr/bin/env python3

from brain_games.games import calc
from brain_games.talk import run_game


def main():
    run_game(calc.get_the_data_for_the_round, calc.RULE)


if __name__ == "__name__":
    main()
