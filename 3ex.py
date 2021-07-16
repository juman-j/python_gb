#  Реализовать программу работы с органическими клетками.
#  Необходимо создать класс Клетка.
#  В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
#  В классе должны быть реализованы методы перегрузки арифметических операторов:
#  сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#  Данные методы должны применяться только к клеткам
#  и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
#  В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, amount_sub_cells):
        self.amount = amount_sub_cells

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount - other.amount >= 0:
            return self.amount - other.amount

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        if self.amount // other.amount < 1:
            return None
        else:
            return self.amount // other.amount

    def make_order(self):
        if self.amount is not None:
            return print(('*' * 4 + '\n') * (self.amount // 4) + ('*' * (self.amount % 4)))
        else:
            return print('Отрицательное/недостаточное количество ячеек')


cell_1 = Cell(8)
cell_2 = Cell(9)
cell_3 = Cell(cell_1 - cell_2)
cell_3.make_order()
cell_1.make_order()



