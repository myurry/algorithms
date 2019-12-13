
with open('input.txt') as file:
    data_in = [int(file.readline().strip()) for x in range(int(file.readline().strip()))]
    a = data_in
    n = len(data_in)
    d = list(range(n))
    for i in range(n):
        d[i] = 1
        for j in range(1, i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(1, n):
        ans = max(ans, d[i])

    print(a)
    print(d)

