#  Начните работу над проектом «Склад оргтехники».
#  Создайте класс, описывающий склад.
#  А также класс «Оргтехника», который будет базовым для классов-наследников.
#  Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#  В базовом классе определить параметры, общие для приведенных типов.
#  В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    stock = {'Printers': {}, 'Scanners': {}, 'Xerox': {}}
    shop_1 = {'Printers': {}, 'Scanners': {}, 'Xerox': {}}
    shop_2 = {'Printers': {}, 'Scanners': {}, 'Xerox': {}}
    shop_3 = {'Printers': {}, 'Scanners': {}, 'Xerox': {}}

    @classmethod
    @abstractmethod
    def __init__(cls):
        pass

    @staticmethod
    def distribution(store_number, product_type, art, num_requests):
        """
            Метод переводит требуемое количество товара из главного склада на склад нужного магазина.
            Происходит коректировка количества в словаре главного склада и в словаре прислушного магазина.

        :param store_number: Число магазина (1, 2, 3)
        :param product_type: Тип товара ('Printers', 'Scanners', 'Xerox')
        :param art: Артикул товара
        :param num_requests: Требуемое количество товара
        """
        if store_number == 1:
            if num_requests < OfficeEquipment.stock.get(str(product_type)).get(art).get('Количество'):
                OfficeEquipment.shop_1.get(str(product_type))[art] =\
                    OfficeEquipment.stock.get(str(product_type)).get(art).copy()
                # Коректировка количества в словаре магазина
                OfficeEquipment.shop_1.get(str(product_type)).get(art)['Количество'] = num_requests
                # Коректировка количества в словаре склада
                OfficeEquipment.stock.get(str(product_type)).get(art)['Количество'] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art)['Количество'] - num_requests
            elif num_requests == OfficeEquipment.stock.get(str(product_type)).get(art).get('Количество'):
                OfficeEquipment.shop_1.get(str(product_type))[art] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art).copy()
                OfficeEquipment.stock.get(str(product_type)).get(art).clear()
            else:
                print('Не достаточное количество товара на складе')

        if store_number == 2:
            if num_requests < OfficeEquipment.stock.get(str(product_type)).get(art).get('Количество'):
                OfficeEquipment.shop_2.get(str(product_type))[art] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art).copy()
                # Коректировка количества в словаре магазина
                OfficeEquipment.shop_2.get(str(product_type)).get(art)['Количество'] = num_requests
                # Коректировка количества в словаре склада
                OfficeEquipment.stock.get(str(product_type)).get(art)['Количество'] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art)['Количество'] - num_requests
            elif num_requests == OfficeEquipment.stock.get(str(product_type)).get(art).get('Количество'):
                OfficeEquipment.shop_2.get(str(product_type))[art] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art).copy()
                OfficeEquipment.stock.get(str(product_type)).get(art).clear()
            else:
                print('Не достаточное количество товара на складе')

        if store_number == 3:
            if num_requests < OfficeEquipment.stock.get(str(product_type)).get(art).get('Количество'):
                OfficeEquipment.shop_3.get(str(product_type))[art] =\
                    OfficeEquipment.stock.get(str(product_type)).get(art).copy()
                # Коректировка количества в словаре магазина
                OfficeEquipment.shop_3.get(str(product_type)).get(art)['Количество'] = num_requests
                # Коректировка количества в словаре склада
                OfficeEquipment.stock.get(str(product_type)).get(art)['Количество'] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art)['Количество'] - num_requests
            elif num_requests == OfficeEquipment.stock.get(str(product_type)).get(art).get('Количество'):
                OfficeEquipment.shop_3.get(str(product_type))[art] = \
                    OfficeEquipment.stock.get(str(product_type)).get(art).copy()
                OfficeEquipment.stock.get(str(product_type)).get(art).clear()
            else:
                print('Не достаточное количество товара на складе')

    @staticmethod
    def get_info(branch):
        """
        Метод выводит информацию о товаре находящийся в выбранном отделении или на складе.

        :param branch: (1, 2, 3)- Числа для магазинов. 'stock'- для склада
        """
        if branch == 1:
            print('Товар в 1 магазине')
            for el in OfficeEquipment.shop_1:
                for q in OfficeEquipment.shop_1.get(el).items():
                    print(el, q)
        elif branch == 2:
            print('Товар во 2 магазине')
            for el in OfficeEquipment.shop_2:
                for q in OfficeEquipment.shop_2.get(el).items():
                    print(el, q)
        elif branch == 3:
            print('Товар в 3 магазине')
            for el in OfficeEquipment.shop_3:
                for q in OfficeEquipment.shop_3.get(el).items():
                    print(el, q)
        elif branch == 'stock':
            print('Товар на складе')
            for el in OfficeEquipment.stock:
                for q in OfficeEquipment.stock.get(el).items():
                    print(el, q)
        else:
            print('Введите число магазина. Для плучения информации про склад, введите "stock"')


