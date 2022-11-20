from collections import deque

def read_ints():
    return map(int, input().split())

n, m = read_ints()
grid = []
for _ in range(n):
    grid.append(list(input()))

start = None
for (y, row) in enumerate(grid):
    for(x, char) in enumerate(row):
        if char == 'S':
            start = (y, x)

# bfs (pos, visited)
q = deque([(start, set([start]))])
while q:
    state = q.popleft()
    print(state)
    moves = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(4):
        move = state[0][:] # clone it
        while True:
            move = tuple(map(lambda x: x[0] + x[1], zip(move, dirs[i])))
            if move[0] < 0 or move[0] >= n or move[1] < 0 or move[1] >= m:
                break
            g = grid[move[0]][move[1]]
            if g == 'X':
                break
            if g == 'P':
                if move in state[1]:
                    break
                moves.append(move)
                break
            if g == 'G':
                print(len(state[1]) + 1)
                exit()
    for move in moves:
        new_visited = set(state[1])
        new_visited.add(state[0])
        q.append((move, new_visited))
print(-1)
