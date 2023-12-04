class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.color} транспорт {self.brand}"

    def __repr__(self):
        return f"Vehicle(brand='{self.brand}', color='{self.color}')"

    def __eq__(self, other):
        return isinstance(other, Vehicle) and self.brand == other.brand and self.color == other.color

    def __ne__(self, other):
        return not self.__eq__(other)


class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def __str__(self):
        return f"{self.color} автомобиль {self.brand} с колесами"

    def __repr__(self):
        return f"Car(brand='{self.brand}', color='{self.color}', num_wheels={self.num_wheels})"

    def __eq__(self, other):
        return isinstance(other, Car) and super().__eq__(other) and self.num_wheels == other.num_wheels

    def __ne__(self, other):
        return not self.__eq__(other)


class ElectricCar(Car):
    def __init__(self, brand, color, num_wheels, battery_capacity):
        super().__init__(brand, color, num_wheels)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{self.color} электроавтомобиль {self.brand} с {self.num_wheels} колесами и емкостью аккумулятора kWh"

    def __repr__(self):
        return f"ElectricCar(brand='{self.brand}', color='{self.color}', num_wheels={self.num_wheels}, battery_capacity={self.battery_capacity})"

    def __eq__(self, other):
        return isinstance(other, ElectricCar) and super().__eq__(other) and self.battery_capacity == other.battery_capacity

    def __ne__(self, other):
        return not self.__eq__(other)


brand = input('Введите марку транспортного средства:')
color = input('Введите цвет транспортного средства:')

vehicle = Vehicle(brand, color)
print(vehicle)
print(repr(vehicle))

car_brand = input('Введите марку автомобиля:')
car_color = input('Введите цвет автомобиля:')
num_wheels = int(input('Введите количество колес автомобиля:'))

car = Car(car_brand, car_color, num_wheels)
print(car)
print(repr(car))

electric_brand = input('Введите марку электромобиля:')
electric_color = input('Введите цвет электромобиля:')
battery_capacity = float(
    input('Введите емкость батареи электромобиля (в кВт·ч):'))

electric_car = ElectricCar(
    electric_brand, electric_color, num_wheels, battery_capacity)
print(electric_car)
print(repr(electric_car))

# Сравнение экземпляров класса
print(electric_car == vehicle)
print(electric_car != vehicle)
print(car == vehicle)
print(car != vehicle)
print(car == electric_car)
print(car != electric_car)
