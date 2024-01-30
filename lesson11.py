import math

# Task 1
class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        else:
            return "У вас обычная газировка"


# Task 2
class Math:
    @staticmethod
    def addition(value1, value2):
        return value1 + value2

    @staticmethod
    def subtraction(value1, value2):
        return value1 - value2

    @staticmethod
    def multiplication(value1, value2):
        return value1 * value2

    @staticmethod
    def division(value1, value2):
        if value2 != 0:
            return value1 / value2
        else:
            return 'cannot division by 0'


# Task 3

class Car:
    def __init__(self, color, type_car, year):
        self.color = color
        self.type_car = type_car
        self.year = year
        self.motors_status = False

    def start(self):
        self.motors_status = True
        print('Автомобиль заведён')

    def stop(self):
        self.motors_status = False
        print('Автомобиль заглушен')

    def set_color(self, new_color):
        self.color = new_color
        print(f'new car color: {new_color}')

    def set_type_car(self, new_type_car):
        self.type_car = new_type_car
        print(f'new type car: {new_type_car}')

    def set_year(self, new_year):
        self.year = new_year
        print(f'new year car: {new_year}')


# Task 4

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.coord_center = (x, y, z)

    def get_volume(self):
        volume = (4 / 3) * math.pi * self.radius ** 2
        return volume

    def get_square(self):
        square = 4 * math.pi * self.radius ** 2
        return square

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.coord_center

    def set_radius(self, new_radius):
        self.radius = new_radius

    def set_center(self, new_x, new_y, new_z):
        self.coord_center = (new_x, new_y, new_z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.coord_center[0]) ** 2
                             + (y - self.coord_center[1]) ** 2 + (z - self.coord_center[2]) ** 2)
        return distance <= self.radius


#  Task 5

class SuperStr(str):
    def is_repeatance(self, string):
        if not string:
            return False

        repeat_count = len(self) // len(string)
        return self == string * repeat_count

    def is_palindrom(self):
        clean_string = ''.join(s.lower() for s in self if s.isalnum())
        return clean_string == clean_string[::-1]


#  calls
#  Task 1

soda_with_flavor = Soda("клубничным")
print(soda_with_flavor)

soda_without_flavor = Soda()
print(soda_without_flavor)

#  Task 2


result_addition = Math.addition(4, -23)
print(f'the result of sum: {result_addition}')
result_subtraction = Math.subtraction(4.5, 34.5)
print(f'the result of subtraction: {result_subtraction}')
result_multiplication = Math.multiplication(12, 5)
print(f'the result of multiplication: {result_multiplication}')
result_division = Math.division(34, 5)
print(f'the result of division: {result_division}')

# Task 3

my_car = Car(color="red", type_car="bmw", year=2020)

print(f"color : {my_car.color}, type: {my_car.type_car}, year: {my_car.year}")

my_car.start()

my_car.set_year(2021)
my_car.set_type_car("ferrari")
my_car.set_color("green")

my_car.stop()

#  Task 4


sphere1 = Sphere()
print('FIRST SPHERE:')
print('Volume:', sphere1.get_volume())
print('Surface Area:', sphere1.get_square())
print('Radius:', sphere1.get_radius())
print('Center:', sphere1.get_center())

sphere1.set_radius(5)
sphere1.set_center(2, 3, 4)
print('New Radius:', sphere1.get_radius())
print('New Center:', sphere1.get_center())

point_inside = sphere1.is_point_inside(26, 3, 4)
print('Is Point Inside Sphere:', point_inside)

sphere2 = Sphere(radius=3, x=1, y=2, z=3)
print('SECOND SPHERE:')
print('Volume:', sphere2.get_volume())
print('Surface Area:', sphere2.get_square())
print('Radius:', sphere2.get_radius())
print('Center:', sphere2.get_center())

sphere2.set_radius(5)
sphere2.set_center(2, 3, 4)
print('New Radius:', sphere2.get_radius())
print('New Center:', sphere2.get_center())

point_inside = sphere2.is_point_inside(2, 3, 4)
print('Is Point Inside Sphere:', point_inside)

#  Task 5


super_str = SuperStr("abcabcabc")

result_repeatance = super_str.is_repeatance("abc")
print(f"Is 'abcabcabc' a repetition of 'abc'?: {result_repeatance}")

result_palindrom = super_str.is_palindrom()
print(f"Is 'abcabcabc' a palindrome?: {result_palindrom}")
