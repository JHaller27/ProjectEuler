import random


class Grid:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

        self._grid = [[None] * width for _ in range(height)]

    @classmethod
    def from_table(cls, table):
        grid = cls(len(table), len(table[0]))
        for r, row in enumerate(table):
            for c, val in enumerate(row):
                grid[r, c] = val

        return grid

    def __repr__(self) -> str:
        return '\n'.join([', '.join([val for val in row]) for row in self._grid])

    def __getitem__(self, c: (int, int)):
        x, y = c
        return self._grid[y][x]

    def __setitem__(self, c: (int, int), val: int):
        x, y = c
        self._grid[y][x] = val

    def copy(self) -> 'Grid':
        """
        Creates identical copy, including values
        """
        new_grid = Grid(self.height, self.width)
        for r in self.height_range():
            for c in self.width_range():
                new_grid[r, c] = self[r, c]

        return new_grid

    def clone(self) -> 'Grid':
        """
        Creates Grid of same size, without setting values
        """
        return Grid(self.height, self.width)

    def fill(self, val) -> None:
        for r in self.height_range():
            for c in self.width_range():
                self[r, c] = val

    def height_range(self) -> int:
        return range(self.height)

    def width_range(self) -> int:
        return range(self.width)


def file2grid(fname: str) -> Grid:
    with open(fname, 'r') as fin:
        table = [list(map(int, line.replace(' ', '').split(','))) for line in fin]

    return Grid.from_table(table)


def get_min_dist(grid: Grid, dist: Grid, r: int, c: int) -> int:
    values = []

    if r + 1 < grid.height:
        values.append(grid[r, c] + dist[r + 1, c])

    if c + 1 < grid.width:
        values.append(grid[r, c] + dist[r, c + 1])

    return grid[r, c] if len(values) == 0 else min(values)


def compute_min_weight(grid: Grid):
    dist = grid.clone()
    dist.fill(0)

    for ridx in reversed(grid.height_range()):
        for cidx in reversed(grid.width_range()):
            dist[ridx, cidx] = get_min_dist(grid, dist, ridx, cidx)

    return dist[0, 0]


if __name__ == '__main__':
    grid = file2grid('data/081.txt')

    print(compute_min_weight(grid))
