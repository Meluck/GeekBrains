"""
6. Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.

Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

filename = 'task6_input.txt'
sub_dict = {}


def calc_sum(str_data: str) -> int:
    hours_str = str_data.strip().split(sep=' ')
    sum_h = 0
    for h_str in hours_str:
        # вычленяем часы как символы до первой круглой скобки
        sum_h += int(h_str[:h_str.index('(')])
    return sum_h


try:
    with open(filename, 'r', encoding='UTF-8') as in_file:
        data = in_file.readlines()
        for line in data:
            sub, hours_line = line.split(sep=':')
            if sub not in sub_dict.keys():
                sub_dict[sub] = calc_sum(hours_line)
            else:
                sub_dict[sub] += calc_sum(hours_line)

    print(sub_dict)

except IOError as ioer:
    print(ioer)
except Exception as ex:
    print(ex)
