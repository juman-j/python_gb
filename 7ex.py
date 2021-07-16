#  Реализовать проект «Операции с комплексными числами».
#  Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
#  Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    # def __sub__(self, other):
    #     return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    # def __truediv__(self, other):
    #     if other.number == 0 + 0j:
    #         return 'На ноль делить нельзя!'
    #     else:
    #         return self.number / other.number


a = ComplexNumbers(2 + 2j)
b = ComplexNumbers(0 + 0j)
print(ComplexNumbers.__add__(a, b))
# print(ComplexNumbers.__sub__(a, b))
print(ComplexNumbers.__mul__(a, b))
# print(ComplexNumbers.__truediv__(a, b))

