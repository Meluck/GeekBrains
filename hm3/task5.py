"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""

print('GeekBrains homework #3, task 5')


def my_sum(num_list: list) -> float:
    """
    :param: list
    :rtype: float
    """
    global tot_sum
    tot_sum += sum(num_list)
    return tot_sum


def my_sum_v2(num_list: list):
    my_sum_v2.tot_sum += sum(num_list)
    return my_sum_v2.tot_sum


my_sum_v2.tot_sum = 0

tot_sum = 0

while True:
    input_list = input('Enter your numbers using space as separator (q for exit):\n').strip().split()
    if 'q' not in input_list:
        float_list = [float(el) for el in input_list]
        print(f'{my_sum(float_list) = }\n{my_sum_v2(float_list) = }')
    else:
        q_pos = input_list.index('q')
        print(f'{my_sum(float_list[:q_pos]) = }\n{my_sum_v2(float_list[:q_pos]) = }')
        break
