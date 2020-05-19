from utils.decorators import *
from functools import reduce


RANK_MAP = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


# @debug()
def parse_hands(hand_str: str) -> (list, list):
    deal = list(map(lambda c: (RANK_MAP[c[0]], c[1]), hand_str.split(' ')))
    return deal[:5], deal[5:]


def is_flush(hand: list) -> bool:
    return len(set(map(lambda c: c[1], hand))) == 1


def is_straight(hand: list) -> bool:
    start = hand[0][0]
    for cidx in range(1, len(hand)):
        c = hand[cidx]
        if c[1] != start + cidx:
            return False

    return True


def find_key(d: dict, search = None, exclude = []) -> int:
    if callable(search):
        for key in d:
            if key not in exclude and search(key, d[key]):
                return key

        return None

    return search if search in d else None


# @debug(exclude=['kwargs'])
def fill_score(group: int, *args) -> int:
    val_max_count = 2
    assert len(args) <= val_max_count

    result = group

    for val in args:
        result *= 100
        result += val

    result *= 100**(val_max_count - len(args))

    return result


@debug(exclude=['kwargs'])
def get_group_score(hand: list) -> int:
    hand = sorted(hand, key=lambda c: c[0])

    if is_flush(hand):
        if is_straight(hand):
            # Royal flush - 9
            if hand[0][0] == RANK_MAP['T']:
                return fill_score(9)

            # Straight flush - 8
            return fill_score(8, hand[0][0])

        # Flush - 5
        return fill_score(5)

    # Straight - 4
    if is_straight(hand):
        return fill_score(4, hand[0][0])

    rank_buckets = {}
    for rank, suit in hand:
        if rank not in rank_buckets:
            rank_buckets[rank] = set()

        rank_buckets[rank].add(suit)

    fours_rank = find_key(rank_buckets, lambda k, v: len(v) == 4)

    # 4 kind - 7
    if fours_rank is not None:
        return fill_score(7, fours_rank)

    threes_rank = find_key(rank_buckets, lambda k, v: len(v) == 3)
    pairs_rank = find_key(rank_buckets, lambda k, v: len(v) == 2)

    if threes_rank is not None:
        # Full house - 6
        if pairs_rank is not None:
            return fill_score(6, threes_rank, pairs_rank)

        # 3 kind - 3
        return fill_score(3, threes_rank)

    # 2 pairs - 2
    if pairs_rank is not None:
        second_pairs_rank = find_key(rank_buckets, lambda k, v: len(v) == 2, [pairs_rank])
        if second_pairs_rank is not None:
            if pairs_rank >= second_pairs_rank:
                return fill_score(2, pairs_rank, second_pairs_rank)
            return fill_score(2, second_pairs_rank, pairs_rank)

        # 1 pair - 1
        return fill_score(1, pairs_rank)

    # High card - 0
    return fill_score(0, hand[-1][0])


def hands_from_file(fname: str) -> (list, list):
    with open(fname, 'r') as fin:
        for line in fin:
            yield parse_hands(line)


def get_rank_score(h1: list, h2: list) -> int:
    assert len(h1) == len(h2)

    for c1, c2 in zip(reversed(h1), reversed(h2)):
        r1, r2 = c1[0], c2[0]
        if r1 != r2:
            return r1 - r2


def player1_wins(h: (list, list)) -> bool:
    p1, p2 = h
    s1, s2 = get_group_score(p1), get_group_score(p2)

    if s1 > s2:
        return True
    elif s1 < s2:
        return False
    else:
        comp = get_rank_score(p1, p2)
        if comp > 0:
            return True
        elif comp < 0:
            return False
        else:
            print('Tie!')
            return False


if __name__ == '__main__':
    p1_wins = list(filter(player1_wins, hands_from_file('data/054.txt')))
    print(len(p1_wins))
