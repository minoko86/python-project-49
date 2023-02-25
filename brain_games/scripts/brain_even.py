#!/usr/bin/env python3

from brain_games.games import even
from brain_games.talk import run_game


def main():
    run_game(even.get_the_data_for_the_round, even.RULE)


if __name__ == "__name__":
    main()
