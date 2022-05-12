
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

int_number = int(input('Integer: '))
max_number, i = 0, 0
while int_number > 0:
    last = int_number % 10
    int_number = int_number // 10
    if max_number < last:
        max_number = last
print(f'Max number: {max_number}')
