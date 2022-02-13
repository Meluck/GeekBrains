# Задание №1
# 1. Поработайте с переменными, создайте несколько,
# выведите на экран. Запросите у пользователя некоторые числа и строки и
# сохраните в переменные, затем выведите на экран.

if __name__ == "__main__":
    print('GeekBrains homework #1, task 1')

    name = input("Hi, how can I contact you?\n")
    print('Awkward question time!')
    age = int(input('So, how old are u?:\n'))
    weight = float(input('How much do u weigh, dude?\n'))
    books = input("What's u favorite books? Use ',' for  enumeration\n").split(sep=",")
    print('Ha-ha. I know everything about you now! Look:')
    print(f'Secret information about {name}:')
    print(f'Age: {age}\nWeight: {weight}')
    for idx in range(len(books)):
        print(f'Favorite book number {idx}: {books[idx]}')
    input()
