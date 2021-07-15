# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg_1, arg_2, arg_3):
    arr = [arg_1, arg_2, arg_3]
    sorted_arr = sorted(arr, reverse=True)
    max_1 = sorted_arr[0]
    max_2 = sorted_arr[1]
    sum_max = max_1 + max_2
    return sum_max


print(my_func(9, 5, 6))




