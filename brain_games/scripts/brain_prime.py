#!/usr/bin/env python3

from brain_games.games import prime
from brain_games.talk import talk_game


def main():
    talk_game(prime.get_question, prime.CASE)


if __name__ == "__name__":
    main()
