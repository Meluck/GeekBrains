# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

if __name__ == '__main__':
    print('GeekBrains homework #1, task 3')

    n_str = input('Enter your natural number:\n')
    res = int(n_str) + int(n_str * 2) + int(n_str * 3)
    print(f'Result for n + nn + nnn:\n{res}')
