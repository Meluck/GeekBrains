"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, conf_data: list[list]):
        self.values = conf_data

    def __str__(self):
        # return ''.join([h_line for h_line in ''.join(self.values)])
        matrix_str = ''
        for h_line in self.values:
            for el in h_line:
                matrix_str += f'{str(el)} '
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        try:
            for idx_i, val in enumerate(self.values):
                for idx_j, _ in enumerate(val):
                    self.values[idx_i][idx_j] += other.values[idx_i][idx_j]
            return Matrix(self.values)
        except IndexError:
            print('Matrix values must be agree')
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    data = [[1, 2, 3], [4, 5, 6]]
    m = Matrix(data)
    print(m + m)