n, m = map(int, input().split())

baskets = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        baskets[x] = k

for i in range(n):
    print(baskets[i], end=' ')