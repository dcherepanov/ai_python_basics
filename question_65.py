
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.'''


class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    
    def draw(self):
        print('Запуск отрисовки маркером')


if __name__ == '__main__':
    all_instances = (Stationery('Тест'), Pen(), Pencil(), Handle())
    for instance in all_instances:
        instance.draw()
