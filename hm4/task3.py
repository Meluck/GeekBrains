"""
3. Для чисел в пределах от 20 до 240 найти числа,
кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""


print('GeekBrains homework #4, task 3')

print([el for el in range(20, 240) if (el % 21 == 0 or el % 20 == 0)])

