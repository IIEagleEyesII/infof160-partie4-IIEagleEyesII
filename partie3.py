#!/usr/bin/env python3

# std
from os.path import isfile
from sys import argv

# local
from breakthrough import Breakthrough
from const import *
from errors import *

def main(path=None):
    player2_is_ai = '-ai' in argv
    try:
        game = Breakthrough(path, player2_is_ai)
    except BadFormatError as e:
        print(e)
    else:
        game.play()
        winner = game.winner
        print(f'Player {CHARS[winner]} won!')

if __name__ == '__main__':
    if len(argv) < 2 or not isfile(argv[1]):
        main()
    else:
        main(argv[1])
