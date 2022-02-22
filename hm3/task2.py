"""
2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.

Осуществить вывод данных о пользователе одной строкой.
"""

print('GeekBrains homework #3, task 2')


def print_user_data(fname, sname, birth, city, email, phone):
    print(f'{fname = }, {sname = }, {birth = }, {city = }, {email = }, {phone = }')


print_user_data(fname='Mark',
                sname='Lustgarten',
                birth='20.04.1998',
                city='Zelenograd',
                email='marklustgarten@yandex.ru',
                phone='+79108069887')
