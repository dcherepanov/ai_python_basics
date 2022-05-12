
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

str_number = input('Integer: ')
max_number_while, i = 0, 0
# while
while i < len(str_number):
    if max_number_while < int(str_number[i]):
        max_number_while = int(str_number[i])
    i += 1
print(f'Max number: {max_number_while}')
max_number_for = 0
# for
for number in str_number:
    if max_number_for < int(number):
        max_number_for = int(number)
print(f'Max number: {max_number_for}')
# max
max_number = max(str_number)
print(f'Max number: {max_number}')
