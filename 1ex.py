# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    atr = 0
    int_list = []

    def __init__(self, d, m, y):
        self.date = f'{d}-{m}-{y}'
        print(f'Строка ({self.date})')
        Data.atr = self.date

    @classmethod
    def trans(cls):
        for el in cls.atr.split('-'):
            cls.int_list.append(int(el))
        print(f'Числа в формате int {cls.int_list}')

    @staticmethod
    def valid():
        if Data.int_list[0] > 0 and Data.int_list[0] <= 31:
            pass
        else:
            print(f'Число месяца{Data.int_list[0]}, должно быть в интервале от 1 до 31')
        if Data.int_list[1] > 0 and Data.int_list[1] <= 12:
            pass
        else:
            print(f'Месяц {Data.int_list[1]}, должен быть в интервале от 1 до 12')
        if Data.int_list[2] >= 0 and Data.int_list[2] <= 2021:
            pass
        else:
            print(f'Год {Data.int_list[2]}, должен быть в интервале от 0 до 2021')


try_data = Data(8, 7, 2021)
try_data.trans()
Data.valid()


















