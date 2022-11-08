def fac(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


n = int(input())

print(str(fac(n))[-2:] if n < 10 else "00")
