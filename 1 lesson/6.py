from random import randint as r

a = r(1, 10)
i = 1
while True:
    b = int(input('Введите число > '))
    if a == b:
        print('Угадал! Kоличество попыток:', i)
        break
    elif a < b:
        print('Мое число меньше')
    else:
        print('Мое число больше')
    i += 1