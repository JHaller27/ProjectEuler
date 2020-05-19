def count_paths(size: int) -> int:
    size += 1

    grid = [[None] * size for _ in range(size)]
    grid[0][0] = 0
    for i in range(1, size):
        grid[i][0] = grid[0][i] = 1

    for row in range(1, size):
        for col in range(1, size):
            grid[row][col] = grid[row][col-1] + grid[row-1][col]

    return grid[-1][-1]


print(count_paths(20))
