
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''

list_ = [1, 2.1, 'str', '9']
for item in list_:
    print(type(item))
