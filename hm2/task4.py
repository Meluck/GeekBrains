# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

print('GeekBrains homework #2, task 4')

words = input('Введите набор слов\n').strip().split()

for ind, string in enumerate(words):
    print(f'{ind + 1}: {string[:10]}')