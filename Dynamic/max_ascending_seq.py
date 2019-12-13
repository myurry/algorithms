a = [1, 2, 3, 1, 5, 7, 8, 2, 3, 4] # Example of a row
n = len(a)
d = [] # Row holding max sequence for every digit in "a"

for i in range(n):
    d.append(1)
    for j in range(1, i):
        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
ans = 0
for i in range(1, n):
    ans = max(ans, d[i])

print(a)
print(d)
print(max(d))
