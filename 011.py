def read(fname: str) -> list:
    with open(fname, 'r') as fin:
        grid = [list(map(int, line.split())) for line in fin]
    return grid


def get_max_sum(grid: list, start_row: int, start_col: int):
    final_product = 0
    for row_add in range(-1, 2):
        for col_add in range(-1, 2):
            if row_add == col_add == 0:
                continue

            row = start_row
            col = start_col

            product = 1

            for _ in range(4):
                product *= grid[row][col]
                row += row_add
                col += col_add

            final_product = max(final_product, product)

    return final_product


if __name__ == '__main__':
    grid = read('data/011.txt')
    print(max(get_max_sum(grid, row, col) for row in range(3, len(grid)-3) for col in range(3, len(grid[row])-3)))
