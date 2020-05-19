def read(fname: str) -> list:
    with open(fname, 'r') as fin:
        return [list(map(int, line.strip().split())) for line in fin]


def main():
    TREE = read('data/018.txt')
    SUM_TREE = [[0] * (i+1) for i in range(len(TREE))]
    SUM_TREE[0][0] = TREE[0][0]

    for ridx in range(1, len(TREE)):
        row = TREE[ridx]

        SUM_TREE[ridx][0] = TREE[ridx][0] + SUM_TREE[ridx-1][0]
        for cidx in range(1, len(row)-1):
            SUM_TREE[ridx][cidx] = TREE[ridx][cidx] + max(SUM_TREE[ridx-1][cidx-1], SUM_TREE[ridx-1][cidx])
        SUM_TREE[ridx][-1] = TREE[ridx][-1] + SUM_TREE[ridx-1][-1]

    return max(SUM_TREE[-1])


if __name__ == '__main__':
    print(main())
