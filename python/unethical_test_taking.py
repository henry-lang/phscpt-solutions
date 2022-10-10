from collections import defaultdict

n, m = [int(x) for x in input().split()]
k = int(input()) 

c = defaultdict(lambda: []) # connections (graph)
p = set() # currently processing
g = {}

for i in range(k):
    a, b = [int(x) for x in input().split()]
    if b not in c[a]:
        c[a].append(b)

def bfs(a):
    # if we are currently processing or have graded student then exit early
    if a in p:
        return
    
    # add student to currently processing list
    p.add(a)

    s = 0
    # if student is competent then add one
    if a <= n:
        s += 1
    
    for b in c[a]:
        # if we've processed them then add their score to ours
        # if not process them
        if b not in p:
            s += bfs(b)

    return s

# traverse everyone
for a in list(c):
    g[a] = bfs(a)
    p.clear()

print(max(g.values()))
