"""
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

content_dir = {}
try:
    with open('task3_file.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            name, salary = line.strip().split()
            content_dir[name] = float(salary)
except IOError as ioer:
    print(ioer)
except Exception as ex:
    print(ex)

salary_lvl = 20_000
result = [name for name, salary in content_dir.items() if salary < salary_lvl]
print(f'Сотрудники, с окладом менее {salary_lvl}: {result}')

medium_salary = sum(content_dir.values()) / len(content_dir)
print(f'Средний оклад сотрудников: {medium_salary} ₽')