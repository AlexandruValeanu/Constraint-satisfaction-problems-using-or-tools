from ortools.constraint_solver import pywrapcp
from itertools import chain
from magic_squares.utils import *


def solve(grid):
    n = len(grid)

    assert is_valid(grid)

    # Create the solver.
    solver = pywrapcp.Solver("magic-squares")

    variables = [[None for i in range(n)] for j in range(n)]
    exp_sum = expected_sum(n)

    # Create all variables
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                variables[i][j] = solver.IntVar(1, n * n, "x{0},{1}".format(i, j))
            else:
                variables[i][j] = solver.IntVar(grid[i][j], grid[i][j], "x{0},{1}".format(i, j))

    # Add constraints for expected sum
    for i in range(n):
        solver.Add(solver.SumEquality([variables[i][j] for j in range(n)], exp_sum))  # sum on lines
        solver.Add(solver.SumEquality([variables[j][i] for j in range(n)], exp_sum))  # sum on columns

    solver.Add(solver.SumEquality([variables[i][i] for i in range(n)], exp_sum))  # sum on main diagonal
    solver.Add(solver.SumEquality([variables[i][n - i - 1] for i in range(n)], exp_sum))  # sum on second diagonal

    # All numbers must be unique
    solver.Add(solver.AllDifferent(list(chain(*variables))))

    db = solver.Phase(list(chain(*variables)), solver.CHOOSE_MIN_SIZE_LOWEST_MAX, solver.ASSIGN_CENTER_VALUE)
    solver.NewSearch(db)

    sol_grid = [[0 for i in range(n)] for j in range(n)]

    if solver.NextSolution():
        for i in range(n):
            for j in range(n):
                sol_grid[i][j] = variables[i][j].Value()

    return sol_grid



