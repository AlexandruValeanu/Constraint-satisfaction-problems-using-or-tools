from ortools.constraint_solver import pywrapcp
from itertools import chain


def solve(grid):
    n = len(grid)
    solver = pywrapcp.Solver("sudoku-solver")

    variables = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                variables[i][j] = solver.IntVar(1, 9, "x{0},{1}".format(i, j))
            else:
                variables[i][j] = solver.IntVar(grid[i][j], grid[i][j], "x{0},{1}".format(i, j))

    # All rows and columns contain all digits only once
    for i in range(n):
        solver.AddConstraint(solver.AllDifferent([variables[i][j] for j in range(n)]))
        solver.AddConstraint(solver.AllDifferent([variables[j][i] for j in range(n)]))

    # All 3x3 regions contain all digits only once
    for u in range(0, 3):
        for v in range(0, 3):
            constraint = []
            for i in range(0, 3):
                for j in range(0, 3):
                    constraint.append(variables[3 * u + i][3 * v + j])

            solver.AddConstraint(solver.AllDifferent(constraint))

    db = solver.Phase(list(chain(*variables)), solver.INT_VAR_SIMPLE, solver.INT_VALUE_SIMPLE)
    solver.NewSearch(db)

    sol = [[None for i in range(n)] for j in range(n)]

    if solver.NextSolution():
        for i in range(n):
            for j in range(n):
                sol[i][j] = variables[i][j].Value()

    return sol
