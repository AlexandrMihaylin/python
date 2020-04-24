class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} цвет {self.color} полицейская машина - {self.is_police} ')

    def go(self):
        print(f'{self.name}: Поехали!')

    def stop(self):
        print(f'{self.name}: Остановка!')

    def turn(self, direction):
        print(f'{self.name}: Поворот {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class Towncar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class Workcar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class Sportcar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 200 else f"{self.name}: Скорость автомобиля {self.speed}"


class Policecar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = Policecar('"ППС"', 'белый', 90)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = Workcar('"Truck"', 'черный', 40)
work_car.go()
print(work_car.show_speed())
work_car.turn(1)
work_car.stop()
print()

town_car = Towncar('"Миинивэн"', 'красный', 50)
town_car.go()
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()

sport_car = Sportcar('"Спорт"', 'желтый', 120)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.stop()
print()

print(f'\nМашина {town_car.name} цвет {town_car.color}')
print(f'Машина {work_car.name} цвет {work_car.color}')
print(f'Машина {sport_car.name} цвет {sport_car.color}')
print(f'Машина {police_car.name} цвет {police_car.color}')
