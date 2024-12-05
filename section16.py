# Clase 144
'''
print(1)
int(9)
int (99)
print(2)
print (3)
'''

# Clase 145
'''
a = 1
b = "2"
print(int(2.5))
print( a + float(b))
'''

# Clase 146
'''
a = 1
b = "2"
c = 3
print(int(2.5))
print( c/0)
'''

# Clase 148
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division can't be done"

print(divide(1,0))