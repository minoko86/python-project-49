#!/usr/bin/env python3

from brain_games.games import even
from brain_games.talk import talk_game


def main():
    talk_game(even.get_question, even.CASE)


if __name__ == "__name__":
    main()
