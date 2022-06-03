
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''


class Matrix:
    def __init__(self, data):
        n_columns = len(data[0])
        if type(data) is list:
            for line in data:
                if type(line) is not list:
                    raise ValueError('List cannot be converted to matrix. Inconsistent data type.')
                elif len(line) != n_columns:
                    raise ValueError('List cannot be converted to matrix. Inconsistent data shape.')
        else:
            raise ValueError('List cannot be converted to matrix. Data is not list.')
        self.__data = data
        self.__shape = len(data), n_columns
        

    def __str__(self):
        return '\n'.join(['|' + '\t'.join(map(str, line)) + '|' for line in self.__data])


    def __add__(self, other):
        if self.__shape[0] != other.__shape[0] or self.__shape[1] != other.__shape[1]:
            raise ValueError('Inconsistent matrix shapes.')
        return Matrix([[item_1 + item_2 for item_1, item_2 in zip(line_1, line_2)]
                    for line_1, line_2 in zip(self.__data, other.__data)])


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2000, 3], [4, 5, 6], [7, 80, 9]])
    matrix_2 = Matrix([[1, -2000, 3], [4, 5, 6], [7, -80, 9]])
    print(matrix_1, '\n')
    print(matrix_1 + matrix_2) 
