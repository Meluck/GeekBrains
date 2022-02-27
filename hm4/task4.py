"""
4. Представлен список чисел. Определите элементы списка,
не имеющие повторений. Сформируйте итоговый массив чисел,
соответствующих требованию. Элементы выведите в порядке
их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


print('GeekBrains homework #4, task 4')

try:
    data = [int(sym) for sym in input("Enter numbers: \n").strip().split(sep=',')]
    res = [el for el in data if data.count(el) == 1]
    print(res)
except ValueError as ver:
    print(ver)
except Exception as ex:
    print(ex)