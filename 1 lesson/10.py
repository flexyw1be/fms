n = input()
a = [int(n[x]) for x in range(len(n))]
print(*[i + 1 for i in range(len(a)) if a[i] == min(a)], sep=', ')
