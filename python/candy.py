n, k = map(int, input().split())
queries = []
best = 0
count = 0

for _ in range(k):
    a, b = map(int, input().split())
    queries.append((a, 1))
    queries.append((b, -1))

queries.sort(key=lambda x: (x[0], -x[1]))

for q in queries:
    count += q[1]
    best = max(best, count)

print(best)
