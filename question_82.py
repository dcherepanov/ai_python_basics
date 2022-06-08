
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.txt = text


if __name__ == '__main__':
    try:
        a, b = 1, 0
        if b == 0:
            raise MyZeroDivisionError('My Zero Division Error')
        c = a / b
    except Exception as e:
        print(e)
