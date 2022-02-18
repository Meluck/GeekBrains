# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print('GeekBrains homework #2, task 1')

multi_lst = ['123', [123], 123, 123.0, {123: 123}, (123, 123)]

for el in multi_lst:
    print(type(el))

for el in multi_lst:
    if type(el) is str:
        print('string')
    elif type(el) is int:
        print('integer')
    elif type(el) is list:
        print('list')
    elif type(el) is float:
        print('float')
    elif type(el) is dict:
        print('dictionary')
    else:
        print('Unknown type')

