from collections import Counter


def attacking_pairs(queens):
    columns = Counter()
    lrDiagonals = Counter()
    rlDiagonals = Counter()

    total = 0

    for (row, col) in enumerate(queens):
        total += columns[col]
        total += lrDiagonals[row + col]
        total += rlDiagonals[row - col]

        columns[col] += 1
        lrDiagonals[row + col] += 1
        rlDiagonals[row - col] += 1

    return total