a = [int(x) for x in input().split()]
cnt = 0
cnt += 1 if a[0] < a[1] else 0
cnt += 1 if a[-1] < a[-2] else 0
for i in range(1, len(a) - 1):
    if a[i - 1] > a[i] and a[i + 1] > a[i]:
        cnt += 1
print(cnt)
