# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

if __name__ == '__main__':
    print('GeekBrains homework #1, task 2')

    total_time_sec = int(input('Enter time counted in seconds:\n'))

    sec_in_hour = 60*60
    min_in_hour = 60

    hours = total_time_sec // SEC_IN_HOUR
    minutes = (total_time_sec % SEC_IN_HOUR) // MIN_IN_HOUR
    seconds = total_time_sec % MIN_IN_HOUR

    print(f'Converted time:\n{hours:02}:{minutes:02}:{seconds:02}')
