a = [1, 2, 3, 2]
if len(a) % 2 == 0:
    print('yes' if a[:len(a) // 2] == a[len(a) // 2:][::-1] else 'no')
else:
    print('yes' if a[:len(a) // 2] == a[len(a) // 2 + 1:][::-1] else 'no')
