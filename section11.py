# Clase 87
'''
myfile = open("downloads/fruits.txt")
print(myfile.read())

# Read Text From File and Print (E)
## On the side panel there's a bear.txt file. The existing code opens that file in read mode. Below that code, please read the file content and print out the content.
file = open("bear.txt")
print(file.read())
'''

# Clase 88
'''
myfile = open("downloads/fruits.txt")
he
print(content)
print(content)
'''

# Clase 89
'''
myfile = open("downloads/fruits.txt")
content = myfile.read()
myfile.close()
print(content)
'''

# Clase 90
'''
with open("downloads/fruits.txt") as myfile:
    content = myfile.read()

print(content)
'''

# Clase 92
'''
with open("downloads/verduras.txt", "w") as myfile:
    myfile.write("Tomate\nPepino\nCebolla\n")
    myfile.write("Ajo")

# Reading and Processing Text (E)
## Read the bear.txt file, and print out the first 90 characters of its content.
myfile = open("bear.txt")
print(myfile.read(90))

# File Processing Inside Function (E)
## Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.
def foo(a, b):
    with open(b, 'r') as file:
            content = file.read()
            return content.count(a)

# Write Snail (E)
## Use Python to create a file with name file.txt and write the text snail there.
with open("file.txt", "w") as myfile:
    myfile.write("snail")

# Write First 90 (E)
## Create a first.txt file that contains the first 90 characters of bear.txt. Note that you should read the content of bear.txt with Python, extract its first 90 characters with Python, and write those characters in first.txt with Python.
with open("first.txt", "w") as myfile:
    bearfile = open("bear.txt")
    content = bearfile.read(90)
    myfile.write(content)
'''

# Clase 93
with open("downloads/verduras.txt", "a+") as myfile:
    myfile.write("\nCipote")
    myfile.seek(0)
    content = myfile.read()

print(content)

# Read and Append (E)
## Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.
with open("bear2.txt", "a+") as myfile:
    bear1 = open("bear1.txt")
    content = bear1.read()
    myfile.write(content)


