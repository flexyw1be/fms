a = [x for x in range(10)]
a[a.index(max(a))], a[a.index(min(a))] = min(a), max(a)
print(a)
