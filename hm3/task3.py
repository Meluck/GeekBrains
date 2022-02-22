"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.

"""

print('GeekBrains homework #3, task 3')


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


try:
    num1, num2, *check_num, num3 = [float(sym) for sym in input('Введите 3 числа через пробел\n').split()]
    if check_num:
        print('Input error')
    else:
        print(my_func(num1, num2, num3))
except Exception as ex:
    print(ex)