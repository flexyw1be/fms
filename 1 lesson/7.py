n = input()
print(sum([int(n[x]) for x in range(len(n)) if x % 2 == 1]))
