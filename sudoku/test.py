from sudoku import solver
from pprint import pprint
from sudoku.utils import check_solution


def test():
    multiple = [[9, 0, 6, 0, 7, 0, 4, 0, 3],
                [0, 0, 0, 4, 0, 0, 2, 0, 0],
                [0, 7, 0, 0, 2, 3, 0, 1, 0],
                [5, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 4, 0, 2, 0, 8, 0, 6, 0],
                [0, 0, 3, 0, 0, 0, 0, 0, 5],
                [0, 3, 0, 7, 0, 0, 0, 5, 0],
                [0, 0, 7, 0, 0, 5, 0, 0, 0],
                [4, 0, 5, 0, 1, 0, 7, 0, 8]]

    homework = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
                [8, 0, 0, 2, 0, 3, 0, 0, 6],
                [0, 3, 0, 0, 6, 0, 0, 7, 0],
                [0, 0, 1, 0, 0, 0, 6, 0, 0],
                [5, 4, 0, 0, 0, 0, 0, 1, 9],
                [0, 0, 2, 0, 0, 0, 7, 0, 0],
                [0, 9, 0, 0, 3, 0, 0, 8, 0],
                [2, 0, 0, 8, 0, 4, 0, 0, 7],
                [0, 1, 0, 9, 0, 7, 0, 6, 0]]

    sol = solver.solve(homework)
    pprint(check_solution(sol))
    pprint(sol)

    sol = solver.solve(multiple)
    pprint(check_solution(sol))
    pprint(sol)