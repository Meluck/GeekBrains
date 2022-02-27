"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

trans_dir = {'one': 'Один',
             'two': 'Два',
             'three': 'Три',
             'four': 'Четыре',
             'five': 'Пять',
             'six': 'Шесть',
             'seven': 'Семь',
             'eight': 'Восемь',
             'nine': 'Девять',
             'ten': 'Десять'}

with open('task4_file.txt', 'r', encoding='UTF-8') as input_file:
    with open('task4_output.txt', 'w+') as output_file:
        for line in input_file:
            sym_number = line[:line.index(' ')].lower()
            new_line = trans_dir[sym_number] + line[line.index(' '):]
            output_file.write(new_line)


