# Clase 29
## En python 3.13 los "Better Error Messages" ya vienen por defecto, en versiones anteriores a la 3.10 no
'''
print("totai".replace("i","y"))
x = [1, 2, 3]
print("totai".replace("i","y"))
'''
# Clase 30
'''
monday_temperature = [9.1, 8.8, 7.5]

# Append Item to List (E)
## Append the value of current to the end of the list seconds Please use the list.append() method to do that.
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

# Remove Item from List (E)
## Remove item 1.45 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)

# Remove Three Items From List (E)
## Remove items 1.45, 1.02, and 1.11 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
new=seconds[0]
seconds.clear()
seconds.append(new)
print(seconds)
'''

# Clase 31
'''
monday_temperature = [9.1, 8.8, 7.5]
print(monday_temperature[1])

# Access Item (E)
## Complete the script so that it prints out the 3rd item of list serials.
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

# Access Multiple Items (E)
## Complete the script so that it prints out the 1st, 3rd, and the 6th items of the list serials.
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

# Access and Append (E)
## Append the first item of weekend to workdays.
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
'''

# Clase 32 y 34
'''
monday_temperature = [9.1, 8.8, 7.5, 6.6, 9.9]
'''

# Clase 35
'''
monday_temperature = ["hello", 1, 2, 3]

# Slicing a List, 2nd to 4th (E)
## Print out the slice ['b', 'c', 'd'] of the letters list using slicing.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

# Slicing a List, First Three (E)
## Print out the slice ['a', 'b', 'c'] of the letters list using slicing.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

# Slicing a List, Last Three (E)
## Print out the slice ['e', 'f', 'g'] of the letters list using slicing.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])
'''

# Clase 37
student_grades = {"Vicente": 10.0, "Maria": 9.5, "Carlos": 5.0}
eng_esp = {"rain" : "lluvia", "sun" : "Sol"}
