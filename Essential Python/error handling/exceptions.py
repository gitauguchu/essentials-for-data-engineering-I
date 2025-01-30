#Exceptions are python's way of signalling that something went wrong during program execution

#Handling division by zero
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("You can't divide by zero")

#Handling multiple exceptions
#Multiple except blocks
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter a valid number")

#Catching all exceptions
try:
    num = int(input("Enter a number: "))
    print(10/num)
except Exception as e:
    print(f"An error occurred: {e}")

#Using else and finally
#Else executes when no exception is raised
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(f"Result: {result}")

#Raising exceptions
def divide(a, b) -> float:
    """The function is supposed to divide two numbers and return the value"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)

#Creating custom exceptions
class NegativeNumberError(Exception):
    def __init__(self, message="Cannot compute the square root of a negative number"):
        super().__init__(message)
def square_root(num):
    if num < 0:
        raise NegativeNumberError()
    return num ** 0.5

try:
    result = square_root(-4)
except NegativeNumberError as e:
    print(e)

#Finally executes regardless of whether an error occurred and is finally used for cleanup tasks
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File closed.")

