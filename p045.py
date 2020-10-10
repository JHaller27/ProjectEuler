import itertools


def T(n):
    return n*(n+1)//2

def P(n):
    return n*(3*n-1)//2

def H(n):
    return n*(2*n-1)

def main():
    P_outs = set()
    H_outs = set()

    # Prime sets
    for n in range(285+1):
        P_outs.add(P(n))
        H_outs.add(H(n))

    # Find solution
    for n in itertools.count(285+1):
        t = T(n)

        if t in H_outs and t in P_outs:
            return t

        P_outs.add(P(n))
        H_outs.add(H(n))


if __name__ == "__main__":
    ans = main()
    print(ans)
