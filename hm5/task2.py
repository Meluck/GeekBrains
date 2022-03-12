"""
2. Создать текстовый файл (не программно),
сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

print('GeekBrains homework #5, task 2')

content_dir = {}
try:
    with open('task2_file.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for idx, line in enumerate(data):
            content_dir[idx] = len(line.split())
except IOError as ioer:
    print(ioer)
except Exception as ex:
    print(ex)

for key, val in content_dir.items():
    print(f'Line {key} contains {val} words')


