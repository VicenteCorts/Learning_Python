# Clase 79
''' 
def area (a, b):
    return a * b
print(area(4, 5))

# Function with Multiple Parameters (E)
## Implements a function that takes two strings as parameters, concatenates them, and returns the result.
def foo(a, b):
    return "{}{}".format(a, b)
print(foo("hola ", "Mundo"))
'''

# Clase 81
'''
def area (a, b=5):
    return a * b
print(area(4, b=7))
print(area(4, 7))
'''

# Clase 82
'''
def mean(*args):
    return sum(args)/len(args)
print(mean(1, 6, 3))

# Average Function (E)
## Define a function that takes an indefinite number of numbers as arguments and returns their average. If I called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.
def foo(*args):
    return sum(args)/len(args)
print(foo(10, 20, 30, 40) )

# Indefinite Number of Strings Processed (E)
## Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].
def foo(*args):
    return sorted(arg.upper() for arg in args)
    
print(foo("snow", "glacier", "iceberg"))
'''

# Clase 83
def mean(**kwargs):
    return kwargs
print(mean(a=1, b=6, c=3))
