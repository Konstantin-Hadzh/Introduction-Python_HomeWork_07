

"""
4) Реализуйте базовый класс Car. У данного класса должны быть следующие 
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, 
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, 
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен 
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar 
переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ 
к атрибутам, выведите результат. Выполните вызов методов и также покажите 
результат
"""

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгон до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Остановка')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворот {direction}')
        else:
            print('Стоит на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена: {self.speed} км/ч')
        else:
            print(f'Скорость: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена: {self.speed} км/ч.')
        else:
            print(f'Скорость: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def samsara_circle(car_metod):
    print(f"Движение {'автомобиля ГИБДД: ' if car_metod.is_police else 'часного автомобиля: '} {car_metod.name}, {car_metod.color} цвет")
    car_metod.go(40)
    car_metod.show_speed()
    car_metod.turn('налево')
    car_metod.stop()
    car_metod.show_speed()
    car_metod.turn('направо')
    car_metod.go(60)
    car_metod.show_speed()
    car_metod.go(120)
    car_metod.show_speed()
    car_metod.stop()
    print("Движение завершено", end="\n\n\n")


car = Car('чёрно-белый', 'Model 3 / 3 PS', False)
samsara_circle(car)

horch = TownCar('серебристый', '853A Voll & Ruhrbeck Spezial Cabriolet')
samsara_circle(horch)

audi = SportCar('белый', 'Sport Quattro S1 E2')
samsara_circle(audi)

studebaker = WorkCar('красный', 'M16 52A')
samsara_circle(studebaker)

zaporojetz = PoliceCar('горбатый', 'ЗАЗ-965')
samsara_circle(zaporojetz)