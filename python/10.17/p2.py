def read_ints():
    return map(int, input().split())


num = int(input())
ints = read_ints()
k = int(input())
print(int(sum(ints) / k))
