
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.'''

from abc import ABC, abstractclassmethod, abstractmethod

class AbstractClothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass
    

class Coat(AbstractClothes):
    def __init__(self, size):
        self.size = size


    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(AbstractClothes):
    def __init__(self, height):
        self.height = height


    @property
    def fabric_consumption(self):
        return self.height * 2 + 0.3
        

if __name__ == '__main__':
    type_1 = Coat(52)
    type_2 = Suit(180)
    print(type_1.fabric_consumption)
    print(type_2.fabric_consumption)
