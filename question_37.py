
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.'''


def int_func(*args):
    return [item.capitalize() for item in args]


initial_str = input('String: ').split(' ')
print(*int_func(*initial_str))
