
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.'''

import time
import random


class TrafficLight:
    def __init__(self):
        self.__color = 'red' 


    def running(self, next_color):
        algorithm_dict = {'red': 'yellow', 'yellow': 'green', 'green': 'red'}
        if algorithm_dict[self.__color] == next_color:
            self.__color = next_color
            print('changed to', next_color)
        else:
            print('Wrong algorithm')
            exit()


if __name__ == '__main__':
    next_colors = ['yellow', 'green', 'red']
    pauses_dict = {'yellow': 7, 'green': 2, 'red': 8}
    trafficlight = TrafficLight()
    while True:
        for next_color in next_colors:
            time.sleep(pauses_dict[next_color])
            trafficlight.running(next_color)
        if random.randint(0, 1) == 1:
            next_colors[0], next_colors[1] = next_colors[1], next_colors[0]
