
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 2. Создать текстовый файл (не программно), сохранить в нём несколько
строк, выполнить подсчёт строк и слов в каждой строке.'''

with open(r'file_for_2_question.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'Число строк: {len(lines)}')
    for i, line in enumerate(lines, 1):
        words_num = len(line.split(' '))
        print(f'Число слов в {i}-й строке: {words_num}')
