n = [int(x) for x in input()]
if max(n) < 5:
    print(int(''.join(map(str, n)), base=5))
else:
    print('Ошибка ввода')