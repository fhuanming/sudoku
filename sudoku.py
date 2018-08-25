def candidates(matrix, x, y):
    candidates = range(1, 10)
    already = set()
    for i in range(0, 9):
        already.add(matrix[x][i])
        already.add(matrix[i][y])

    cell_x = (x / 3) * 3
    cell_y = (y / 3) * 3
    for i in range(0, 3):
        for y in range(0, 3):
            already.add(matrix[cell_x + i][cell_y + y])

    candidates = [c for c in candidates if c not in already]
    return candidates


def next(x, y):
    if x == 8 & y == 8:
        return -1, -1
    if x == 8:
        return 0, y + 1
    return x + 1, y


def helper(matrix, x, y):
    if (x, y) == (-1, -1):
        print matrix
        return

    x_n, y_n = next(x, y)
    if matrix[x][y] != 0:
        return helper(matrix, x_n, y_n)

    candidates_list = candidates(matrix, x, y)
    for c in candidates_list:
        matrix[x][y] = c
        helper(matrix, x_n, y_n)
    matrix[x][y] = 0


def solve(matrix):
    helper(matrix, 0, 0)


def main():
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 1, 0, 0, 0, 9, 0, 0, 0],
        [0, 4, 0, 0, 2, 0, 0, 0, 0],
        [0, 9, 2, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 9, 1, 4, 6, 0, 0],
        [0, 0, 4, 0, 6, 8, 7, 0, 0],
        [0, 0, 0, 6, 7, 0, 4, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [8, 7, 0, 0, 3, 0, 9, 0, 0],
    ]
    solve(matrix)


if __name__ == '__main__':
    main()
