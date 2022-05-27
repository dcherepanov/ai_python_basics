
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.'''

with open(r'file_for_4_question.txt', encoding='utf-8') as f:
    translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open(r'file_out_for_4_question.txt', 'w', encoding='utf-8') as f_out:
        f_out.writelines([' - '.join([translator[word], number]) for word, number in 
            map(lambda s: s.split(' - '), f)])