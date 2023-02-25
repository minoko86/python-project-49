#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.talk import run_game


def main():
    run_game(prime.get_the_data_for_the_round, prime.RULE)


if __name__ == "__name__":
    main()
