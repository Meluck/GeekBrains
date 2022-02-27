"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

print('GeekBrains homework #4, task 2')


try:
    data = [int(sym) for sym in input('Enter numbers\n').strip().split(sep=',')]
    res = [el for idx, el in enumerate(data[1:]) if data[idx + 1] > data[idx]]
    print(f'{res = }')
except ValueError as ver:
    print(ver)
except Exception as ex:
    print(ex)
