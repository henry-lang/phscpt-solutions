from collections import deque, defaultdict, OrderedDict

def pathExists(w: int, h: int, portalArr: list[tuple[int]]):
    portals = defaultdict(dict)
    colors = defaultdict(list)
    for p in portalArr:
        portals[p[1]][p[0]] = p[2]
        colors[p[2]].append((p[0], p[1]))



    q = deque([(0, 0, set())]) # x, y, portals used
    while q:
        state = q.popleft()
        if state[1] == h - 1:
            return True
        for x, color in portals[state[1]].items():
            if not (x, state[1]) in state[2] and state[0] < x:
                #visit
                new_visited = set(state[2])
                new_visited.add((x, state[1]))
                q.append((x, state[1], new_visited))
                for other in colors[color]:
                    if (other[0], other[1]) != (x, state[0]) and (other[0], other[1]) not in state[2]:
                        if other[1] == h - 1:
                            return True
                        q.append((other[0], other[1], set(new_visited)))

    return False
    
# Do not modify below this line
if __name__ == "__main__":
    tests = int(input())
    for test in range(tests):
        line = input().split()
        w = int(line[0])
        h = int(line[1])
        n = int(input())
        portalArr = []
        for _ in range(n):
            tupline = input().split()
            currTuple = tuple([int(tupline[0]), int(tupline[1]), int(tupline[2])])
            portalArr.append(currTuple)
        output = pathExists(w, h, portalArr)
        print("true" if output else "false")