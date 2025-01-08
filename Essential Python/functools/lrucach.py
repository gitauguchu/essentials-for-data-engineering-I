#lru_cache() is a decorator that caches the result of function calls using a Least Recently Used(LRU) cache
from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(10))

#Use lru_cache() to optimize functions that are called frequently with the same arguments reducing computational overhead by caching results
#Use this function if you are calling the function with the same parameter