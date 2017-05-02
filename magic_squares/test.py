from pprint import pprint
from time import time

from magic_squares.solver import solve
from magic_squares.utils import is_correct


def test():
    n = 4
    grid = [[0 for i in range(n)] for j in range(n)]

    start = time()
    sol = solve(grid)
    end = time()
    pprint(end - start)
    pprint(is_correct(grid))
    pprint(sol)
