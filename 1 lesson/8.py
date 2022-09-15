n = input()
a = [int(n[x]) for x in range(len(n))]
print('Максимум:', max(a), 'Среднее:', sum(a)/ len(a))