def check_solution(grid):
    """
    :param grid: completed sudoku grid
    :return: true if grid is correctly filled in or false otherwise
    """
    rows = [[] for _ in range(0, 9)]
    cols = [[] for _ in range(0, 9)]

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            rows[i].append(val)
            cols[j].append(val)

            # wrong value in current cell
            if val < 1 or val > 9:
                return False

    # test for number of digits in each row and column
    for i in range(0, 9):
        if len(set(rows[i])) != 9 or len(set(cols[i])) != 9:
            return False

    # test for number of digits in each 3x3 square
    for k in range(1, 10):
        for u in range(0, 3):
            for v in range(0, 3):
                square = set()
                for i in range(1, 4):
                    for j in range(1, 4):
                        square.add(grid[3 * u + i - 1][3 * v + j - 1])

                if len(square) != 9:
                    return False

    return True