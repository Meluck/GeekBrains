"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу:
(выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
 конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

print('GeekBrains homework #4, task 1')

if __name__ == "__main__":
    print(argv)
    _, working_time, salary_per_h, premium, *tail = argv
    if len(tail) > 0:
        print("Input error")
    else:
        try:
            profit = float(working_time) * float(salary_per_h) + float(premium)
            print(f'{profit = }$')
        except ValueError as ver:
            print('Unsupported parameters: {ver}')
        except Exception as ex:
            print(ex)
