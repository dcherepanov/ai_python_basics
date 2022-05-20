
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.'''


def user_info(name, surname, year_of_birth, current_city, email, phone_number):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year_of_birth}, Город проживания: {current_city}, Email: {email}, Телефон: {phone_number}')


user_info(name='Дмитрий', surname='Черепанов', year_of_birth=1996, current_city='Новосибирск', email='d.cherepanov@mymail.com', phone_number=89789488793)
