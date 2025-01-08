#Provides functions for doing mathematical operations such as square roots, trigonometry, logarithms and rounding numbers
import math

#Performing basic mathematical operations
result_sqrt = math.sqrt(25) 
print(result_sqrt)
result_pow = math.pow(2, 5)
print(result_pow)
result_abs = math.fabs(-5)
print(result_abs)

#Calculating trigonometric functions
sine_value = math.sin(math.pi / 2)
print(sine_value)
cosine_value = math.cos(math.pi)
print(cosine_value)
tangent_value = math.tan(math.pi / 4)
print(tangent_value)

#Rounding numbers to the nearest integer
rounded_number_floor = math.floor(3.6)
print(rounded_number_floor)
rounded_number_ceiling = math.ceil(3.6)
print(rounded_number_ceiling)
rounded_number_round = round(3.5)
print(rounded_number_round)

#Calculating logarithms
log_value = math.log(10, 2)
print(log_value)

#Calculating factorial
factorial_value = math.factorial(5)
print(factorial_value)

#Converting angles between degrees and radians
degrees_to_radians = math.radians(90)
print(degrees_to_radians)
radians_to_degrees = math.degrees(math.pi / 2)
print(radians_to_degrees)