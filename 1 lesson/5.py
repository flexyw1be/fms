
n = int(input())
a = []
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        a.append(x)
print(sorted(a)[::-1][0])