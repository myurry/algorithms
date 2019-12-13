n = 8

def fib(n):
    if n < 1:
        return -1
    f = [0, 1]
    for i in range(2, n+1):
        f.append(0)
        f[i] = f[i-2] + f[i-1]
    return f[n-1]

print(fib(n))