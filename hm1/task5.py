# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

if __name__ == '__main__':
    print('GeekBrains homework #1, task 5')

    revenue = float(input('Введите размер выручки фирмы $:\n'))
    cost = float(input('Введите размер издержек фирмы, $:\n'))
    if revenue > cost:
        print(f'Прибыль фирмы составила {revenue - cost}$')
    elif revenue < cost:
        print(f'Убыток фирмы составил {cost - revenue}$')
    else:
        print(f'Фирма работает в ноль. Стоит продумывать следующие шаги')