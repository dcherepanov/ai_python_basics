
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''

from functools import reduce

init_list = [i for i in range(100, 1001) if i % 2 == 0]
total_multiplication = reduce(lambda previous, current: previous * current, init_list)
print(total_multiplication)
