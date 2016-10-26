fib_cache = {}
def fib(n):
    # If we have cached the value, then return it 
    if n in fib_cache:
        return fib_cache[n]
    # Compute the next term
    if n == 1: 
        value = 1
    elif n == 2: 
        value = 1
    else:
        value = fib(n-1) + fib(n-2)
    # Cache the value and return it
    fib_cache[n] = value
    return value
for n in range (1, 100):
    print (fib(n))

