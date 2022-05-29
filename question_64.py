
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.'''


class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self, speed):
        if self.speed == 0:
            self.speed = speed
            return f'Машина {self.name} поехала'
        else:
            speed_diff = speed - self.speed
            self.speed = speed
            if speed_diff > 0:
                return f'Машина {self.name} ускорилась на {speed_diff}'
            if speed_diff < 0:
                return f'Машина {self.name} замедлилась на {-speed_diff}'
        return f'Машина {self.name} уже едет с указанной скоростью'

    
    def stop(self):
        self.speed = 0
        return f'Машина {self.name} остановилась'


    def turn(self, direction):
        if self.speed != 0:
            return f'Машина {self.name} повернула {direction}'
        else:
            return f'Машина {self.name} стоит'


    def show_speed(self):
        return f'{self.name}: скорость {self.speed}'


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


    def show_speed(self):
        speed_limit = 60
        if self.speed <= speed_limit:
            return f'{self.name}: скорость {self.speed}'
        else:
            return f'{self.name}: скорость {self.speed}, превышение скорости на {self.speed - speed_limit}'


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


    def show_speed(self):
        speed_limit = 40
        if self.speed <= speed_limit:
            return f'{self.name}: скорость {self.speed}'
        else:
            return f'{self.name}: скорость {self.speed}, превышение скорости на {self.speed - speed_limit}'


if __name__ == '__main__':
    towncar = TownCar('red', 'Lexus SC300')
    policecar = PoliceCar('black', 'Ford Crown Victoria')
    sportcar = SportCar('white', 'Porsche 911GT')
    workcar = WorkCar('green', 'Dodge RAM')
    print(towncar.go(61))
    print(policecar.go(100))
    print(sportcar.go(120))
    print(workcar.go(39))
    print(towncar.show_speed())
    print(towncar.go(55))
    print(towncar.turn('налево'))
    print(towncar.show_speed())
    print(policecar.show_speed())
    print(policecar.stop())
    print(sportcar.turn('направо'))
    print(policecar.turn('направо'))
    print(workcar.go(39))
    print(workcar.show_speed())
