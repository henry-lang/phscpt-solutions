def getNth(c1, c2, c3, n):
    seq = [c1, c2, c3]
    if n <= 3:
        return seq[n - 1]
    for i in range(2, n - 1):
        seq.append(seq[i] + seq[i - 1] + seq[i - 2])
    return seq[-1] % (10**8 + 7)

if __name__ == "__main__":
    tests = int(input())
    for test in range(tests):
        arr = input().split(' ')
        c1 = int(arr[0])
        c2 = int(arr[1])
        c3 = int(arr[2])
        n = int(input())
        output = getNth(c1, c2, c3, n)
        print(output)
