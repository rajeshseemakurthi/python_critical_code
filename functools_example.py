from functools import cache

"""where ever the memory location been given,we have to pass on this 
 cache decorator or lru_cache decorator"""
@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)


def run():
    for i in range(400):
        print(i,fib(i))

run()