
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.'''

#через list:
seasons_list = ['зима', 'весна', 'лето', 'осень']
month_number = int(input('Month number: '))
print(seasons_list[month_number % 12 // 3])
#через dict:
seasons_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for key in seasons_dict:
    if month_number in seasons_dict[key]:
        print(key)
