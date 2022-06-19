factorial = lambda x : x if x <= 1 else x * factorial(x-1)
print(factorial(3))
