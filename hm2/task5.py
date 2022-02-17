# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных
# чисел, который не возрастает. У пользователя нужно запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


print('GeekBrains homework #2, task 5')

# Используем sort только при создании начального, потом по-четному
rating: list = sorted([int(pos) for pos in input('Enter start rating data\n').strip().split()], reverse=True)
print(f'Start rating: {rating}')

while True:
    new_input = input('Enter new rating number\n')
    if new_input in ['q', 'quite', 'exit()']:
        break
    else:
        new_pos = int(new_input)
        for idx, el in enumerate(rating):
            if new_pos > el:
                rating.insert(idx, new_pos)
                print(f'Insert position: {idx}')
                break
        if new_pos < min(rating):
            rating.append(new_pos)

    print(f'New rating is: {rating}')

