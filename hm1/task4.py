# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

if __name__ == '__main__':
    print('GeekBrains homework #1, task 3')

    print('Solution number 1')
    num_str = input('Enter integer positive number:\n')
    num = int(num_str)
    max_dig = 0
    while num > 1:
        max_dig = num % 10 if num % 10 > max_dig else max_dig
        num //= 10
    print(f'max digit is {max_dig}')

    print('\nSolution number 2')
    print('Use the fact of ASCII serial number coding:')
    max_dig_s = num_str[0]
    for dig_str in num_str:
        max_dig_s = dig_str if dig_str > max_dig_s else max_dig_s

    print(f'max digit is {max_dig_s}')
