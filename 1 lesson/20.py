a = list(map(int, input().split()))
d = [0 for i in range(len(a))]
for i in range(1, len(a) - 1):
    d[i] = a[i - 1] + a[i + 1]
d[0] = a[1] + a[-1]
d[-1] = a[0] + a[-2]
print(*d)