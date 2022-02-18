"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

print('GeekBrains homework #3, task 1')


def div(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError as zde:
        print(f'div: {zde}')


num1, *check_num, num2 = [float(sym) for sym in input('Введите 2 числа через пробел\n').split()]
if check_num:
    print('Input error')
else:
    print(f'Division result: {div(num1, num2)}')
