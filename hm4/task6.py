"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
"""

from sys import argv
from itertools import count, cycle

help_mes = f'This program has 2 modes:\n' \
           f'int: integer continues numbers generation\n' \
           f'rep: repeat of input sequence while number of' \
           f' elements less then n (20 default)\n' \
           f'Usage example:\n' \
           f'1) int 10 20\n' \
           f'2) rep 1,2,3,4,5 10'


def int_gen_iter(start_num: int, stop_num: int):
    for num in count(start_num):
        if num > stop_num:
            break
        print(f'{num}', end=' ')


def repeat_gen_iter(sequence: list, *args):
    arg, *tail = args
    stop_num = arg if arg is not None else 20
    for idx, el in enumerate(cycle(sequence)):
        print(el, end=' ')
        if idx >= stop_num - 1:
            break


if __name__ == "__main__":
    try:
        if len(argv) == 1:
            print(help_mes)
        else:
            mode = argv[1]
            if mode == 'int':
                if argv[2].isnumeric() and argv[3].isnumeric():
                    int_gen_iter(int(argv[2]), int(argv[3]))
                else:
                    print('Input error. Use -h to get more usage information')
            elif mode == 'rep':
                seq = argv[2].strip().split(sep=',')
                if len(argv) > 3 and argv[3].isnumeric():
                    repeat_gen_iter(seq, int(argv[3]))
                else:
                    repeat_gen_iter(seq)
            elif mode in ['-h', '-help']:
                print(help_mes)
    except Exception as ex:
        print(ex)


