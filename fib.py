# add the two privious numbers
# Fibonacci Sequence [1, 1, 2, 3, 5, 8, 13, 21, 34]
# Return the Nth Fibonacci Number
#

cache = {}

def fib(n):
    if n < 0:
        print("Negative numbers are not valid")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in cache:
        return cache[n]
    else:
        # Return (n - 1) + (n - 2)
        value = fib(n - 1) + fib(n - 2)
        cache[n] = value
        return value

print(fib(777))

# if cache is None:
#     cache = {}

# if not cache:
#     cache = {i: 0 for i in range(n+1)}