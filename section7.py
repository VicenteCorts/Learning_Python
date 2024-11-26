# Clase 59
'''
monday_temperature = [9.1, 8.8, 7.5]

for temp in monday_temperature:
    print(round(temp))

for letter in "Hello":
    print(letter)

# Loop Over Colors (E)
## Loop over the colors items and print out the item in every loop. 
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)

# Loop Over Big Colors (E)
## Loop over the colors items and print out the item in every loop only if the item is greater than 50. 
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color>50:
        print(color)

# Loop Over Integer Colors (E)
## Loop over the colors items and print out the item in every loop only if the item is an integer.
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if type(color) == int:
        print(color)

# Loop Over Int and Big Colors (E)
## Loop over the colors items and print out the item in every loop only if the item is an integer and it is greater than 50.
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if type(color) == int and color>50:
        print(color)
'''

# Clase 61
'''
student_grades = {"Vicente": 10.0, "Maria": 9.5, "Carlos": 5.0}
for grades in student_grades.items():
    print(grades)
#('Vicente', 10.0)
#('Maria', 9.5)
#('Carlos', 5.0)

for grades in student_grades.values():
    print(grades)
#10.0
#9.5
#5.0

for grades in student_grades.keys():
    print(grades)
#Vicente
#Maria
#Carlos
'''

# Clase 62
'''
# Dictionary Loop and String Formatting
## Make the code print out the following output using a for loop: John Smith: +37682929928 Marry Simpons: +423998200919 So, the code should loop over the dictionary items and in each iteration should print out the dictionary key, a colon, a space, and the corresponding value.
phone = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for item in phone.items():
    print(f"{item[0]}: {item[1]}")

# Loop Over Dictionary and Replace
## Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instead of '+'. In other words, your code should output: 0037682929928 00423998200919 Hint: You can access dictionary values with phone_numbers.values() and you can replace characters using str.replace() .
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for number in phone_numbers.values():
    print(number.replace("+", "00"))
'''

# Clase 63
'''
a = 3
while a < 10 :
    a = a+1
    print(a)
'''

# Clase 64
'''
username = ''
while username != "Vicente":
    username = input("Nombre de Usuario: ")
'''

# Clase 65




