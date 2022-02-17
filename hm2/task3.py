# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.


# используем словарь
month = {'1 2 12': 'Winter',
         '3 4 5': 'Spring',
         '6 7 8': 'Summer',
         '9 10 11': 'Autumn'}

month_num = input('Введите номер месяца\n').strip()

print('GeekBrains homework #2, task 3')

for key in month.keys():
    # используем list (условия соблюдены))) )
    if month_num in key.split():
        print(month[key])
        break
