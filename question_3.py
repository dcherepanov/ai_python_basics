
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

str_number = input('Integer: ')
sum_ = int(str_number) + int(2 * str_number) + int(3 * str_number)
print(f'Sum: {sum_}')
