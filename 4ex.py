# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала,
# остановилась,
# повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police == 'police':
            self.is_police = True
        else:
            self.is_police = False

    def go(self):
        print(f'{self.name} started moving')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'{self.name} travels at a speed of {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} travels at a speed of {self.speed}')
        if self.speed > 60:
            print(f'{self.name} is overspeed')
            print(f'{ford_police.name} ведет погоню за {self.name}')
            PoliceCar.fbi(ford_police)
        else:
            pass


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} travels at a speed of {self.speed}')
        if self.speed > 40:
            print(f'{self.name} is overspeed')
            print(f'{ford_police.name} ведет погоню за {self.name}')
            PoliceCar.fbi(ford_police)
        else:
            pass


class SportCar(Car):
    def show_speed(self):
        print(f'{self.name} travels at a speed of {self.speed}')
        if self.speed < 200:
            print('Поддай газу!')
        else:
            print('Полет нормальный')


class PoliceCar(Car):
    def fbi(self):
        if self.is_police is True:
            print('FBI, open up!')

#  def __init__(self, speed, color, name, is_police):


ford_police = PoliceCar(300, 'black', 'Ford Police Interceptor Utility', 'police')
porsche_911 = SportCar(246, 'blue', 'porsche 911', 'no')
tesla_model_x = TownCar(90, 'white', 'tesla model x', 'no')
lada_vesta = WorkCar(41, 'orange', 'lada vesta', 'no')

# go
porsche_911.go()
tesla_model_x.go()
lada_vesta.go()
ford_police.go()
print('-' * 100)
porsche_911.turn('left')
tesla_model_x.turn('right')
ford_police.turn('left')
lada_vesta.turn('right')
print('-' * 100)
ford_police.show_speed()
tesla_model_x.show_speed()
porsche_911.show_speed()
lada_vesta.show_speed()
print('-' * 100)
ford_police.stop()
tesla_model_x.stop()
porsche_911.stop()
lada_vesta.stop()
