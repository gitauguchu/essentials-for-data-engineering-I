#cmp_to_key() converts an old-style comparison function into a key function for use with sorting
from functools import cmp_to_key

def compare(a, b):
    return (a > b) - (a < b)
sorted_list = sorted([3, 2, 1], key=cmp_to_key(compare))

print(sorted_list)

#Use cmp_to_key when you have legacy comparison functions that you want to reuse with python's sorting functions