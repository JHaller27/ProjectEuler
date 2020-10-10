def main():
    MAX_SUM = 200

    ways = [1] + [0] * MAX_SUM
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for sub_sum in range(coin, len(ways)):
            ways[sub_sum] += ways[sub_sum - coin]

    return ways[-1]


if __name__ == "__main__":
    ans = main()
    print(ans)
