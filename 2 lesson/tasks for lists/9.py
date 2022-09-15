a = [x for x in range(10)]
s = 0
for i in range(1, len(a) - 1):
    if a[i - 1] + a[i + 1] < a[i]:
        s += 1
s += 1 if a[0] > a[1] else 0
s += 1 if a[-1] > a[-2] else 0
print(s)
