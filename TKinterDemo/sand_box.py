# args = unlimited positional arguments

def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,4,6,5,7,8,9,4,2,4,5,2,1))


# **kwargs: many key worded arguments
# also is a dictionary type
# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)