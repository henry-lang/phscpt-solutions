n, v, e = map(int, input().split())
graph = [[]] * v
bread = map(int, input().split())
for i in range(e):
    first, second = map(lambda x: x - 1, map(int, input().split()))
    print(graph[first])
    graph[second].append(first)
print(graph)
