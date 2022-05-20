
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.'''


def divide(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        print('Zero division error')


dividend = float(input('Dividend: '))
divider = float(input('Divider: '))
result = divide(dividend, divider)
if result != None:
    print(result)
