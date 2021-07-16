#  Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#  Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
#  Класс-исключение должен контролировать типы данных элементов списка.
from itertools import permutations


class MyError(Exception):
    def __init__(self, text):
        self.text = text


def int_list():
    my_list = []
    # numbers = '1234567890'.  совсем забыл про .isdigit:)
    while True:
        user_input = input('user_input: ')
        if user_input == 'stop':
            break
        try:
            if user_input.isdigit():
                my_list.append(int(user_input))
            else:
                raise MyError(f'({user_input}) это не число')
        except MyError as er:
            print(f'Ошибка ({er}). Введите число.')

    return print(my_list)


int_list()


