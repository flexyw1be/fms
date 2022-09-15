a, n = map(int, input().split())
s = 0
for i in range(n + 1):
    if i % 2 == 0:
        s += a ** i
    else:
        s -= a ** i
print(s)