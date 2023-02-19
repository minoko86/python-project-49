#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.talk import talk_game


def main():
    talk_game(gcd.get_question, gcd.CASE)


if __name__ == "__name__":
    main()
