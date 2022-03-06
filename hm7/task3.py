"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки
должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

from random import randint


class Cell:
    def __init__(self, core_num: int):
        self.core_num = core_num

    # не понял, должен ли быть новый объект или увеличиваться в старой клетке,
    # поэтому сделал новый
    def __add__(self, other):
        return Cell(self.core_num + other.core_num)
        # self.core_num -= other.core_num

    def __sub__(self, other):
        res = self.core_num - other.core_num
        if res > 0:
            self.core_num = res
        else:
            # raise ValueError("Cell number of first obj must be greater (obj_1.cell_num > obj_2.cell_num)")
            print("Cell number of first obj must be greater (obj_1.cell_num > obj_2.cell_num)")

    def __mul__(self, other):
        return Cell(self.core_num * other.core_num)

    def __truediv__(self, other):
        return Cell(self.core_num // other.core_num)

    def make_order(self, cores_in_raw):
        if cores_in_raw <= 0:
            raise ValueError(f'cores_in_raw must be above zero, but {cores_in_raw} was given')
        return f'{"*" * cores_in_raw}\n' * (self.core_num // cores_in_raw) + f'{"*" * (self.core_num % cores_in_raw)}\n'

    def __str__(self):
        return str(self.core_num)


def test(num_of_rep = 3):

    try:
        # Create random num of cell with random cores num
        cells = [Cell(randint(1, 25)) for i in range(randint(10, 20))]
        rep_counter: int

        for rep_counter in range(num_of_rep):
            # Choose two random cells
            cell_1_idx, cell_2_idx = randint(0, len(cells) - 1), randint(0, len(cells) - 1)
            cell_1, cell_2 = cells[cell_1_idx], cells[cell_2_idx]

            print(f'Start values for cells:\n{cell_1}, {cell_2}')
            print(f'add(): {cell_1 + cell_2}')
            cell_1 - cell_2
            print(f'sub(): {cell_1}')
            print(f'mul(): {cell_1 * cell_2}')
            print(f'div(): {cell_1 / cell_2}')

            sym_in_line = randint(0, 25)
            print(f'{sym_in_line} cores in a line:\n{cell_2.make_order(sym_in_line)}')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    test(10)
