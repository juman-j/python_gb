# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num1: int, num2: int):
    if num2 != 0:
        return float(num1 / num2)
    else:
        return print('You cannot divide by zero!')


print(division(int(input('numerator: ')), int(input('denominator: '))))

print('END')
