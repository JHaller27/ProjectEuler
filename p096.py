GRID_SIZE = 9


class Config:
    def is_goal(self) -> bool:
        raise NotImplementedError

    def get_children(self):
        raise NotImplementedError


class Backtracker_Strategy:
    def add(self, config: Config):
        raise NotImplementedError

    def has_next(self) -> bool:
        raise NotImplementedError

    def __next__(self) -> Config:
        raise NotImplementedError

    def __iter__(self):
        return self


class DFS_Strategy(Backtracker_Strategy):
    # Stack
    def __init__(self):
        self._stack = []

    def add(self, config: Config):
        self._stack.append(config)

    def has_next(self) -> bool:
        return len(self._stack) > 0

    def __next__(self):
        return self._stack.pop()


class BFS_Strategy(Backtracker_Strategy):
    # Queue
    def __init__(self):
        self._queue = []

    def add(self, config: Config):
        self._queue.append(config)

    def has_next(self) -> bool:
        return len(self._queue) > 0

    def __next__(self):
        return self._queue.pop(0)


class Backtracker:
    def __init__(self, strategy: Backtracker_Strategy, init_config: Config):
        self._configs = strategy
        self._configs.add(init_config)

    def _run_once(self):
        if not self._configs.has_next():
            return None

        config = next(self._configs)

        if config.is_goal():
            return config

        children = config.get_children()
        for c in children:
            self._configs.add(c)

        return None

    def run(self) -> Config:
        goal = self._run_once()
        while goal is None:
            goal = self._run_once()

        return goal


class SudokuConfig:
    def __init__(self, init_grid=None):
        if init_grid is None:
            init_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

        self._unsolved_vals = GRID_SIZE * GRID_SIZE

        # Create possibilities grid
        self._possibilities = [[set(range(1, GRID_SIZE + 1)) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        for ridx, row in enumerate(init_grid):
            for cidx, val in enumerate(row):
                if val != 0:
                    self.set_value(ridx, cidx, val)

    def __repr__(self) -> str:
        s = ''

        for ridx in range(GRID_SIZE):
            for cidx in range(GRID_SIZE):
                val = self._possibilities[ridx][cidx]
                if isinstance(val, set):
                    s += '0'
                elif isinstance(val, int):
                    s += str(val)
                else:
                    s += '?'
            s += '\n'

        return s.rstrip()

    @classmethod
    def from_list(cls, init_list: list):
        grid = [init_list[i * GRID_SIZE : (i + 1) * GRID_SIZE] for i in range(0, GRID_SIZE)]
        return cls(grid)

    def get(self, ridx, cidx):
        return self._possibilities[ridx][cidx]

    def set_value(self, ridx: int, cidx: int, val: int):
        if isinstance(self._possibilities[ridx][cidx], int) or self._unsolved_vals == 0:
            return

        self._possibilities[ridx][cidx] = val
        self._unsolved_vals -= 1

        self.set_impossible_around(ridx, cidx, val)

    def _set_one_impossible(self, ridx: int, cidx: int, val: int):
        if isinstance(self._possibilities[ridx][cidx], set):
            self._possibilities[ridx][cidx].discard(val)

            if len(self._possibilities[ridx][cidx]) == 0:
                raise ValueError(f'({ridx},{cidx}) has no possible values')

            elif len(self._possibilities[ridx][cidx]) == 1:
                self.set_value(ridx, cidx, self._possibilities[ridx][cidx].pop())

    def set_impossible_around(self, ridx: int, cidx: int, val: int):
        # Set impossible for row/col
        for i in range(GRID_SIZE):
            self._set_one_impossible(ridx, i, val)
            self._set_one_impossible(i, cidx, val)

        # Set impossible for block
        start_ridx = (ridx // 3) * 3
        start_cidx = (cidx // 3) * 3
        for br_idx in range(start_ridx, start_ridx + 3):
            for bc_idx in range(start_cidx, start_cidx + 3):
                self._set_one_impossible(br_idx, bc_idx, val)

    def is_goal(self) -> bool:
        return self._unsolved_vals == 0

    def copy(self):
        cp = SudokuConfig()
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                v = self._possibilities[r][c]
                if isinstance(v, set):
                    cp._possibilities[r][c] = v.copy()
                else:
                    cp._possibilities[r][c] = v

        cp._unsolved_vals = self._unsolved_vals

        return cp

    def get_children(self):
        # Find first unsolved location
        ridx, cidx = -1, -1
        for r, row in enumerate(self._possibilities):
            for c, val in enumerate(row):
                if isinstance(val, set):
                    for arbitrary_val in val:
                        child = self.copy()
                        child.set_value(r, c, arbitrary_val)
                        yield child
                    return


def read_grid(fp):
    grid = [fp.readline().rstrip() for _ in range(GRID_SIZE + 1)]

    if grid[0] == '':
        return None

    title = grid.pop(0)
    print(title)
    grid = [list(map(int, l)) for l in grid]

    return grid


def solve(sudoku: SudokuConfig):
    bt = Backtracker(DFS_Strategy(), sudoku)
    solution = bt.run()
    if solution is None:
        print('No solution! *insert Bernie scream*')

        return 0
    else:
        return solution.get(0, 0) * 100 + solution.get(0, 1) * 10 + solution.get(0, 2)


def main():
    total = 0
    with open('./data/096.txt', 'r') as fin:
        while True:
            raw_grid = read_grid(fin)

            if raw_grid is None:
                break

            grid = SudokuConfig(raw_grid)

            total += solve(grid)

    return total


if __name__ == "__main__":
    ans = main()
    print(ans)
