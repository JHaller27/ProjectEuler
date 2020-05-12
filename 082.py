from utils.backtracker import *
from multiprocessing import Pool


class Matrix(Configuration):
    EAST = 0
    NORTH = 1
    SOUTH = 2

    def __init__(self, init, row, col, _total = 0, _last = EAST):
        super().__init__()

        self._grid = init
        self._row_count = len(self._grid)
        self._col_count = len(self._grid[0])

        self._row = row
        self._col = col
        self._total = _total + self._grid[self._row][self._col]

        self._last = _last

    def __str__(self) -> str:
        lines = []

        for ridx, row in enumerate(self._grid):
            cells = []
            for cidx, val in enumerate(row):
                fmt = '({})' if ridx == self._row and cidx == self._col else ' {} '
                fmt = fmt.format('{:>3}')
                cells.append(fmt.format(val))
            lines.append(' '.join(cells))

        width = max(map(lambda l: len(l), lines))
        lines = ['-' * width] + lines + ['-' * width]

        return '\n'.join(lines)

    def get_sum(self) -> int:
        return self._total

    def get_children(self) -> list:
        children = []

        child_pos_lst = []

        child_pos_lst.append((self._row, self._col+1, Matrix.EAST))  # East
        if self._last != Matrix.SOUTH:
            child_pos_lst.append((self._row-1, self._col, Matrix.NORTH))  # North
        if self._last != Matrix.NORTH:
            child_pos_lst.append((self._row+1, self._col, Matrix.SOUTH))  # South

        for pos in child_pos_lst:
            row, col, last = pos
            if 0 <= row < self._row_count and 0 <= col < self._col_count:
                child = Matrix(self._grid, row, col, self._total, last)
                children.append(child)

        return children

    def is_valid(self) -> bool:
        return True

    def is_goal(self) -> bool:
        return self._col == self._col_count - 1


def get_min_path(start_row: int) -> int:
    global init

    backtracker = Backtracker()
    matrix = Matrix(init, start_row, 0)
    solutions = backtracker.run(matrix, Backtracker.DFS, goal_halts=False)

    return min(map(lambda s: s.get_sum(), solutions))


init = []
with open('matrix.txt', 'r') as fin:
    for line in fin:
        init.append(list(map(int, line.split(','))))

if __name__ == '__main__':
    min_paths = []
    with Pool(4) as pool:
        min_path = pool.map(get_min_path, range(len(init)))
        min_paths.append(min_path)

    print(min(min_paths))
