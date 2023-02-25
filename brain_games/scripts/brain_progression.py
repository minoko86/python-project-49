#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.talk import run_game


def main():
    run_game(progression.get_the_data_for_the_round, progression.RULE)


if __name__ == "__name__":
    main()
