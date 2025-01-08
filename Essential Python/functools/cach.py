#cache() is a decorator that caches the result of function calls. It's a shorthand for lru_cache(maxsize=None)
from functools import cache

@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(5))

#Use cache() for functions where results should be cached without a size limit, esp when calls with the same arguments occur frequently
#The difference between cache and lru_chache is that when lru_cache reaches the maxsize, lru_cache will remove the least-recent used cache item