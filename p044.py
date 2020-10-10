import itertools


def P(n):
    return n * (3 * n - 1) >> 1


class Pentagon:
    def __init__(self):
        self._val_list = []
        self._val_set = set()


    def get_value(self, n):
        while n >= len(self._val_list):
            val = P(len(self._val_list))
            self._val_list.append(val)
            self._val_set.add(val)

        return self._val_list[n]

    def is_value(self, v):
        while v > self._val_list[-1]:
            val = P(len(self._val_list))
            self._val_list.append(val)
            self._val_set.add(val)

        return v in self._val_set


def main():
    the_pentagon = Pentagon()
    min_d = None

    for j in itertools.count(2):
        val_j = the_pentagon.get_value(j)

        # If next smallest difference is at least as large as min_d, stop searching
        #   next smallest difference = P(j) - P(j-1)
        if min_d is not None and val_j - the_pentagon.get_value(val_j - 1):
            break

        for k in range(j - 1, 0, -1):
            val_k = the_pentagon.get_value(k)
            dif = val_j - val_k

            # If difference is at least as large as min_d, stop searching
            if min_d is not None and dif >= min_d:
                break

            elif the_pentagon.is_value(val_j + val_k) and the_pentagon.is_value(dif):
                min_d = dif

    return min_d


if __name__ == '__main__':
    ans = main()
    print(ans)
