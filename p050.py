import utils.eulerlib as utils


limit = 10**6-1

primes = utils.list_primes(limit)
primes_set = set(primes)

addends = []

for start_idx in range(len(primes)):
    for end_idx in range(start_idx, len(primes)-1):
        sub_list = primes[start_idx:end_idx]
        sub_sum = sum(sub_list)
        if sub_sum > limit:
            break
        if sub_sum not in primes_set:
            continue

        addends.append((sub_list, sub_sum))


max_len = 0
max_sum = None

# for a, b in addends:
#     print(f"{b} => {a}")

for sub_list, sub_sum in addends:
    if len(sub_list) > max_len:
        max_len = len(sub_list)
        max_sum = sub_sum

print(max_sum)
