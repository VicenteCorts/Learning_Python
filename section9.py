# Clase 74
'''
temps = [221, 234, 340, 230]

new_temps = [ temp / 10 for temp in temps]

print(new_temps)
'''
# Clase 75
'''
temps = [221, 234, 340, -9999, 230]

new_temps = [ temp / 10 for temp in temps if temp != -9999]

print(new_temps)
'''
# Only Numbers (E)
## Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers. For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].
def foo (mylist):
    listnew = [item for item in mylist if type(item) == int]
    return listnew
print(foo([99, 'no data', 95, 94, 'no data'])) 

# Only Positive Numbers (E)
## Define a function that takes as parameter list of numbers and returns the list containing only the numbers that are greater than 0. For example, I called your function with foo([-5, 3, -1, 101]) it should return [3, 101].
def foo (mylist):
    listnew = [item for item in mylist if item > 0]
    return listnew
print(foo([-5, 3, -1, 101]))

# Clase 76
'''

'''
