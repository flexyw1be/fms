from datetime import datetime


def first(n):
    m = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
    k = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    while n > k[i]:
        n -= k[i]
        i += 1

    return m[i]


def second():
    k = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    today = datetime.today()
    return sum(k[:today.month - 1]) + today.day


def third(n):
    sum = n - second()
    if sum == 0:
        return 'Этот день сегодня'
    elif sum < 0:
        return f'Этот день был {sum} дней назад'
    return f'Этот день будет через {sum} дней'


def fourth(x):
    n = int(x[-2:])
    if n // 10 == 1 or n % 10 == 0 or n % 10 in [5, 6, 7, 8, 9]:
        return f'Прошло {x} дней'
    elif n % 10 == 1:
        return f'Прошел {x} день'
    return f'Прошло {x} дня'


print(first(int(input('Введите день> '))))
print(second())
print(third(int(input('Введите день> '))))
print(fourth(input('Введите число> ')))
