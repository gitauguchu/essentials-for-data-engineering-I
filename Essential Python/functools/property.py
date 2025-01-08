#cached_property() is a decorator for class properties that caches the result of the method, storing it for future access without recomputation
from functools import cached_property

class Square:
    def __init__(self, side):
        self.side = side
    @cached_property
    def area(self):
        print("Calculating area")
        return self.side ** 2

square = Square(4)
print(square.area)
print(square.area)

#Use cached_property() for expensive-to-compute properties that don't change often, or if recalculating them each time is inefficient
