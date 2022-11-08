from sys import prefix


n, m = map(int, input().split())
subjects = input().split()
psum = [0] * (len(subjects))
queries = []
psum[0] = 1 if subjects[0] == "prefixsums" else 0
for i in range(1, len(subjects)):
    psum[i] = psum[i - 1] + (1 if subjects[i] == "prefixsums" else 0)
psum.insert(0, 0)
for _ in range(m):
    a, b = map(lambda x: int(x), input().split())
    queries.append(psum[b] - psum[a - 1])
print("\n".join(map(str, queries)))
