"""
5. Реализовать класс Stationery (канцелярская принадлежность).

    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""

import os
from PIL import Image
import pytesseract
import io
import PIL

print('GeekBrains homework #6, task 5')


class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')  # логичнее просто pass, чтобы был интерфейсный класс


class Pen(Stationery):
    def __init__(self):
        super().__init__(title='pen')

    def draw(self):
        # say('Pen text', colors=['green', 'blue'], size=(100, 5), font='slick')
        os.system("image2ascii pen.png --color --quality 9")


class Pencil(Stationery):
    def __init__(self):
        super().__init__(title='pencil')

    def draw(self):
        # say('Pencil text', colors=['red', 'yellow'], size=(100, 5), font='grid')
        os.system("image2ascii pencil.png --color --quality 9")


class Handle(Stationery):
    def __init__(self):
        super().__init__(title='handle')

    def draw(self):
        # say('Handle text', colors=['green', 'blue'], size=(100, 5))
        os.system("image2ascii handle.png --color --quality 9")


if __name__ == '__main__':
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    pen.draw()
    print('\n\n\n')
    pencil.draw()
    print('\n\n\n')
    handle.draw()
