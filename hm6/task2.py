"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия
одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т. #FIXME очень странная формула. м^2*см*кг = кг ??? (даже не 12500, строго говоря)
"""


print('GeekBrains homework #6, task 2')


class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calc_mas(self, mas_per_meter: float, depth: float) -> float:
        return self._length * self._width * mas_per_meter * depth / 1000  # делим на 1000 для перевода в тонны


if __name__ == '__main__':
    road = Road(width=20, length=5000)
    print(f'{road.calc_mas(mas_per_meter=25, depth=5) = } ton')

