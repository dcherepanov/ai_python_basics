
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. Создать программный файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных будет свидетельствовать
пустая строка.'''

str_list, string = [], None
while string != '':
    string = input('Enter the string (empty string to stop input): ')
    if string != '':
        str_list.append(string)
with open(r'file_for_1_question.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(str_list))
