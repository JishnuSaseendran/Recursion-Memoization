
import functools 

# Least Recentlt Used cache
# works in python3

@functools.lru_cache(maxsize = 1000)
def fib(n):

    # Compute the Nth term
    if n == 1: 
        return 1
    elif n == 2: 
        return 1
    else:
        return fib(n-1) + fib(n-2)

x = int(input('Enter the range : '))
for n in range (1, x):
    print (fib(n))

