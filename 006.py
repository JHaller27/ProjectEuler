LIMIT = 100

print(sum(range(1, LIMIT+1))**2 - sum(i**2 for i in range(1, LIMIT+1)))
