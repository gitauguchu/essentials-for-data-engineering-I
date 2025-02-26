#A decorator is a function returning another function usually applied as a function transformation using the @wrapper syntax
#The decorator modifies the behavior of its decoratee without having to change the source code
def add_exclamation(func):
    def wrapper(name):
        return func(name) + '!'
    return wrapper

@add_exclamation
def greet(name):
    return 'Hello' + ' ' + name

print(greet('Tom')) #Prints "Hello Tom!"


#Advance decorators with two inner functions
def add_symbol(symbol):
    def decorator(func):
        def wrapper(name):
            return func(name) + symbol
        return wrapper
    return decorator

@add_symbol('!')
def greet(name):
    return 'Hello' + ' ' + name

print(greet('Tom')) #Prints "Hello Tom!"

@add_symbol('??')
def greet(name):
    return 'Hello' + ' ' + name

print(greet('Tom')) #Prints "Hello Tom??"


#Using classes as decorators
#We need to implement the __call__ method which defines behaviour when we call an object like we call functions
class add_symbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def __call__(self, func):
        def wrapper(name):
            return func(name) + self.symbol
        return wrapper

@add_symbol('!')
def greet(name):
    return 'Hello' + ' ' + name

print(greet('Tom')) #Prints "Hello Tom!"

#Using functools.wraps to preserve the function's metadata
from functools import wraps
def add_exclamation(func):
    @wraps(func)
    #Decorating the wrapper with @wraps(func) forces the functions metadata to be passed onto the wrapper
    def wrapper(name):
        return func(name) + ' ' + '!'
    return wrapper

@add_exclamation 
def greet(name):
    """Greets someone"""
    return 'Hello' + ' ' + name

print(greet('Tom')) #Prints "Hello Tom !"
print(greet.__name__) #Prints "greet"
print(greet.__doc__) #Prints "Greets someone"


#Using __wrapped__ to undecorate
#To be able to undecorate, we need to: 1. Use functools.wraps to decorate our wrapper function in our decorator 
#And 2. Use __wrapped__ to access the original undecorated function
from functools import wraps
def add_exclamation(func):
    @wraps(func)
    #Decorating the wrapper with @wraps(func) forces the functions metadata to be passed onto the wrapper
    def wrapper(name):
        return func(name) + ' ' + '!'
    return wrapper

@add_exclamation 
def greet(name):
    """Greets someone"""
    return 'Hello' + ' ' + name

print(greet('Tom')) #Prints "Hello Tom !"
print(greet.__wrapped__('Tom')) #Prints "Hello Tom"


#Decorators to decorate classes
#Here we create a class decorator that adds a common function hello to every single class it decorates
def add_hello(cls):
    cls.hello = lambda self: print('Hello')
    return cls

@add_hello
class Dog: pass

@add_hello
class Cat: pass

Dog().hello() #Prints "Hello"
Cat().hello() #Prints "Hello"