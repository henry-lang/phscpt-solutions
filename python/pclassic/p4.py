# Implement the following function
def monsterMash(arr, k):
    done = False
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append([arr[i], 1])
            continue
        if arr[i] == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([arr[i], 1])
        if stack[-1][1] == k:
            stack.pop()
    final = []
    for val, num in stack:
        for _ in range(num):
            final.append(val)
    return str(final)

# Do not modify below this line
tests = int(input().strip())
for test in range(tests):
    n = int(input().strip())
    arr = input().strip().split(' ')
    for i in range(n):
        arr[i] = int(arr[i])
    k = int(input().strip())
    print(monsterMash(arr, k))