a = [x for x in range(100)]
print(min([a[i] for i in range(len(a)) if i % 2 != 0]))
