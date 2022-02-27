"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

print('GeekBrains homework #4, task 7')


def fact(n: int):
    if n > 0:
        temp_res = 1
        for i in range(1, n + 1):
            temp_res *= i
            yield temp_res
    else:
        raise ValueError('n must be integer above 0')


try:
    n = int(input('Enter n:\n'))
    for el in fact(n):
        print(el)

    print(f'Тип объекта, возвращаемого функцией: {type(fact(2))}')

except Exception as ex:
    print(ex)