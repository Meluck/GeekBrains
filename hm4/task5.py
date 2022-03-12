"""
5. Реализовать формирование списка,
используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


from functools import reduce

print('GeekBrains homework #4, task 5')

odd_num_lst = [num for num in range(100, 1002, 2)]
mul_res = reduce(lambda x, y: x * y, odd_num_lst)
print(f'{mul_res = }')
