def get_names(fname: str) -> list:
    with open(fname, 'r') as fin:
        return fin.read().replace('"', '').split(',')


def score(name: str, line_num: int) -> int:
    return line_num * sum(map(lambda c: ord(c) - ord('A') + 1, name))


def main(names: list):
    return sum(score(name, idx + 1) for idx, name in enumerate(sorted(names)))


if __name__ == '__main__':
    print(main(get_names('data/022.txt')))
