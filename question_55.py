
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

numbers = [1, 5, 10, 56, 70, 27, 68, 45, 12, 500, 7, 42, 54.2]
with open(r'file_for_5_question.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))
with open(r'file_for_5_question.txt', encoding='utf-8') as f:
    print(sum(map(float, f.read().split(' '))))
