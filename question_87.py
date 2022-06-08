
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.'''


class Complex:
    def __init__(self, imaginary, real):
        self.imaginary = imaginary
        self.real = real
    

    def __add__(self, other):
        return Complex(self.imaginary + other.imaginary, self.real + other.real)


    def __mul__(self, other):
        return Complex(self.imaginary * other.real + self.real * other.imaginary, 
            self.real * other.real - self.imaginary * other.imaginary)


    def __abs__(self):
        return (self.imaginary**2 + self.real**2)**0.5


    def __str__(self):
        return f'{self.imaginary}i + {self.real}'


    def conjugate(self):
        return Complex(-self.imaginary, self.real)


    def __truediv__(self, other):
        return Complex((self.imaginary * other.real - self.real * other.imaginary) 
            / abs(other)**2, (self.real * other.real + self.imaginary * other.imaginary) 
            / abs(other)**2)


if __name__ == '__main__':
    a = Complex(4, 3)
    b = Complex(1, 2)
    print(f'a = {a}, b = {b}')
    print(f'|a| = {abs(a)}')
    print(f'a + b = {a + b}')
    print(f'a * b = {a * b}')
    print(f'a / b = {a / b}')
