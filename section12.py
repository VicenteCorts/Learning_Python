# Clase 96
'''
import time

while True:
    with open("downloads/verduras.txt") as file:
        print(file.read())
        time.sleep(3)
'''

# Clase 97
'''
import time
import os

while True:
    if os.path.exists("downloads/verduras.txt"):
        with open("downloads/verduras.txt") as file:
            print(file.read())
    else:
        print("No existe el archivo")
    time.sleep(3)
'''

# Clase 98-99
''''''
import time
import os
import pandas

while True:
    if os.path.exists("downloads/temps_today.csv"):
        data = pandas.read_csv("downloads/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("No existe el archivo")
    time.sleep(3)










