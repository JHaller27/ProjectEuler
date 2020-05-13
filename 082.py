from utils.a_star import *
from multiprocessing import Pool


class MatrixCell(Node):
    def __init__(self, pos: (int, int), val: int, size: (int, int), avg_val: int):
        super().__init__()

        self._pos = pos
        self._val = val
        self._neighbors = list()
        self._num_rows = size[0]
        self._num_cols = size[1]

        self._avg_val = avg_val

    def __repr__(self) -> str:
        return f'({self._pos[0]}, {self._pos[1]} -> {self._val} / {super().__repr__()})'

    def add_neighbor(self, neighbor):
        self._neighbors.append(neighbor)

    def matches_goal(self, goal) -> bool:
        return self._pos[1] == self._num_cols - 1

    # h is the heuristic function. h() estimates the cost to reach goal from this node.
    def h(self) -> int:
        return (self._num_cols - self._pos[1]) * self._avg_val

    def get_neighbors(self):
        return self._neighbors

    def dist_to(self, other: 'MatrixCell'):
        return other._val

    def get_val(self) -> int:
        return self._val


def get_starts(init: list) -> list:
    num_rows = len(init)
    num_cols = len(init[0])

    avg_val = sum(sum(row) for row in init) // (num_rows * num_cols)

    # Convert primitives to Cells, but do not link yet
    matrix = [[MatrixCell((ridx, cidx), val, (num_rows, num_cols), avg_val) for cidx, val in enumerate(row)] for ridx, row in enumerate(init)]

    # Link neighbors to Cells (first row should only allow moving East)
    for ridx, row in enumerate(matrix):
        for cidx, cell in enumerate(row):
            # North
            if 0 <= ridx - 1 and cidx != 0:
                matrix[ridx][cidx].add_neighbor(matrix[ridx - 1][cidx])

            # East
            if cidx + 1 < num_cols:
                matrix[ridx][cidx].add_neighbor(matrix[ridx][cidx + 1])

            # South
            if ridx + 1 < num_rows and cidx != 0:
                matrix[ridx][cidx].add_neighbor(matrix[ridx + 1][cidx])

    # Return first Cell in each row
    return [row[0] for row in matrix]


init = []
with open('matrix.txt', 'r') as fin:
    for line in fin:
        init.append(list(map(int, line.split(','))))

if __name__ == '__main__':
    starts = get_starts(init)

    for start in starts:
        path = a_star(start, None)
        path_sum = sum(map(lambda mc: mc.get_val(), path))

        print(path)
        print(path_sum)
        print()
