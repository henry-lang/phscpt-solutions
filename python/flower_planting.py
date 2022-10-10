n, m = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]

t.sort()

i = 0
c = 0

while c + t[i] <= m:
    c += t[i]
    i += 1
    if i == n:
        i = n
        break

print(i)