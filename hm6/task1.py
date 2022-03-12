"""
1. Создать класс TrafficLight (светофор).

    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
import sys

print('GeekBrains homework #6, task 1')


def print_red(text: str):
    sys.stdout.write(f'\r\033[31m{text}')
    sys.stdout.flush()


def print_yellow(text: str):
    sys.stdout.write(f'\r\033[33m{text}')
    sys.stdout.flush()


def print_green(text: str):
    sys.stdout.write(f'\r\033[32m{text}')
    sys.stdout.flush()


class TrafficLight:
    def __init__(self):
        pass
        self.__color = 'GREEN'
        self.__color_queue = ('RED', 'YELLOW', 'GREEN')
        self.__color_print = {'RED': (print_red, 7),
                              'YELLOW': (print_yellow, 2),
                              'GREEN': (print_green, 5)}

    def running(self,  color=None):
        try:
            if color:
                # контроль очередности
                if ((self.__color_queue.index(color.upper()) - 1) % 3) == self.__color_queue.index(self.__color):
                    self.__color = color.upper()
                else:
                    print('\nНеверный порядок')
                    return
            else:
                self.__color = self.__color_queue[(self.__color_queue.index(self.__color) + 1) % 3]

            func, delay = self.__color_print[self.__color]
            func(f'● - {self.__color}')
            time.sleep(delay)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    # Usage example:
    traff = TrafficLight()
    for i in range(5):
        traff.running()

    print('\nПример контроля порядка:')
    traff.running('red')
    traff.running('yellow')
    traff.running('green')
    traff.running('green')