class Printers(OfficeEquipment):
    @classmethod
    def __init__(cls, name, vendor_code, quantity, price, production_year, guarantee, connection_type):
        if isinstance(name and connection_type, str) and \
                isinstance((vendor_code and quantity and price and production_year and guarantee), int):
            cls.stock[str(cls.__name__)].update({vendor_code: {'Имя': name,
                                                               'Количество': quantity,
                                                               'Год производства': production_year,
                                                               'Гарантия': guarantee,
                                                               'Тип подключения': connection_type}})
        else:
            print('Ошибка типа данных!')


class Scanners(OfficeEquipment):
    @classmethod
    def __init__(cls, name, vendor_code, quantity, price, production_year, guarantee, resolution):
        if isinstance(name, str) and \
                isinstance((vendor_code and quantity and price and production_year and guarantee), int):
            cls.stock[str(cls.__name__)].update({vendor_code: {'Имя': name,
                                                               'Количество': quantity,
                                                               'Год производства': production_year,
                                                               'Гарантия': guarantee,
                                                               'Тип подключения': resolution}})
        else:
            print('Ошибка типа данных!')


class Xerox(OfficeEquipment):
    @classmethod
    def __init__(cls, name, vendor_code, quantity, price, production_year, guarantee, page_per_min):
        if isinstance(name, str) and isinstance((vendor_code and quantity and
                                                 price and production_year and guarantee and page_per_min), int):
            cls.stock[str(cls.__name__)].update({vendor_code: {'Имя': name,
                                                               'Количество': quantity,
                                                               'Год производства': production_year,
                                                               'Гарантия': guarantee,
                                                               'Тип подключения': page_per_min}})
        else:
            print('Ошибка типа данных!')


# Запись характеристик товара и поставленного количества на склад
printer_1 = Printers('HP Laser 107wr', 129054, 100, 8990, 2011, 2, 'wifi')
printer_2 = Printers('Epson L132', 123456, 100,  11990, 2016, 2, 'wifi')
scanner_1 = Scanners('Canon Scan LiDE300', 213456, 100, 5390, 2019, 2, 1800)
xerox_1 = Xerox('Xerox B215', 412621, 100, 20190, 2019, 2, 20)

# Распределение товара по точкам сбыта
OfficeEquipment.distribution(1, "Printers", 129054, 5)
OfficeEquipment.distribution(2, "Printers", 129054, 5)
OfficeEquipment.distribution(3, "Printers", 129054, 5)
OfficeEquipment.distribution(1, "Printers", 123456, 4)
OfficeEquipment.distribution(2, "Printers", 123456, 9)
OfficeEquipment.distribution(3, "Printers", 123456, 80)
OfficeEquipment.distribution(1, 'Scanners', 213456, 11)
OfficeEquipment.distribution(2, 'Scanners', 213456, 12)
OfficeEquipment.distribution(3, 'Scanners', 213456, 18)
OfficeEquipment.distribution(1, 'Xerox', 412621, 24)
OfficeEquipment.distribution(2, 'Xerox', 412621, 27)
OfficeEquipment.distribution(3, 'Xerox', 412621, 1)

# Информация о товаре на складе или в магазинах
OfficeEquipment.get_info('stock')
print('-' * 130)
OfficeEquipment.get_info(1)
print('-' * 130)
OfficeEquipment.get_info(2)
print('-' * 130)
OfficeEquipment.get_info(3)
