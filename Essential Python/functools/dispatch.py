#singledispatch() is a decorator that transforms a function into a single-dispatch generic function, allowing different implementations based on the first argument type
from functools import singledispatch

@singledispatch
def process(value):
    print("Default processing")

@process.register(int)
def _(value):
    print("Processing integer", value, sep=":")

@process.register(str)
def _(value):
    print("Processing string", value, sep=":")

process(10)
process("hello")

#Use singledispatch() when you need to handle multiple types within a function, providing a clear and organized way to define type-specific behavior
#In a class, we need to use singlemethoddispatch
#This we can use when we want to restrict the type of variable