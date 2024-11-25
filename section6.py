# Clse 53
'''
def foo(temp):
    if temp > 7:
        return "Warm"
    else:
        return"Cold"

user_input = float(input("Introduce una temperatura:"))
print(foo(user_input))
'''

# Clase 54
'''
user_input = input("Cuálm es tu nombre compadre? ")
message = "Hola mi compadre: %s" % user_input
message = f"Hola mi compadre: {user_input}"
print(message)
'''

# Clase 55
'''
name = input("Nombre: ")
surname = input("Apellido: ")
message = "Hola: %s %s" % (name, surname)
message = f"Hola mi compadre: {name} {surname}"
print(message)
'''

# Clase 56

# Formatting Strings
## Implement a function that gets a person's name as a parameter and greets the person with Hi Person. For example, if I called your function using foo("Marry") the function should return Hi Marry .
def foo(name):
   return f"Hi {name}"

print(foo("Mary"))

# Formatting and Uppercase
## Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John). Note that the first letter of the person's name should always be uppercase.
def foo(name):
    uppername = name.title()
    msg = f"Hi {uppername}"
    return msg
    
print(foo("aaaaaa"))

