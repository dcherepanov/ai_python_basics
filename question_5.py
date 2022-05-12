
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчёте на одного сотрудника.'''

revenue = float(input('Revenue: '))
cost = float(input('Cost: '))
if revenue >= cost:
    profit = (revenue - cost) / revenue
    print(f'Profit: {profit}')
    number_of_employees = int(input('Number of employees: '))
    profit_on_employee = profit / number_of_employees
    print(f'Profit on employee: {profit_on_employee}')
else:
    print('Loss')
