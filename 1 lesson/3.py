n = int(input())
s, g = 12 ** 0.5, 0
for i in range(n + 1):
    a =  1 / (3 ** i * (i * 2 + 1))
    if i % 2 == 0:
        g += a
    else:
        g -= a
print(s * g)