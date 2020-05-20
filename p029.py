LIMIT = 100

print(len(sorted(list(set(a**b
    for a in range(2, LIMIT+1)
    for b in range(2, LIMIT+1)
)))))

