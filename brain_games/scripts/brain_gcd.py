#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.talk import run_game


def main():
    run_game(gcd.get_the_data_for_the_round, gcd.RULE)


if __name__ == "__name__":
    main()
