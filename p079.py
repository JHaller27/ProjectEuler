import itertools


def read_file(fname):
    with open(fname, 'r') as fin:
        lines = list(map(lambda l: l.strip(), fin))

    return lines


def obeys_rules(ordering, rules):
    try:
        for rule in rules:
            start = 0
            for rchr in rule:
                start = ordering.index(rchr, start)
        return True
    except ValueError:
        return False


def main():
    rules = read_file('./data/079.txt')
    digits = set(''.join(rules))
    for ordering in itertools.permutations(digits, len(digits)):
        ordering = ''.join(ordering)
        if obeys_rules(ordering, rules):
            return ordering

    return None


if __name__ == '__main__':
    ans = main()
    print(ans)
