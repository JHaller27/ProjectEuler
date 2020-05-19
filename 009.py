def main():
    a = 1
    while a < 999:
        b = 1
        while a + b < 1000:
            c = 1
            while a + b + c <= 1000:
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c
                c += 1
            b += 1
        a += 1


if __name__ == "__main__":
    a, b, c = main()
    print(f'{a} * {b} * {c} = {a*b*c}')
