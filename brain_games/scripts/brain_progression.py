#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.talk import talk_game


def main():
    talk_game(progression.get_question, progression.CASE)


if __name__ == "__name__":
    main()
