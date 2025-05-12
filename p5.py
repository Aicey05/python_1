# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name} and I protect {self.city} with my power: {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass with encapsulation and method override
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.__flight_speed = flight_speed  # Encapsulated attribute

    def use_power(self):
        return f"{self.name} soars through the sky at {self.__flight_speed} km/h using {self.power}!"

# Create objects
hero1 = Superhero("Shadow Knight", "Invisibility", "Gotham")
hero2 = FlyingSuperhero("Sky Falcon", "Wind Control", "Metropolis", 300)

# Test output
print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.use_power())




# Base class
class Vehicle:
    def move(self):
        pass

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Polymorphic behavior
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
