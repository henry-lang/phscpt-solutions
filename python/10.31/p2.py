n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
d = {}
for (i, pu) in enumerate(sorted(p)):
    if pu not in d:
        d[pu] = i

for pu in p:
    print(d[pu])
