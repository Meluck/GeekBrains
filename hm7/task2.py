"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

import random


class Cloth:
    def __init__(self, cl_size: int, name: str):
        self.name = name
        self.cl_size = cl_size

    @property
    def fabric_consumption(self):
        pass

    def __eq__(self, other):
        return self.cl_size == other.cl_size and type(self) == type(other)

    def __hash__(self):
        return hash(self.name + str(self.cl_size))


class Coat(Cloth):
    def __init__(self, coat_size, name=''):
        super(Coat, self).__init__(coat_size, name)

    @property
    def fabric_consumption(self):
        return self.cl_size / 6.5 + 0.5

    def __str__(self):
        return f'Cloth type: Coat\nname: {self.name}\nsize: {self.cl_size}'

    def __repr__(self):
        return f'Cloth type: Coat\nname: {self.name}\nsize: {self.cl_size}'


class Costume(Cloth):
    def __init__(self, costume_size, name=''):
        super(Costume, self).__init__(costume_size, name)

    @property
    def fabric_consumption(self):
        return self.cl_size * 2 + 0.3

    def __str__(self):
        return f'Cloth type: Costume\nname: {self.name}\nsize: {self.cl_size}'

    def __repr__(self):
        return f'Cloth type: Costume\nname: {self.name}\nsize: {self.cl_size}'


class ClothFabrica:
    def __init__(self):
        super().__init__()
        """
        cloth_dict = {'Cloth_type': num}
        """
        self.__cloth_dict = {}

    def add_cloth(self, cloth_obj: Cloth, num = 1):
        if cloth_obj not in self.__cloth_dict.keys():
            self.__cloth_dict[cloth_obj] = num
        else:
            self.__cloth_dict[cloth_obj] += num

    @property
    def total_fabric_consumption(self):
        total_cons = 0
        for key, val in self.__cloth_dict.items():
            total_cons += key.fabric_consumption * val
        return total_cons

    def get_cloth_dict(self):
        return self.__cloth_dict


def gen_cloth():
    if random.random() > 0.5:
        return Costume(costume_size=random.randint(130, 200) / 100)
    else:
        return Coat(coat_size=random.randint(30, 60))


if __name__ == "__main__":

    fabrica = ClothFabrica()
    for i in range(20):
        fabrica.add_cloth(gen_cloth())

    print(fabrica.get_cloth_dict())
    print(f'{fabrica.total_fabric_consumption = }')


