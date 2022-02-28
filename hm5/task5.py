"""
5. Создать (программно) текстовый файл,
 записать в него программно набор чисел, разделённых пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


from random import random, randrange


def create_numeric_file(out_file_name, num_of_el):
    num_str_lst = [str(randrange(0, 1000) / 100) for i in range(num_of_el)]
    num_str = ' '.join(num_str_lst)
    with open(out_file_name, 'w+') as out_file:
        out_file.write(num_str)


def calc_sum(in_file_name):
    with open(in_file_name) as input_file:
        lines = input_file.readlines()
        total_sum = 0
        for line in lines:
            total_sum += sum([float(sym) for sym in line.split()])
        return  total_sum


if __name__ == '__main__':
    file_name = 'task5_output'
    create_numeric_file(file_name, 50)
    print(f'Sum of numbers: {calc_sum(file_name)}')

