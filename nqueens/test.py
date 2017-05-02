from nqueens import solver
from nqueens.utils import attacking_pairs


def test():
    n = 10
    queens = solver.solve(n)
    assert len(set(queens)) == n
    assert attacking_pairs(queens) == 0
    print(queens)

    n = 2000
    queens = solver.solve(n)
    assert len(set(queens)) == n
    assert attacking_pairs(queens) == 0
    print(queens)
