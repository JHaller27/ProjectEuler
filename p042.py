import itertools


def t(n: int) -> int:
    return (n*(n+1))//2


def word_value(word: str) -> int:
    return sum(map(lambda c: ord(c) - ord('A') + 1, word))


def get_words(fname: str) -> list:
    with open(fname, 'r') as fin:
        line = fin.readline().strip()

    return line.replace('"', '').split(',')


def main():
    words = get_words('data/042.txt')
    max_word_len = len(max(words, key=len))
    max_t = t(word_value('Z' * max_word_len))
    t_vals = set(itertools.takewhile(lambda v: v < max_t, map(t, itertools.count(1))))

    for w in words:
        print(f'[{w}] => {word_value(w)}')

    return len(list(filter(lambda w: word_value(w) in t_vals, words)))


if __name__ == '__main__':
    ans = main()
    print(ans)
