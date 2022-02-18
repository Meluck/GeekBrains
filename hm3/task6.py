"""
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

print('GeekBrains homework #3, task 5')


def int_func(*words_str: list[str]):
    new_words = []
    for word in words_str:
        new_words.append(f'{word[0].upper()}{word[1:]}')
    return new_words


while True:
    in_par, *input_params = input('Enter your words using space as separator (q for exit):\n').strip().split()
    if 'q' != in_par:
        print(' '.join(int_func(in_par, *input_params)))
    else:
        break
