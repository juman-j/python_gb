# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def my_func(x: float, y):
    """
    Эта функция возводит х в отрицательную степень у
    :param x: Основание
    :param y: Отрицательная степень
    """
    counter = 0
    z = 1
    while counter < abs(y):
        z = z * x
        counter += 1
    result = 1 / z
    return result


p_1 = float(input('Основание: '))
p_2 = int(input('Отрицательная степень: '))
print(my_func(p_1, p_2))

print('END')


# p_1 = int(input('number1: '))
# p_2 = int(input('number2: '))
#
# func_2 = lambda pam_1, pam_2: pow(pam_1, pam_2)
# print(light(p_1, p_2))
