#wraps() is a decorator that helps keep the metadata of the original function intact when wrapping it with another function
from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Prints a greeting"""
    print("Hello!")

print(greet.__name__)
print(greet.__doc__)
greet()

#Use wraps() when you write decorators to ensure the function's metadata is preserved making it easier to understand and debug your code
#It maintains the original of the functions