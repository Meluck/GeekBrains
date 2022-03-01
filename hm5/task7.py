"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

print('GeekBrains homework #5, task 7')

firm_dict = {}
total_profit = 0
firm_prof_counter = 0


try:
    with open('task7_input.txt', 'r', encoding='UTF-8') as in_file:
        for line in in_file:
            firm, _, profit, losses = line.strip().split()
            profit, losses = float(profit), float(losses)

            # включаем в расчет средней прибыли только фирмы без убытков
            if profit >= losses:
                total_profit += profit - losses
                firm_prof_counter += 1

            # в словарь вносим всех подряд с вычисленной прибылью/убытком
            firm_dict[firm] = profit - losses

        # среднее только по фирмам, которые заработали
        average_profit = total_profit / firm_prof_counter
        final_lst = [firm_dict, {'average_profit': average_profit}]
        print(f'Data for writing:\n{final_lst}')

        with open('task7_output.json', 'w+') as out_file:
            json.dump(final_lst, out_file)

        print('Check file content:')
        with open('task7_output.json') as json_file:
            data = json.load(json_file)
            print(data)
except Exception as ex:
    print(ex)

