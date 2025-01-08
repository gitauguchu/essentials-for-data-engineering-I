#reduce() applies a binary function cummulatively to the items of an iterable, reducing it to a single value
from functools import reduce

#Calculating the product of a list of numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

#Use reduce() when you want to perform cumulative operations such as summing or multiplying elements in a list
