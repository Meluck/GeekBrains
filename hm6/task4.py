"""
4. Реализуйте базовый класс Car.

    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

"""


print('GeekBrains homework #6, task 4')


class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if speed > 0:
            self.__is_moving = True
        else:
            self.__is_moving = False

    def go(self):
        if not self.__is_moving:
            self.__is_moving = True
            self.speed = 10
            print('Start moving')
        else:
            print('Already moving')

    def stop(self):
        if self.__is_moving:
            self.__is_moving = False
            self.speed = 0
            print('Stop moving')
        else:
            print('Already stopped')

    def turn(self, direction):
        print(f'Turned {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'speed = {self.speed}')
        if self.speed > 60:
            print('Over speed')


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'speed = {self.speed}')
        if self.speed > 40:
            print('Over speed')


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, is_police=True)


def test(car_obj: Car):
    print(f'{car_obj.name}, {car_obj.speed}, {car_obj.color}, {"police" if car_obj.is_police else ""}')
    car_obj.show_speed()
    car_obj.go()
    car_obj.show_speed()
    car_obj.stop()
    car_obj.show_speed()
    car_obj.stop()
    car_obj.go()
    car_obj.show_speed()
    car_obj.speed = 55
    car_obj.show_speed()
    car_obj.speed = 65
    car_obj.show_speed()
    car_obj.turn('left')
    car_obj.turn('right')


if __name__ == '__main__':
    t_car = TownCar(speed=50, color='red', name='mazda')
    s_car = SportCar(speed=100, color='blue', name='ford')
    w_car = WorkCar(speed=20, color='orange', name='UAZ')
    p_car = PoliceCar(speed=77, color='black and white', name='BMW')

    cars = [t_car, s_car, w_car, p_car]

    for car in cars:
        test(car)
        print('='*15)


""" Program output:

GeekBrains homework #6, task 4
mazda, 50, red, 
speed = 50
Already moving
speed = 50
Stop moving
speed = 0
Already stopped
Start moving
speed = 10
speed = 55
speed = 65
Over speed
Turned left
Turned right
===============
ford, 100, blue, 
100
Already moving
100
Stop moving
0
Already stopped
Start moving
10
55
65
Turned left
Turned right
===============
UAZ, 20, orange, 
speed = 20
Already moving
speed = 20
Stop moving
speed = 0
Already stopped
Start moving
speed = 10
speed = 55
Over speed
speed = 65
Over speed
Turned left
Turned right
===============
BMW, 77, black and white, police
77
Already moving
77
Stop moving
0
Already stopped
Start moving
10
55
65
Turned left
Turned right
===============

Process finished with exit code 0
"""