# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

print('Программа для вычисления суммы')
print('Стоп слово: "stop"')
empty_list = []
while True:
    my_str = input('Ввод: ')
    clear_str = my_str.strip()
    my_list = clear_str.split(" ")
    if 'stop' in my_list:
        z = my_list.index('stop')
        last_list = []
        last_list.extend(my_list[0:z])
        for el in last_list:
            el = int(el)
            empty_list.append(el)
        break
    else:
        for el in my_list:
            el = int(el)
            empty_list.append(el)
        print(empty_list)
        get_sum = sum(empty_list)
        print(get_sum)


print(empty_list)
get_sum = sum(empty_list)
print(get_sum)

print('END')




