a = [1, 1, 3, 4, 4, 6]
dct = {x: a.count(x) for x in a}
print([x[0] for x in dct.items() if x[1] > 1])
