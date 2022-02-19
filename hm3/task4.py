"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла."""

print('GeekBrains homework #3, task 4')


def my_pow(arg1, arg2):
    if arg2 >= 0:
        raise ValueError('arg2 must be negative integer')
    else:
        # positive pow
        pow_pos = abs(arg2)
        res = 1
        while pow_pos:
            res *= arg1
            pow_pos -= 1
        return 1/res


try:
    x_num = float(input('Enter x value\n'))
    y_num = int(input('Enter y value\n'))
    print(f'{my_pow(x_num, y_num) = }')
except Exception as ex:
    print(ex)

