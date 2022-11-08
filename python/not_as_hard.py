a, b = map(int, input().split())
print(2 if a != b else next(filter(lambda x: a % x == 0, range(2, a + 1))))