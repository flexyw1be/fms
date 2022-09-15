s, i, a = 0, 0, 1
while s <= 3.1945280494:
    s += 2 ** i / a
    a *= (i + 2)
    i += 1
print(i - 1)

