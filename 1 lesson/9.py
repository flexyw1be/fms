n = input()
a = [int(n[x]) for x in range(len(n))]
print(a.count(max(a)))
