a = [1, 3, 4, 5, 6, 3, 5, 6, 3, 6]
s = [i for i in range(len(a)) if a[i] == max(a)]
print(s[0], s[-1])
