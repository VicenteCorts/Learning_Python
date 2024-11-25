# Clase 41
'''
def media (mylist):
    la_media = sum(mylist) / len(mylist)
    return la_media

print(media([1, 4, 5]))

# Square Area (E)
## Define a function that calculates the area of a square. For example, if I was to call your function with foo(7) the output would be 49. If I called it with foo(3)  it would return 9, and so on. Note that you don't have to name your function foo. Give it any name you want.
def foo (lado):
    area = lado * lado
    return area
    
print(foo(4))

# Volume Converter (E)
## Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 milliliters. For example, I was to call your function with foo(1) I would get an output of 29.57353. If I called it with  foo(5) I would get 147.86765, and so on.
def foo(ml):
    vol = ml * 29.57353
    return vol
    
print(foo(1))
'''

# Clase 43
'''
def media (mylist):
    la_media = sum(mylist) / len(mylist)
    return la_media

mymean = media([0, 3, 4])
print(mymean)
'''

# Clase 45
'''
def media (value):
    if type(value) == dict:
        la_media = sum(value.values()) / len(value)
    else:
        la_media = sum(value) / len(value)

    return la_media

students_grades = {"A": 9.1, "B": 8.8, "C": 7.5}
print(media(students_grades))

monday_temperature = [9.1, 8.8, 9.9]
print(media(monday_temperature))

# Warm or Cold (E)
## Define a function that: (1) takes a temperature as a parameter (2) returns "Warm" if the temperature is greater than 7 (3) returns "Cold" if the temperature is equal to or less than 7. If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.
def foo(temp):
    if temp > 7:
        msg="Warm"
    else:
        msg="Cold"
    return msg
        
print(foo(24))

# Password Controller (E)
## Define a function that: (1) takes a string as a parameter (2) returns False if the string contains less than 8 characters (3) returns True if the string contains 8 or more characters In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.
def foo(word):   
    if len(word)<8:
        msg = False
    else:
        msg = True
    return msg
    
print(foo('hwjo'))
'''

# Clase 49
'''
x = 3
y = 1
if x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual que y")
else:
    print ("x es menor que y")
'''

# Test Condicionales
'''
def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))
'''

# Clase 50
if      3>1:
    print('a')

print('aa')
print('aaa')

if 3>1:
    print('b')

print('bb')
print('bbb')

if 3 > 1:
    print('c')

print('cc')
print('ccc')

# Hot, Warm, Cold (E)
## Define a function that: (1) takes a temperature as a parameter (2) returns "Hot" if the temperature is greater than 25 (3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25. (4) returns "Cold" if the temperature is less than 15. If I called your function with foo(10) it would return "Cold". foo(15) or foo(16) or foo(25) would all return "Warm" and foo(26) would return "Hot".
def foo(temp):
    if temp > 25:
        msg = "Hot"
    elif temp <= 25 and temp >= 15:
        msg = "Warm"
    else:
        msg = "Cold"
    return msg
    
print(foo(27))
print(foo(25))
print(foo(23))
print(foo(15))
print(foo(12))