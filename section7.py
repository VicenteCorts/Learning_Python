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




