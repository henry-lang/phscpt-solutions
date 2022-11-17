from collections import defaultdict, deque

def read_ints():
    return map(int, input().split())

n, v, e = read_ints()
bread = list(read_ints())
graph = defaultdict(list)

# adj list
for _ in range(e):
    a, b = map(lambda x: x - 1, read_ints())
    if a == b:
        continue
    graph[a].append(b)
    graph[b].append(a)

# bfs (pos, bread, visited)
q = deque([(0, 0, set([0]))])

while q:
    state = q.popleft()
    for other in graph[state[0]]:
        if state[1] >= n:
            print(len(state[2]))
            exit()
        if other not in state[2]:
            new_state = set(state[2])
            new_state.add(state[0])

            q.append((other, state[1] + bread[other], new_state))

print(-1)
