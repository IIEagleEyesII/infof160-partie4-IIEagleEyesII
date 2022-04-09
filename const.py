from itertools import starmap
from pos2d import Pos2D

from sys import platform

DEFAULT_SIZE = 6
# Encodage du plateau
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
# pour print_board
a = ord('a')
z = ord('z')
ALPHABET = ''.join(map(chr, range(a, z+1)))
if platform == 'linux':
    BOLD  = lambda s: f'\033[1m{s}\033[0m'
    RED   = lambda s: f'\033[31m{s}\033[37m'
    GREEN = lambda s: f'\033[32m{s}\033[37m'
    CHARS = [BOLD('.'), BOLD(GREEN('W')), BOLD(RED('B'))]
else:
    CHARS = '.WB'
# pour is_valid_direction
VALID_MOVES = (
    tuple(starmap(Pos2D, ((-1, -1), (-1,  0), (-1,  1)))),  # W
    tuple(starmap(Pos2D, (( 1, -1), ( 1,  0), ( 1,  1)))),  # B
)
INF = float('inf')
POS_INF = +INF
NEG_INF = -INF

# Minimax
DRAW = 0
WIN  = +100
LOSS = -100

# Input utilisateur
YES   = 'y'
LEFT  = 'j'
RIGHT = 'l'
UP    = 'i'
DOWN  = 'k'
