# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.name} пишет синим цветом')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.name} пишет серым цветом')


class Handle(Stationery):
    def draw(self):
        print(f'{self.name} пишет красным цветом')


start = Stationery('start')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

start.draw()
pen.draw()
pencil.draw()
handle.draw()

