def fibonacci(limit: int) -> int:
    a, b = 1, 1
    yield a
    yield b
    while (c := a+b) < limit:
        yield c
        a, b = b, c


if __name__ == '__main__':
    s =  sum(f for f in filter(lambda e: e % 2 == 0, fibonacci(4*10**6)))
    print(s)

