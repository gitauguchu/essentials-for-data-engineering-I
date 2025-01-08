#partial() allows you to fix a certain number of arguments of the function and create a new function with fewer parameters
from functools import partial

#Fixing the first argument of a multiplication function
def multiply(x, y, z):
    return x * y * z

#Creating a new function with x fixed at 2
double = partial(multiply, 2)
print(double(3, 4))

#Use partial() when you repeatedly pass the same argument, and mainly if you pass the same parameter