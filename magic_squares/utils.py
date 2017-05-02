from collections import Counter
from itertools import chain


def expected_sum(n):
    return n * (n ** 2 + 1) // 2


def is_valid(grid):
    n = len(grid)
    exp_sum = expected_sum(n)

    for x in chain(*grid):
        if x < 0 or x > exp_sum:
            return False

    return True


def is_correct(grid):
    n = len(grid)
    exp_sum = expected_sum(n)

    counter = Counter()

    for i in range(n):
        s1 = sum(grid[i][j] for j in range(n))
        s2 = sum(grid[j][i] for j in range(n))

        if s1 != exp_sum or s2 != exp_sum:
            return False

        for x in grid[i]:
            counter[x] += 1

    s1 = sum([grid[i][i] for i in range(n)])
    s2 = sum([grid[i][n - i - 1] for i in range(n)])

    if s1 != exp_sum or s2 != exp_sum:
        return False

    for e in range(1, n * n + 1):
        if counter[e] != 1:
            return False

    return True
