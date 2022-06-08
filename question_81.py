
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.'''


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.is_date(self)


    @classmethod
    def date_to_num(cls, date):
        return Date(*map(int, date.split('-')))


    @staticmethod
    def is_date(obj):
        day_error_fstr = 'Error: for month {} and year {} day can be from 1 to {}'
        if obj.month > 0 and obj.month <= 12:
            if obj.month != 2:
                if obj.month in (1, 3, 5, 7, 8, 10, 12):
                    if obj.day <= 0 or obj.day > 31:
                        raise ValueError(
                            day_error_fstr.format(obj.month, obj.year, 31))
                else:
                    if obj.day <= 0 or obj.day > 30: 
                        raise ValueError(
                            day_error_fstr.format(obj.month, obj.year, 30))
            else:
                if obj.year % 4 == 0 or obj.year % 100 == 0 and obj.year % 400 == 0:
                    if obj.day <= 0 or obj.day > 29:
                        raise ValueError(
                            day_error_fstr.format(obj.month, obj.year, 29))
                else:
                    if obj.day <= 0 or obj.day > 28:
                        raise ValueError(
                            day_error_fstr.format(obj.month, obj.year, 28))
        else:
            raise ValueError('Error: month can be from 1 to 12')


if __name__ == '__main__':
    dates = ['21-01-1999', '32-03-2000', '29-02-2020', '29-02-2021', 
        '28-02-2022', '08-14-2000', '30-02-2000', '31-04-2000', '32-08-2001']
    for date in dates:
        try:
            print(date)
            d = Date.date_to_num(date)
            print('OK')
        except Exception as e:
            print(e)
