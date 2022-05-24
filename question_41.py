
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.'''

from sys import argv

try:
    hours, rate_per_hour, bonus = map(float, argv[1:])
    print(f'Зарплата сотрудника: {hours * rate_per_hour + bonus}')
except ValueError:
    print('Ошибка: Некорректные данные')
