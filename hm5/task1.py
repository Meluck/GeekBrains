"""
1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""


if __name__ == '__main__':
    print('GeekBrains homework #5, task 1')

    try:
        with open('task1_file.txt', 'a+') as file:
            while True:
                input_data = input('Enter your data\n')
                if input_data == '':
                    print('End of data writing')
                    break
                else:
                    file.write(f'{input_data}\n')
    except IOError as ioer:
        print(ioer)
    except Exception as ex:
        print(ex)
