# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

print('GeekBrains homework #2, task 2')

idle_lst = input('Введите данные списка через пробел\n').strip().split()

idle_len = len(idle_lst)
for i in range(0, idle_len - idle_len % 2, 2):
    idle_lst[i], idle_lst[i+1] = idle_lst[i + 1], idle_lst[i]

print(idle_lst)
