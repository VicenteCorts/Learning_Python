# Clase 220
''' 
SQL ********************************************************************************
'''
'''import sqlite3

#########################
## Crear base de datos ##
#########################

def create_table():
    # 1. Crear la conexión - si no existe la base de datos, la crea
    conn = sqlite3.connect('bases_de_datos/lite.db')
    # 2. Crear un cursor
    cur = conn.cursor()
    # 3. Query SQL
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # 4. Commit
    conn.commit()
    # 5. Close Connection
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect('bases_de_datos/lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('bases_de_datos/lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect('bases_de_datos/lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect('bases_de_datos/lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()'''

'''insert('Coffe Cup', 10, 5)
update(11, 6, "Water Glass")
delete("Wine Glass")
print(view())'''

''' ********************************************************************************
hasta aquí el código para base de datos SQLlite'''

# Clase 223
''' POSTGRESQL '''
import psycopg

# Crear base de datos
def create_table():
    conn = psycopg.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#insert("Grapes", 10, 15)
#delete("Grapes")
update(20, 16, "Apple")
print(view())








