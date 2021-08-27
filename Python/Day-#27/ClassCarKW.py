class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.price = kw.get("price")

# Car()
# (class) Car(**kw)
# The base class of the class hierarchy.
# When called, it accepts no arguments and returns a new featureless instance that has no instance attributes and cannot be given any.

my_car = Car(make="Nissan")
print(my_car.make) # Nissan
print(my_car.price) # None