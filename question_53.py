
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 3. Создать текстовый файл (не программно). Построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32'''

with open(r'file_for_3_question.txt', encoding='utf-8') as f:
    less_than_20000_names, sum_salary, n = [], 0, 0
    for line in f:
        name, salary = line.split(' ')
        salary_float = float(salary)
        if salary_float < 20000:
            less_than_20000_names.append(name)
        sum_salary += salary_float
        n += 1
    print('Оклад менее 20000:', ', '.join(less_than_20000_names))
    print(f'Средний оклад: {sum_salary / n}')
