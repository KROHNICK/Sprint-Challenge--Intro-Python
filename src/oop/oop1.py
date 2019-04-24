# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # base class
    def __init__(self, name):
        self.name = name


class GroundVehicle(Vehicle):
    def __init__(self, name, desc):
        super().__init__(name, desc)


class Car(GroundVehicle):
    def __init__(self, name, desc):
        super().__init__(name, desc)


class Motorcycle(GroundVehicle):
    def __init__(self, name, desc):
        super().__init__(name, desc)


class FlightVehicle:  # base class
    def __init__(self, name):
        self.name = name


class Airplane(FlightVehicle):
    def __init__(self, name, desc):
        super().__init__(name, desc)


class Starship:  # base class
    def __init__(self, name):
        self.name = name
