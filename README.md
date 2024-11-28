# Primeros Pasos con Python
## Instalación
- Nos dirigiremos a esta url (https://www.python.org/downloads/) y clicaremos en "downloads", nos descargaremos el ejecutable más actualizado para windows.
- Ejecutamos el archivo descargado y marcamos las dos opciones inferiores (install laucher y add to PATH); luego clicamos en **install now**.
- Posteriormente nos dirigimos a la consola (cmd) y escribimos el comando: py -3
- Si se muestra: ">>>" significa que python se ha instalado correctamente; ahora nos encontramos en la **consola de python**.
- Para salir de la consola python: exit()
- Para conservar el código que escribamos en la consola python necesitaremos un IDE
- En mi caso usaré **Visual Studio Code**
- Ya lo tengo instalado en mi ordenador (así que no profundizaré en la instalación de este).

## Clase 5
### Crear y correr un programa de Python
Creamos una nueva carpeta "**Python**" donde crearemos nuestro primer proyecto sencillo de Python
- Para empezar, debemos tener claro que la extensión para los archivos python es **.py**
- Sin embargo, haremos una primera prueba con un archivo "**my_program.txt**", acabado en .txt para ver su comportamiento.
```hmtl
print (3+4)
```
Abrimos una nueva terminal en VSCode para correr el programa: **barra superior>Terminal>New Terminal**
- escribimos py -3 my_program.txt
- nos devolverá un 7; el resultado del programa que hemos creado.

### Extensión de Python para "Run Button"
Nos dirigimos al símbolo de extensiones de VSCode y buscamos: **python**. Ahora si cambiamos la extensión del archivo de .txt a .py veremos que aparece el botón de "correr".
<br/>
<br/>
Posteriormente nos dirigimos a la parte inferior de VSC en la barra azul (habiendo seleccionado el archivo .py y clicamos en "**Python{}**) y seleccionamos el intérprete de Python.

## Clase 6
### Operadores matemáticos
```html
print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(10//5)
print(6%5)
print(5**3)
```

## Clase 7
### Tips
CTRL+, (Configuración de VSCode)

## Clase 8
### What (surprisingly) is Python?
Documentación de Python: https://docs.python.org/3/

## Clase 11
### Variables
```html
spent = 3
donated = 4
total = spent + donated
print(total)
```
Se debe evitar poner números al principio de las variables, tampoco se pueden poner espacios, si puede haber espacios entre la variable el operador "=" y el valor, pero lo correcto es un espacio.
<br/>
<br/>

## Clase 12
###  Tip
#### Imprimir múltiples variables
```html
items = 10
price = 2
 
total_price = items * price
 
# Below we print out three variables
print(total_price, items, price) 
Output: 20 10 2
```
#### Comentarios en python
Se declaran con el símbolo "#" al principio de la línea de código

## Clase 13
### Python Interactive Shell
Nos dirigimos a la temrinal de python dentro de VSCode; para ello escribimos: **py -3** --> Output: >>>
```html
>>> items = 3
>>> price = 2
>>> total = items *price
>>> print(total)
6
>>> 
```
La principal diferencia con la elaboración de código en archivos .py es que el código de la temrinal no se guarda en ningún sitio, mientras que el de archivo si queda con permanencia.
<br>
<br>
Tambiém destacar que en la terminal python no es necesario escribir "print"; directamente escribiendo la variable que queremos imprimir nos arroja el valor de esta:
```html
>>> total
6
>>> 
```
**Importante:** si alternamos el uso de "Run" del archivo y el uso de la terminal de forma nativa, debemos escribir **exit()**  y **py -3** para poder retomar el uso normal de la temrinal con código nativo o el "Run" de los archvios.

## Clase 14
### Terminal
Por normal general los programadores abren dos temrinales una para el "Run" y otra para usar la Python Interactive Shell. Para ello clicamos en la temrinal en la dobre ventana para que esta se divida en dos. Luego damos a **"RUN"** en una de ellas y en la otra escribimos el comando: **py -3** para hacer uso de la PIS (Python Interactive Shell).
<br>
<br>
Tip: Podemos limpiar la temrinal escribiendo **cls** (en la temrinal Run) o **clear** en la temrinal py -3

# Sección 3
## Clase 15
### Tipos: Integers, Strings y Floats
Trabajaremos sobre un nuevo archivo **basics.py** para ver los tipos de varaibles:
```html
x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

# Output:
20 1010
<class 'int'> <class 'str'> <class 'float'>
```
## Clase 16
### List Types
```html
students_grades = [9.1, 8.8, 7.5]
```

## Clase 17
###  Ranges
Haciendo pruebas con la variable students_grade de la clase anterior
```html
students_grades = [9, "Hello", [1,2,4.33]]
print(students_grades *3)
    # Output: [9, 'Hello', [1, 2, 4.33], 9, 'Hello', [1, 2, 4.33], 9, 'Hello', [1, 2, 4.33]]
print(students_grades + 3)
    # Output: Error syntax "+"cls
print(students_grades + students_grades)
    # Output: [9, 'Hello', [1, 2, 4.33], 9, 'Hello', [1, 2, 4.33]]
```
Ahora modificamos la variable por: **students_grades = range(0, 11)**
```html
students_grades = range(0, 11)
print(students_grades)
# Output: range(0,11)
```
A continuación cambiamos la variable por: **students_grades = list(range(0, 11))**
```html 
students_grades = list(range(0, 11))
print(students_grades)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

students_grades = list(range(1, 9))
print(students_grades)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
```
Podemos añadir un tercer argumento a la variable y ver como varía el output:
```html
students_grades = list(range(1, 9, 2))
print(students_grades)
# Output: [1, 3, 5, 7] -> da saltos de 2 en 2; siendo 2 el tercer argumento añadido
```

## Clase 19
### Data Types Attributes
La función **dir()** es una función específica de python que nos da una lista de todas las accioens que podemos con los diferentes tipos de datos:
```html
## Podemos escribir estos comandos en la terminal py -3
dir(list)
# Output: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir(int)
# Output: ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes'] 
dir(str)
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
dir(float)
# Output: ['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```
También podemos profundizar en alguno de estos métodos a través de la consola py -3, por ejemplo tomemos el comando: **help(str.upper)**
```html
help(str.upper)
# Output: Help on method_descriptor:

upper(self, /) unbound builtins.str method    Return a copy of the string converted 
to uppercase.
```
Y al hacer uso del método en la temrinal py -3:
```html
"hello".upper()
Output: 'HELLO'

"hello".title()
Output: 'Hello'
```

## Clase 21
### Encontrando el Código que necesitas
Además de los métodos específicos para los diferentes tipos de datos, podemos encontrar funciones para emplear en neustro código. Por ejemplo **print()** es una función que no pertenece a ningún tipo de dato. Para mostrar una lista de funciones mediante la temrinal **py -3** podemos emplear el comando: dir(__builtins__):
```html
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 
'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 
'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```
Así con la combinación de algunos de estos métodos como **sum** o **len** podemos realizar la media de notas de la variable que tenemos en clases anteriores:
```html
students_grades = [9.1, 8.8, 7.5]
mysum = sum(students_grades)
mylen = len(students_grades)

media = mysum/mylen
print(media)

# Output: 8.466666666666667
```

## Clase 22
### Dictionary Types
Emplearemos el tipo "diccionario" cuando queremos que una lista tenga un tipo de identidad unida a ella; en el ejemplo de la nota media del alumnado, trabajar con listas esta bien para carcular dicha media, pero si queremos atribuírsela a un alumno en concreto debemos hacer uso de los tipos "diccionario":
```html
# syntax: student_grades = {}

# LIST
students_grades = [9.1, 8.8, 7.5]
# Dictionary
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
---------------------------------------------------------
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(students_grades.values())
mylen = len(students_grades)

media = mysum/mylen
print(media)
print(students_grades.keys())

# Output: 8.466666666666667 dict_keys(['Marry', 'Sim', 'John'])
```
En el ejemplo anterior prestad atención a **students_grades.values()** y **students_grades.keys()**

## Clase 24
### Qué hace al programador un buen programador:
- Syntaxis: paréntsis, comas, llaves, puntos, etc...
- Data structure: saber el tipo correcto de la variable que estás creando
- Algorithm: creación de métodos que ejecuten la acción que queremos

## Clase 25
### Tuplas
Una tupla se diferencia de una lista por la forma de declararlos: tuplas con paréntesis y listas con braquets:
```html
# LIST
monday_temperature = [1, 4, 5]
# DICT
monday_temperature = ["morning": 1, "noon": 4, "evening": 5]
# TUPLA
monday_temperature = (1, 4, 5)
```
Esta sería la principal diferencia en cuanto a syntaxis pero, la verdadera diferencia reside en que las **Tuplas** son inmutables, mientras que las listas son mutables. **Algo inmutable significa que no se le pueden añadir más elementos** por ejemplo:
```html
## Tupla -> inmutable, no se le pueden añadir más elementos
monday_temperature = (1, 4, 5)
print(monday_temperature)

## Lista -> se pueden añadir más elementos
monday_temperature2 = [1, 4, 5]
monday_temperature2.append(6)
print(monday_temperature2)
```

## Clase 26
### Usando Datatypes en el mundo real
Existen formas automatizadas de escribir la información de docuemntos de texto o excels en formato de código, para ello es importante determinar que datatype debe tener cada tipo de dato o información.
<br><br>
Para ello, se hace uso de extensiones específicas de Python para cargar los datos a las variables que deseemos directamente desde los archivos con los que tengamos que trabajar.

## Clase 27
### Cheatsheet: Data Types
#### Integers 
used to represent whole numbers:
```html
rank = 10
eggs = 12
people = 3
```

#### Floats 
represent decimal numbers:
```html
temperature = 10.2
rainfall = 5.98
elevation = 1031.88
```

#### Strings 
represent text:
```html
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
```

#### Lists 
represent arrays of values that may change during the course of the program:
```html
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
```

#### Dictionaries 
represent pairs of keys and values:
```html
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
```

#### Keys of a dictionary 
can be extracted with:
```html
phone_numbers.keys()
```

#### Values of a dictionary 
can be extracted with:
```html
phone_numbers.values()
```

#### Tuples 
represent arrays of values that are not to be changed during the course of the program:
```html
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

#### dir()
You can get a list of attributes of a data type has using:
```html
dir(str)
dir(list)
dir(dict)
```

#### dir(__builtins__)
You can get a list of Python builtin functions using:
```html
dir(__builtins__)
```
#### help()
You can get the documentation of a Python data type using:
```html
help(str)
help(str.replace)
help(dict.values)
```

# Sección 4
## Clase 29
###  Tip: Better Error Messages in Python 3.13
En python 3.13 los "Better Error Messages" ya vienen por defecto, en versiones anteriores a la 3.10 no
```html
print("totai".replace("i","y")
x = [1, 2 3]
print("totai".relpace("i","y"))
```
En cada uno de los ejemplos la temrinal nos arroja un error con una explicación que puede ser la solución directa al error que hemos generado.

## Clase 30
### Operadores con Listas
Empleamos dir(list) en la consola **py -3** y vemos la lista de operaciones posibles con los datos "Lista":
<br><br>
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
<br><br>
Hacemos uso de algunos de estos directamente en la temrinal **py -3**
```html
>>> monday_temperature = [9.1, 8.8, 7.\5]
>>> monday_temperature.append(8.1)
>>> monday_temperature
[9.1, 8.8, 7.5, 8.1]
>>> monday_temperature.clear()
>>> monday_temperature
[]
>>> monday_temperature = [9.1, 8.8, 7.5]
>>> monday_temperature.index(8.8)
1
>>> 
```

## Clase 31
### Acceder a un item de la lista
Para acceder a un item concreto emplearíamos el método **'getitem'**; veámoslo en la temrinal **py -3**:
```html
>>> monday_temperature = [9.1, 8.8, 7.5]
>>> monday_temperature.__getitem__(1)
8.8
```
Pero para hacerlo de modo más sencillo podemos emplear la siguiente sintaxis:
```html
>>> monday_temperature[1]
8.8
```

## Clase 32
### Accessing List Slices
Trabajaremos con una lista de 5 elementos a través de la temrinal de comandos **py -3**; estaremos trabajando con "slices", es decir, fragmentos extraídos de la lista por bloques:
```html
>>> monday_temperature = [9.1, 8.8, 7.5, 6.6, 9.9]
>>> len(monday_temperature)
5
>>> monday_temperature[3]
6.6
>>> monday_temperature[1:3]
[8.8, 7.5]
>>> monday_temperature[1:4]
[8.8, 7.5, 6.6]
>>> 
```
El ultimo valor del Slice no se incluye en el fragmento extraído: [1:4] extrae el valor del índice 1, 2 y 3.
<br><br>
Como último dato, en caso de querer extraer un Slice desde el índice 0, no es necesario indicar el número 0 entre los corchetes (seguríamos la misma sintaxis para extraer desde un índice cualquiera hasta el final de la lista):
```html
>>> monday_temperature[:4]
[9.1, 8.8, 7.5, 6.6]
>>> monday_temperature[2:]
[7.5, 6.6, 9.9]
```

## Clase 34
### Accessing List Slices whit negative indexes
Siguiendo la línea del apartado anterior, para acceder a índices de una lista con una gran cantidad de valores, puede ser engorroso contar de valor en valor hasta llegar a un índice del final que nos interese para saber su número. Para ello empleamos **índices negativos**:
```html
>>> monday_temperature[-1]
9.9
```
También se pueden hacer Slices empleando índices negativos:
```html
>>> monday_temperature[-2:]
[6.6, 9.9]
>>> monday_temperature[-4:-2]
[8.8, 7.5]
>>> monday_temperature[:-2]
[9.1, 8.8, 7.5]
```

## Clase 35
### Accessing Characters and Slices in Strings
En caso de los String el mecanismo para acceder a los índices del propio string y los slices funcionan de la mimsa forma, con sus índices positivos, negativos, sus slices, etc... 
```html
>>> mystring = "hello"
>>> mystring[1]
'e'
>>> mystring[-1]
'o'
>>> mystring[:3]
'hel'
```
Otro ejemplo combinado con el datatype "Lista"
```html
>>> monday_temperature = ["hello", 1, 2, 3]
>>> monday_temperature[0]
'hello'
>>> monday_temperature[0][2]
'l'
>>> 
```

## Clase 37
###  Accessing Items in Dictionaries
De igual forma, veremos como acceder a los items de los datatypes "Dictionaries"; en este caso para acceder a los índices no podemos referenciarlos con el número que le corresponde por su orden, sino con el nombre de la **key**:
```html
>>> student_grades = {"Vicente": 10.0, "Maria": 9.5, "Carlos":\ 5.0}
>>> student_grades[1]
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    student_grades[1]
    ~~~~~~~~~~~~~~^^^
KeyError: 1 
>>> student_grades["Vicente"]
10.0
----------------------------------------------------
>>> eng_esp = {"rain" : "lluvia", "sun" : "Sol"}
>>> eng_esp["sun"]
'Sol'
```

## Clase 38
### Tip: Converting Between Datatypes
Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

#### From tuple to list:
```html
>>> cool_tuple = (1, 2, 3)
>>> cool_list = list(cool_tuple)
>>> cool_list
[1, 2, 3]
```

#### From list to tuple:
```html
>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> cool_tuple
(1, 2, 3)
```

#### From string to list:
```html
>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']
```

#### From list to string:
```html
>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'
```
As can be seen above, converting a **list into a string** is more complex. Here str() is not sufficient. We need str.join(). Try running the code above again, but this time using str.join("---", cool_list) in the second line. You will understand how str.join() works.

## Clase 39
### Cheatsheet: Operations with Data Types
In this section, you learned that:

#### Lists, strings, and tuples have a positive index system:
```html
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
```
And they have a negative index system as well:
```html
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
```
#### In a list, the 2nd, 3rd, and 4th items can be accessed with:
```html
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']

First three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 

Last three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']

Everything but the last:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

Everything but the last two:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
```
#### A dictionary value can be accessed using its corresponding dictionary key:
```html
phone_numbers = {"John":"+37682929928","Marry":"+423998200919"}
phone_numbers["Marry"]
Output: '+423998200919'
```
# Sección 5
## Clase 41
### Creando tus propias funciones
Para crear una función en python se emplea la palabra reservada **def** seguida del nombre que queramos darle a la función y **():** y finaliza con un **return**.
```html
# Ejemplo de función para hacer una media
def media (mylist):
    la_media = sum(mylist) / len(mylist)
    return la_media

print(media([1, 4, 5]))
``` 
Otro ejemplo: función para hacer conversiones de dinero
```html
def convert(amount):
    output = amount * 1.75
    return output
 
print(convert(10))
```

## Clase 43
### Print or Return?
Cuando declaramos una función sin return nos devuelve un "None". Es importante que dentro de una función respetemos 4 espacios al comienzo de cada línea de código de la función.
<br><br>
Si intentamos emplear un print en vez de return dará error, podemos emplear un return "sin uso" para poder acometer la función al menos:
```html
def media (mylist):
  la_media = sum(mylist) / len(mylist)
  return la_media
mymean = media([0, 3, 4])
print(mymean)
```

## Clase 44
### Condicionales
Sin embargo, a la hora de trabajar en funciones como la de calcular la media de clases anteriores, intentamos trabajar con una variable de tipo dictionary nos lanzará un error ya que esta función trabaja con listas, no con dictionaries.
<br><br>
Para solucionar esto haremos uso de los condicionales como veremos en las siguientes clases

## Clase 45
### IF
A continuación veremos un ejemplo de condicional para solucionar el problema anterior
```html
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
```

## Clase 46
### Explicacion del condicional
(...)

## Clase 47
### Más Condicionales
Los condicionales pueden emplearse tanto dentro como fuera de las funciones. Existen más tipos de condicionales a parte del **IF** como veremos en las siguientes clases

## Clase 48
### Boolean Operators "and" and "or"
So far, you learned how to check for one single condition:
```html
x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")
```

You can also check if two conditions are met at the same time using an and operator:
```html
x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
That will return Yes since x == 1 and y ==1 are both True.
```

You can also check if one of two conditions are met using an or operator:
```html
x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
That will return Yes since at least one of the conditions is True. In this case x == 1 is True.
```

## Clase 49
### ELIF
Ejemplo
```html
x = 3
y = 1
if x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual que y")
else:
    print ("x es menor que y")
```

## Clase 50
### Espacios en blanco
Ahora veremos cuando es importante usar un espacio en blanco, cuando usar más de uno o cuando no utilizar ninguno:
```html
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
```
Todos los bloques funcionarían correctamente pero la manera correcta por buenas prácticas sería el bloque **b**.

## Clase 51
### Cheatsheet: Functions and Conditionals
In this section, you learned to:
#### Define functions:
```html
def cube_volume(a):
    return a * a * a
```
#### Write if-else conditionals:
```html
message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
```
#### Write if-elif-else conditionals:
```html
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
```
#### Use the and operator to check if both conditions are True at the same time:
```html
x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
```
#### Use the or operator to check if at least one condition is True:
```html
x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
```
#### Check if a value is of a particular type with isinstance:
```html
isinstance("abc", str)
isinstance([1, 2, 3], list)
or directly:

type("abc") == str
type([1, 2, 3]) == list
```

# Sección 6
## Clase 53
### User Input
En ese apartado abordaremos como codificar neustro código para que el ususario objetivo pueda interactuar con él a través de la función **input()**:
```html
def foo(temp):
    if temp > 7:
        return "Warm"
    else:
        return"Cold"

user_input = float(input("Introduce una temperatura:"))
print(foo(user_input))
```
En este caso es necesario transformar el input del ususario en un valor numérico o float mediante la función **float()**, sino nos dará error por incompatibilidad de tipos de datos.
<br><br>
Input() siempre recoge la información del usuario en **str**.

## Clase 54
### String Formatting
Ahora veremos como generar respuestas al usuario mediante **String Formatting** --> **(Py 2 & 3)** en el mensaje a mostrar debemos añadir **%s** donde queramos introducir alguna variable ya declarada, es decir, el nombre que introducirá el usuario; seguido de **% nombre_de_la_variable**:
```html
user_input = input("Cuálm es tu nombre compadre? ")
message = "Hola mi compadre: %s" % user_input
print(message)
```
Otro modo de hacerlo es mediante el prefijo **f** antes del mensaje y el nombre de la variable que queremos reflejar entre llaves: **(Py 3.6 & later)**
```html
user_input = input("Cuálm es tu nombre compadre? ")
message = f"Hola mi compadre: {user_input}"
print(message)
```

## Clase 55
### Strinf Formatting para múltiples variables
En caso de que queramos plasmar más de una variable en ejemplos como el anterior, debemos escribir nuestro código de la siguiente manera:
```html
# (Py 2 & 3)
name = input("Nombre: ")
surname = input("Apellido: ")
message = "Hola: %s %s" % (name, surname)
print(message)
-------------------------------------------------
# (Py 3.6 & later)
name = input("Nombre: ")
surname = input("Apellido: ")
message = f"Hola mi compadre: {name} {surname}"
print(message)
```
En el html anterior mostramos las dos formas para plasmar variables de input.

## Clase 56
### More String Formatting
There is also another way to format strings using the "{}".format(variable) form. Here is an example:
```html
name = "John"
surname = "Smith"

message = "Your name is {}. Your surname is {}".format(name, surname)
print(message)
Output: Your name is John. Your surname is Smith
```

## Clase 57
### Cheatsheet: Processing User Input
In this section, you learned that a Python program can get user input via the input function:
```html
The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")
----------------------------------------------------

The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12

-----------------------------------------------------
You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.
```
# Section 7
## Clase 59
### Bucle For
De cursos anteriores ya sabemos lo que es un bucle **for**. En este apartado veremos cómo declararlo en Python:
```html
monday_temperature = [9.1, 8.8, 7.5]

# Forma burda de recorer la lista

print(round(monday_temperature[0]))
print(round(monday_temperature[1]))
print(round(monday_temperature[2]))

# Bucle para recorrer la lista

for temp in monday_temperature:
    print(round(temp))

# Otro ejemplo

for letter in "Hello":
    print(letter)
```

## Clase 60
### For Loop Over a Function
A for loop can also be used to execute a function multiple times. For example, below we are executing celsius_to_kelvin three times since there are three items in the iterating list:
```html
def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))


The output of that would be:

282.25
281.95
3.0
```
So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

## Clase 61
### Bucle en dato dictionary
A la hora de iterar un **dict** debemos especificar con qué elemnto queremos trabajar, diferenciando entre item (tupla), valor o key:
```html
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
```
## Clase 62
### Dictionary Loop and String Formatting
Here is an example that combines a dictionary loop with string formatting. The loop iterates over the dictionary and it generates and prints out a string in each iteration:
```html
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")
```
And here is a better way to achieve the same results by iterating over keys and values:
```hyml
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")
```
In both cases, the output is:
```html
John has as phone number +37682929928
Marry has as phone number +423998200919
```

## Clase 63
### Bucle While
De cursos anteriores ya sabemos lo que es un bucle **While**. En este apartado veremos cómo declararlo en Python:
```html
a = 3
while a < 10 :
    a = a+1
    print(a)
```

## Clase 64
### Bucle While con User_input
A continuación, otro ejemplo de **While** en combinación con user_input:
```html
username = ''
while username != "Vicente":
    username = input("Nombre de Usuario: ")
```

## Clase 65
### While: Break & Continue
Ahora abordaremos el funcionamiento de las palabras claves **Break & Continue** Empleadas dentro de los bucles while de manera optativa:
```html
while True :
    username = input("Nombre de Usuario: ")
    if username == "pypy":
        break
    else:
        continue
```

## Clase 66
### Cheatsheet: Loops
In this section, you learned:
#### A for-loop is useful to repeatedly execute a block of code.
```html
You can create a for-loop like so:

for letter in 'abc':
    print(letter.upper())
Output:

A
B
C
```
As you can see, the for-loop repeatedly converted all the items of 'abc' to uppercase.

#### The name after for (e.g. letter) is just a variable name
```html
You can loop over dictionary keys as follows:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
Output:

John Smith
Marry Simpsons
```
#### You can loop over dictionary values:
```html
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
Output:

+37682929928
+423998200919
```
#### You can loop over dictionary items:
```html
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
Output: 

John Smith +37682929928
Marry Simpons +423998200919
```
#### We also have while-loops. The code under a while-loop will run as long as the while-loop condition is true:
```html
while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.
```

# Section 8
## Clase 69-72
### "Problem Statement"
Ahora pondremos en común todo lo aprendido hasta el momento, para ello crearemos un programa en el que empleemos todos los elementos juntos:
```html
def frase (cadena):
    interrogacion = ("qué", "cómo", "cuándo", "quién", "por qué")
    mayus = cadena.capitalize()
    if cadena.startswith(interrogacion):
        return "¿{}?". format(mayus)
    else:
        return "{}.".format(mayus)

result = []

while True:
    user_imput = input("Escribe algo: ")
    if user_imput == "/end":
        break
    else:
        result.append(frase(user_imput))

print(" ".join(result))
```
# Section 9
## Clase 74
### List Comprehension (Loops para listas)
En el ejemplo de las temperaturas, para ahorrar espacio en algunas programaciones establecen archivos con los datos, en los que los floats aparecen como números enteros sin punto, es decir, habría que dividirlos entre 10 para obtener el valor auténtico. Es en este tipo de  casos dodne las **List Comprehensions** ebtran a jugar.
```html
# ejemplo con for
temps = [221, 234, 340, 230]

new_temps = []

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)
--------------------------------
# ejemplo con List Comprehension
temps = [221, 234, 340, 230]

new_temps = [ temp / 10 for temp in temps]

print(new_temps)
```

## Clase 75
### List Comprehension + IF
Siguiendo lo aprendido en la clase anterior, también podemos añadir condicionales a los **LC**:
```html
temps = [221, 234, 340, -9999, 230]

new_temps = [ temp / 10 for temp in temps if temp != -9999]

print(new_temps)
```

## Clase 76
### List Comprehension with If-Else Conditional
Siguiendo el ejemplo anterior:
```html
```
Destacar que en este caso el orden se invierte; es decir, primero iría la operación (en ambos ejemplos igual), pero luego iría primero el condicional **if-else** y luego el **bucle for**

## Clase 77
### Cheatsheet: List Comprehensions
In this section, you learned that:

#### A list comprehension is an expression that creates a list by iterating over another container.
```html
A basic list comprehension:

[i*2 for i in [1, 5, 10]]
Output: [2, 10, 20]

List comprehension with if condition:

[i*2 for i in [1, -2, 10] if i>0]
Output: [2, 20]

List comprehension with an if and else condition:

[i*2 if i>0 else 0 for i in [1, -2, 10]]
Output: [2, 0, 20]
```
# Section 10
## Clase 79
### Funciones con múltiples argumentos
Tan sencillo como:
```html
def area (a, b):
    return a * b
print(area(4, 5))
```

## Clase 81
### Default and Non-default Parameters and Keyword and Non-keyword Arguments
Llamamos keyword-arguments a aquellos que vienen definidos en la entrada de parámetros:
```hmtl
# Non-KWA
def area (a, b):
    return a * b
print(area(4, 5))

# Keyword-Arguments
def area (a = 5 , b = 4):
    return a * b
```
Esto también está asociado a la posición de los parámetros:
```html
def area (a, b):
    return a * b
print(area(b = 4, a = 5))
```
Aquí las variables a y b están en orden opuesto, pero seguirían entrando con sus respectivos nombrameintos.
#### Parámetros default
Parámetros que ya vienen definicdos en la función y no es necesario volver a llamar para ejecutarla:
```html
def area (a, b = 5):
    return a * b
print(area(4))
```
Incluso podríamos asignar un valor diferente a **b** simplemente incluyéndolo como parámetro en la llamada a la fucnión
```html
def area (a, b=5):
    return a * b
print(area(4, b = 7))

o

print(area(4, 7))

# en este ejemplo b tendría el valor "7"
``` 
**Hay que tener en cuenta que los parámetros default NO pueden estar delante de los no default**
```html
def area (a=5, b):
    return a * b
print(area(4, 7))

# ERROR
```

## Clase 82
### Functions with an Arbitrary Number of Non-keyword Arguments
Hay funciones que tiene un número predefinido de parámetros. Al añadir más o menos de los que exigen, dará error:
```html
>>> len('hello')
5   
>>> len('hello', 'hi')
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    len('hello', 'hi')        
    ~~~^^^^^^^^^^^^^^^        
TypeError: len() takes exactly one argument (2 given) 
-------------------------------
>>> isinstance(6, int)
True
>>> isinstance(6, int, int)
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    isinstance(6, int, int)   
    ~~~~~~~~~~^^^^^^^^^^^^^   
TypeError: isinstance expected 2 arguments, got 3
------------------------------
# Otras funciones no tienen un número predefinido de parámetros:
>>> print(1,2,3,4,5)
1 2 3 4 5
```
#### Crear funciones con número de parámetros indefinidos:
Para crear una función con estas características la declararemos de la sigueinte fomra:
```html
def mean(*args):
    return sum(args)/len(args)
print(mean(1, 6, 3))
```

## Clase 83
### Functions with an Arbitrary Number of Keyword Arguments
PAra crear funciones sin un número predeterminado de parámetros y que además estos sean kw (keywords) se realizaría añadiendo dos asteriscos en vez de 1 entre los paréntesis de la declaración de la función:
```html
def mean(**kwargs):
    return kwargs
print(mean(a=1, b=6, c=3))

# Nos devolvería un dict: {'a': 1, 'b': 6, 'c': 3}
```

## Clase 84
### Cheatsheet: More on Functions
In this section, you learned that:

#### Functions can have more than one parameter:
```html
def volume(a, b, c):
    return a * b * c
```
#### Functions can have default parameters (e.g. coefficient):
```html
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))
Output: 3.0480370641306997
```
#### Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):
```html
def volume(a, b, c):
    return a * b * c
 
print(volume(1, b=2, c=10))
```
#### An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:
```html
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
Output: 1001
```
#### A **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
```html
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
Output: Sim
```
#### Here's a summary of function elements:
![imagen resumen sección 10](/img/Clase84.png)

# Section 11
## Procesar archvios en Python
Al abrir archivos a través de Python, se emplea una parte de la memoria temporal (RAM)

## Clase 87
### Leer Text de un archivo
Debemos abrir el archivo con el que vamos a trabajar y posteriormente imprimirlo para ver su contenido
```html
myfile = open("downloads/fruits.txt")
print(myfile.read())
```

## Clase 88
### File Cursos
Cuando creamos el objeto "file" al abrir el archivo y empleamos el método .read(), el "cursor" se sitúa al final del archvio, por lo que si volvemos a ejecutar el método .read() nos devolverá una respuesta vacía (ya que no hay nada más al final del archivo).
- Es importante tener en cuenta este concepto del **cursor**
- Si queremos imprimir el contenido del archivovarias veces podemos hacer lo sigueinte:
```html
myfile = open("downloads/fruits.txt")
content = myfile.read()
print(content)
print(content)
```

## Clase 89
### Cerrar el archvio
```html
myfile = open("downloads/fruits.txt")
content = myfile.read()

myfile.close()

print(content)
```

## Clase 90
### Abrir archvios con "with"
Con with-as podemos abrir y manipulat los archivos de igual forma que con los ejemplos anteriores, con la salvedad de que al temrinar el bloque de código precedido por el **with**, el arhcivo se cierra automáticamente:
```html
with open("downloads/fruits.txt") as myfile:
    content = myfile.read()

print(content)
```
Este código haría exactamente lo mismo que el de la clase anterior.

## Clase 91
### Diferentes rutas de archivos
Tener en cuenta dónde se ubica el archiv para llamarlo correctamente en nuestro código(...)

## Clase 92
### Escribir texto en un archivo
help(open)-> Nos muestra los diferentes métodos y parámetros para abrir archivos. A continuación cambiaremos el "mode" de "r" a "w" para poder escribir texto en un nuevo archivo:
```html
with open("downloads/verduras.txt", "w") as myfile:
    myfile.write("Tomate")
```
Al ejecutar este código, crea un nuevo archivo "verduras.txt" en la ruta especificada si no existe, y escribe la palabra "Tomate".
- **CUIDADO** con este código puede sobreescribirse el archivo.
#### Escribir una nueva línea:
```html
with open("downloads/verduras.txt", "w") as myfile:
    myfile.write("Tomate\nPepino\nCebolla")

# verduras.txt
Tomate
Pepino
Cebolla
-------------------------------------------
# Si hacemos lo siguiente, las palabras Cebolla y Ajo aparecerán juntas en la misma línea del archivo
with open("downloads/verduras.txt", "w") as myfile:
    myfile.write("Tomate\nPepino\nCebolla")
    myfile.write("Ajo")

# verduras.txt
Tomate
Pepino
CebollaAjo
```

## Clase 93
### Append texto a un archivo ya existente
#### modo "X"
Si en el modo de apertura del archivo sustituimos la "r" o "w" por **"x"**, crearemos un nuevo archivo con el nombre indicado. La "x" nos infomra de que el archivo a tratar ya está creado
```html
with open("downloads/verduras.txt", "x") as myfile:
    myfile.write("Cipote")

# FileExistsError: [Errno 17] File exists: 'downloads/verduras.txt'
```
#### modo "A"
Este es el modo que nos permite añadir texto sin sobreescribir:
```html
with open("downloads/verduras.txt", "a") as myfile:
    myfile.write("\nCipote")
```
#### modo "+"
Si queremos leer y escribir al mismo tiempo, añadiremos un "+" al modo indicado:
```html
with open("downloads/verduras.txt", "a+") as myfile:
    myfile.write("\nCipote")
    content = myfile.read()

print(content)
```
**IMPORTANTE** el output de este archivo será un espacio en blanco, ya que al añadir la nueva palabra, el **CURSOR** se establece al final del archivo. Para solucionar esto añadimos **myfile.seek(0)** para situarlo en el elemento 0 del archivo:
```html
with open("downloads/verduras.txt", "a+") as myfile:
    myfile.write("\nCipote")
    myfile.seek(0)
    content = myfile.read()

print(content)
```

## Clase 94
### Cheatsheet: File Processing
In this section, you learned that:

#### You can read an existing file with Python:
```html
with open("file.txt") as file:
    content = file.read()
```
#### You can create a new file with Python and write some text on it:
```html
with open("file.txt", "w") as file:
    content = file.write("Sample text")
```
#### You can append text to an existing file without overwriting it:
```html
with open("file.txt", "a") as file:
    content = file.write("More sample text")
```
#### You can both append and read a file with:
```html
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
```

# Section 12
## Clase 96
### Built in Modules
Podemos acceder a la lista de **métodos** buildin mediante: **dir(__builtins__)** en la temrinal py -3:
```html
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 
'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 
'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']     
>>> 
```
#### Módulos
Para acceder a los módulos disponibles de cara a instalarlos:
- En concreto instalaremos el módulo **time** y haremos uso de **time.sleep**:
```html
>>> import sys
>>> sys.builtin_module_names
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_interpchannels', '_interpqueues', '_interpreters', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', '_sha3', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_sysconfig', '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref', '_winapi', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
>>>
--------------------------------------------
>>> import time
>>> dir(time)
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']
>>> help(time.sleep)
Help on built-in function sleep in module time:   

sleep(object, /)
    sleep(seconds)

    Delay execution for a given number of seconds. 
 The argument may be
    a floating-point number for subsecond precision.

>>> 
```
Como ejemplo este bucle while se ejecuta de forma constante, pero haciendo uso de sleep se ejecutará infinitamente cada 3 segundos:
```html
import time

while True:
    with open("downloads/verduras.txt") as file:
        print(file.read())
        time.sleep(3)

# Para abortar ctrl + C
```

## Clase 97
### Módulos Estándar
Son módulos que vienen predefinidos en python

#### OS
C:\Users\Vicente Corts León\AppData\Local\Programs\Python\Python313\Lib
<br>

https://docs.python.org/3/library/os.html
<br>

Módulo para controlar el sistema operativo. Puede hacer que un script siga ejecutándose auque lance un error (para retomar una función en cuanto se fixee):
```html
>>> import os
>>> dir(os)
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', 
'_walk_symlinks_as_files', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 
'curdir', 'defpath', 'device_encoding', 'devnull', 
'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchmod', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_blocking', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'lchmod', 'linesep', 'link', 'listdir', 'listdrives', 'listmounts', 
'listvolumes', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'process_cpu_count', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_blocking', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
>>> 
```
Ejemplo de uso:
```html
# Para ver que el path de un archivo existe
>>> os.path.exists("downloads/verduras.txt"ras.txt")
True
>>> 
--------------------------------------------
# Tenemos un bucle while que se repite sin fin en el que accedemos a un archivo, en caso de que este falte, podrá seguir funcionando:
import time
import os

while True:
    if os.path.exists("downloads/verduras.txt"):
        with open("downloads/verduras.txt") as file:
            print(file.read())
    else:
        print("No existe el archivo")
    time.sleep(3)
```
## Recapitulación de Módulos
### módulos builtin
Existen módulos builtin que pueden ser de dos tipos:
- C: módulos a cuya información podemos acceder mediante **dir(__builtins__)**
- Python: módulos cuyos archivos se encuentran en nuestro equipo.
<br>
Ambos tipo se módulos son utilizables mediante la importación en el archivo del código.

### módulos de terceros
Existen también módulos de terceros que veremos en las próximas clases. Estos precisan de su instalación para poder hacer uso de ellos.

## Clase 98
### Módulos de Terceros
Para comenzar en este apartado debemos hacer uso de **pip**, una libreria default empleada para instalar librerias de terceros.
<br>

Mediante **pip** queremos instalar **pandas**, una librería de terceros muy versatil. Para nuestra versión de python debemos usar el sigueinte comando para instalar pandas a través de pip:
```html
>>>exit()
pip install pandas
# Yo personalmente he upgradeado la versión a la que me decía la consola que había como versión actualizada
python.exe -m pip install --upgrade pip
```
Ahora podemos hacer uso de **pandas** en nuestro script. Documentación de pandas: https://pandas.pydata.org/docs/

## Clase 99
### Ejemplo básico de Pandas
Más tarde trabajaremos en profundidad con Pandas, pero por el momento veamos alguno de sus usos.
```html
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
```
Con pandas creamos un tipo de objeto nuevo propio de esta libreria al usar: "data = pandas.read_csv("downloads/temps_today.csv")". Podemos ver este nuevo objeto en la temrinal py -3:
```html
>>> import pandas
>>> data = pandas.read_csv("downloads/temps_today.csv")
>>> data
    st1   st2
0  23.3  22.1
1  24.0  23.1
2  22.1  20.2
3  19.1  16.8                                       
>>> type(data)
<class 'pandas.core.frame.DataFrame'>
>>> 
```

## Clase 100
### Cheatsheet: Imported Modules
In this section, you learned that:

- **Builtin objects** are all objects that are written inside the Python interpreter in C language.

- **Builtin modules** contain builtins objects.

- **Some builtin objects** are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:
```html
import time
time.sleep(5)
```
- A **list of all builtin modules** can be printed out with:
```html
import sys
sys.builtin_module_names
```
- Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

- Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

- Packages are a collection of .py modules.

- **Third-party libraries** are packages or modules written by third-party persons (not the Python core development team).

- Third-party libraries can be **installed from the terminal/command line**:
```html
Windows:

pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:

pip3 install pandas or use python3 -m pip install pandas if that doesn't work.
```

# Section 13
## Clase 102
### Pandas: Librería de Data Analysis
Panda permite el manejo de datos a través de python. También cabe destacar la figura de bokeh que veremos más adelante.

## Clase 103
### Installing pandas
Please make sure you have **pandas** installed. You can install it with pip from your computer or Atom/VS Code terminal/cmd just like you have installed other third-party packages. Please execute one of the commands below to do the installation depending on what version of Python you are using:
```html
pip3.13 install pandas
```
Also, in the next lecture, we will use an enhanced Python interactive shell called IPython.
<br>

**IPython** is just like the standard shell you get when you run Python, but IPython provides better printing for large text. This ability makes IPython suitable for data analysis because the program prints data in a well-structured format. You can install IPython with pip:
```html
pip3.13 install ipython
```

## Clase 104
### Pandas: Comenzando
En la consola (normal) escribimos: **ipython**, para abrir la temrinal **Ipython** -> diseñada para el data analisis y trabajar con datos. [También cabe destacar **Jupyter Notebook**, que veremos más adelante.]. Ahora comenzaremos a emplear ipython:
- df -> data frame
```html
#consola normal: 
ipython

# consola ipython
In [1]: import pandas

In [2]: df1=pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

In [3]: df1
Out[3]:
    0   1   2
0   2   4   6
1  10  20  30

In [4]: df1=pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["price", "age", "value"])

In [5]: df1
Out[5]: 
   price  age  value
0      2    4      6
1     10   20     30

In [6]: df1=pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["price", "age", "value"], index=["First", "Second"])

In [7]: df1
Out[7]: 
        price  age  value
First       2    4      6
Second     10   20     30

In [8]: df2=pandas.DataFrame([{"Name":"Vicente"}, {"Name":"Maria"}])

In [9]: df2
Out[9]: 
      Name
0  Vicente
1    Maria

In [10]: df2=pandas.DataFrame([{"Name":"Vicente", "Apellido":"Corts"}, {"Name":"Maria"}])

In [11]: df2
Out[11]: 
      Name Apellido
0  Vicente    Corts
1    Maria      NaN

In [12]: df1
Out[12]: 
        price  age  value
First       2    4      6
Second     10   20     30

In [13]: type(df1)
Out[13]: pandas.core.frame.DataFrame

In [14]: dir(df1)
Out[14]: 
['T',
 '_AXIS_LEN',
 '_AXIS_ORDERS',
 '_AXIS_TO_AXIS_NUMBER',
 '_HANDLED_TYPES',
 '__abs__',
 '__add__',
 '__and__',
 '__annotations__',
 '__array__',
 '__array_priority__',
 '__array_ufunc__',
 '__arrow_c_stream__',
 '__bool__',
 '__class__',
 '__contains__',
 '__copy__',
 '__dataframe__',
 '__dataframe_consortium_standard__',
 '__deepcopy__',
 '__delattr__',
 '__delitem__',
 '__dict__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__finalize__',
 '__firstlineno__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattr__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__iand__',
 '__ifloordiv__',
 '__imod__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__invert__',
 '__ior__',
 '__ipow__',
 '__isub__',
 '__iter__',
 '__itruediv__',
 '__ixor__',
 '__le__',
 '__len__',
 '__lt__',
 '__matmul__',
 '__mod__',
 '__module__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__nonzero__',
 '__or__',
 '__pandas_priority__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rmatmul__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__setitem__',
 '__setstate__',
 '__sizeof__',
 '__static_attributes__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__weakref__',
 '__xor__',
 '_accessors',
 '_accum_func',
 '_agg_examples_doc',
 '_agg_see_also_doc',
 '_align_for_op',
 '_align_frame',
 '_align_series',
 '_append',
 '_arith_method',
 '_arith_method_with_reindex',
 '_as_manager',
 '_attrs',
 '_box_col_values',
 '_can_fast_transpose',
 '_check_inplace_and_allows_duplicate_labels',
 '_check_is_chained_assignment_possible',
 '_check_label_or_level_ambiguity',
 '_check_setitem_copy',
 '_clear_item_cache',
 '_clip_with_one_bound',
 '_clip_with_scalar',
 '_cmp_method',
 '_combine_frame',
 '_consolidate',
 '_consolidate_inplace',
 '_construct_axes_dict',
 '_construct_result',
 '_constructor',
 '_constructor_from_mgr',
 '_constructor_sliced',
 '_constructor_sliced_from_mgr',
 '_create_data_for_split_and_tight_to_dict',
 '_data',
 '_deprecate_downcast',
 '_dir_additions',
 '_dir_deletions',
 '_dispatch_frame_op',
 '_drop_axis',
 '_drop_labels_or_levels',
 '_ensure_valid_index',
 '_find_valid_index',
 '_flags',
 '_flex_arith_method',
 '_flex_cmp_method',
 '_from_arrays',
 '_from_mgr',
 '_get_agg_axis',
 '_get_axis',
 '_get_axis_name',
 '_get_axis_number',
 '_get_axis_resolvers',
 '_get_block_manager_axis',
 '_get_bool_data',
 '_get_cleaned_column_resolvers',
 '_get_column_array',
 '_get_index_resolvers',
 '_get_item_cache',
 '_get_label_or_level_values',
 '_get_numeric_data',
 '_get_value',
 '_get_values_for_csv',
 '_getitem_bool_array',
 '_getitem_multilevel',
 '_getitem_nocopy',
 '_getitem_slice',
 '_gotitem',
 '_hidden_attrs',
 '_indexed_same',
 '_info_axis',
 '_info_axis_name',
 '_info_axis_number',
 '_info_repr',
 '_init_mgr',
 '_inplace_method',
 '_internal_names',
 '_internal_names_set',
 '_is_copy',
 '_is_homogeneous_type',
 '_is_label_or_level_reference',
 '_is_label_reference',
 '_is_level_reference',
 '_is_mixed_type',
 '_is_view',
 '_is_view_after_cow_rules',
 '_iset_item',
 '_iset_item_mgr',
 '_iset_not_inplace',
 '_item_cache',
 '_iter_column_arrays',
 '_ixs',
 '_logical_func',
 '_logical_method',
 '_maybe_align_series_as_frame',
 '_maybe_cache_changed',
 '_maybe_update_cacher',
 '_metadata',
 '_mgr',
 '_min_count_stat_function',
 '_needs_reindex_multi',
 '_pad_or_backfill',
 '_protect_consolidate',
 '_reduce',
 '_reduce_axis1',
 '_reindex_axes',
 '_reindex_multi',
 '_reindex_with_indexers',
 '_rename',
 '_replace_columnwise',
 '_repr_data_resource_',
 '_repr_fits_horizontal_',
 '_repr_fits_vertical_',
 '_repr_html_',
 '_repr_latex_',
 '_reset_cache',
 '_reset_cacher',
 '_sanitize_column',
 '_series',
 '_set_axis',
 '_set_axis_name',
 '_set_axis_nocheck',
 '_set_is_copy',
 '_set_item',
 '_set_item_frame_value',
 '_set_item_mgr',
 '_set_value',
 '_setitem_array',
 '_setitem_frame',
 '_setitem_slice',
 '_shift_with_freq',
 '_should_reindex_frame_op',
 '_slice',
 '_stat_function',
 '_stat_function_ddof',
 '_take_with_is_copy',
 '_to_dict_of_blocks',
 '_to_latex_via_styler',
 '_typ',
 '_update_inplace',
 '_validate_dtype',
 '_values',
 '_where',
 'abs',
 'add',
 'add_prefix',
 'add_suffix',
 'age',
 'agg',
 'aggregate',
 'align',
 'all',
 'any',
 'apply',
 'applymap',
 'asfreq',
 'asof',
 'assign',
 'astype',
 'at',
 'at_time',
 'attrs',
 'axes',
 'backfill',
 'between_time',
 'bfill',
 'bool',
 'boxplot',
 'clip',
 'columns',
 'combine',
 'combine_first',
 'compare',
 'convert_dtypes',
 'copy',
 'corr',
 'corrwith',
 'count',
 'cov',
 'cummax',
 'cummin',
 'cumprod',
 'cumsum',
 'describe',
 'diff',
 'div',
 'divide',
 'dot',
 'drop',
 'drop_duplicates',
 'droplevel',
 'dropna',
 'dtypes',
 'duplicated',
 'empty',
 'eq',
 'equals',
 'eval',
 'ewm',
 'expanding',
 'explode',
 'ffill',
 'fillna',
 'filter',
 'first',
 'first_valid_index',
 'flags',
 'floordiv',
 'from_dict',
 'from_records',
 'ge',
 'get',
 'groupby',
 'gt',
 'head',
 'hist',
 'iat',
 'idxmax',
 'idxmin',
 'iloc',
 'index',
 'infer_objects',
 'info',
 'insert',
 'interpolate',
 'isetitem',
 'isin',
 'isna',
 'isnull',
 'items',
 'iterrows',
 'itertuples',
 'join',
 'keys',
 'kurt',
 'kurtosis',
 'last',
 'last_valid_index',
 'le',
 'loc',
 'lt',
 'map',
 'mask',
 'max',
 'mean',
 'median',
 'melt',
 'memory_usage',
 'merge',
 'min',
 'mod',
 'mode',
 'mul',
 'multiply',
 'ndim',
 'ne',
 'nlargest',
 'notna',
 'notnull',
 'nsmallest',
 'nunique',
 'pad',
 'pct_change',
 'pipe',
 'pivot',
 'pivot_table',
 'plot',
 'pop',
 'pow',
 'price',
 'prod',
 'product',
 'quantile',
 'query',
 'radd',
 'rank',
 'rdiv',
 'reindex',
 'reindex_like',
 'rename',
 'rename_axis',
 'reorder_levels',
 'replace',
 'resample',
 'reset_index',
 'rfloordiv',
 'rmod',
 'rmul',
 'rolling',
 'round',
 'rpow',
 'rsub',
 'rtruediv',
 'sample',
 'select_dtypes',
 'sem',
 'set_axis',
 'set_flags',
 'set_index',
 'shape',
 'shift',
 'size',
 'skew',
 'sort_index',
 'sort_values',
 'squeeze',
 'stack',
 'std',
 'style',
 'sub',
 'subtract',
 'sum',
 'swapaxes',
 'swaplevel',
 'tail',
 'take',
 'to_clipboard',
 'to_csv',
 'to_dict',
 'to_excel',
 'to_feather',
 'to_gbq',
 'to_hdf',
 'to_html',
 'to_json',
 'to_latex',
 'to_markdown',
 'to_numpy',
 'to_orc',
 'to_parquet',
 'to_period',
 'to_pickle',
 'to_records',
 'to_sql',
 'to_stata',
 'to_string',
 'to_timestamp',
 'to_xarray',
 'to_xml',
 'transform',
 'transpose',
 'truediv',
 'truncate',
 'tz_convert',
 'tz_localize',
 'unstack',
 'update',
 'value',
 'value_counts',
 'values',
 'var',
 'where',
 'xs']

In [15]: df1.mean()
Out[15]: 
price     6.0
age      12.0
value    18.0
dtype: float64

In [16]: df1.mean().mean()
Out[16]: np.float64(12.0)

In [17]: type(df1.mean())
Out[17]: pandas.core.series.Series

In [18]: df1
Out[18]: 
        price  age  value
First       2    4      6
Second     10   20     30

In [19]: ERROR

In [20]: df1.price
Out[20]: 
First      2
Second    10
Name: price, dtype: int64

In [21]: type(df1.price)
Out[21]: pandas.core.series.Series

In [22]: df1.price.mean()
Out[22]: np.float64(6.0)

In [23]: df1.price.max()
Out[23]: np.int64(10)
```

## Clase 105
### Installing Jupyter
In the next videos, we will use Jupyter Notebook is a third-party library. Please install Jupyter Notebook by executing one of the commands below:
```html
# Installing Jupyter

pip3.13 install jupyter
```
Please change the number after pip to reflect the version of Python you are using.

#### Starting Jupyter

After a successful installation you can start Jupyter Notebook by running the command below from your terminal:
```html
jupyter notebook

# If the above command does not work try the following command:

py -3.13 -m jupyter notebook (for Windows users)
```
If it works, you will see Jupyter Notebook opened up in your default internet browser: **Jupyter in the cloud**
<br>

If you do not want to install Jupyter or you cannot install it, you can use Jupyter in the cloud. Google offers a ready-to-use Jupyter notebook here: https://colab.research.google.com/#create=true

## Clase 106
### Primeros Pasos Jupyter
Documentación disponible en: https://jupyter-notebook.readthedocs.io/en/stable/
<br>

Tras instalar jupyter(**pip3.13 install jupyter**) y escribir en la consola: jupyter notebook; nos lanza un par de urls de nuestro jupyter en local host en nuestro navegador predeterminado.
<br>

En dicha url nos dirijimos a Nuevo>Python3(ipkernel). Aquí podemos editar el "notebook" desde el nombre del mismo como su contenido. Los cambios y arhcivos que vayamos guardando se almacenarán donde hayamos instalado jupyter (A:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world Applications\Python\.ipynb_checkpoints).

#### Trabajando con Jupyter Notebook
En el navegador podemos emplear la consola de jupyter notebook como una consola normal, con la salvedad de que podemos escribir varias líneas de cósigo pulsando "Enter". Para correr el código, pulsaremos el botón "Run" en el panel de la consola del navegador o **Ctrl + Enter**. Ahora añadamos algo de código para probar la consola:
```html
print(1)
print(2)
# Out
1
2
```
Para crear una nueva Celda **Alt + Enter**
```html
print(3)
print(4)
# Out
3
4
```
Para crear una nueva Celda de manera directa **Shift + Enter**
<br>

Para eliminar una celda: **Esc into dd**.
<br>

Podemos diferenciar la existencia de dos modos dentro de Jupyter Notebook:
- Common Mode: rectángulo gris al rededor del código
- Edit Mode: cuando presionas Enter, seleccionas la celda, cuando presionas Esc sales de la celda y retornas al common mode para moverte entre celdas
<br>

Podemos ver más atajos para el manejo de Jupyter Notebook en **Help>Keyboard Shotcuts**
```html
Redo	Ctrl + Shift + Z
Undo	Ctrl + Z
Run Selected Cell	Shift + Enter
Find Next	Ctrl + G
Find Previous	Ctrl + Shift + G
Find…	Ctrl + F
Activate Next Tab	Ctrl + Shift + ]
Activate Next Tab Bar	Ctrl + Shift + .
Activate Previous Tab	Ctrl + Shift + [
Activate Previous Tab Bar	Ctrl + Shift + ,
Toggle Left Area	Ctrl + B
Toggle Mode	Ctrl + Shift + D
Toggle Right Area	Ctrl + J
Toggle Sidebar Widget	Alt + 1
Toggle Sidebar Widget	Alt + 2
Toggle Sidebar Widget	Alt + 3
Toggle Sidebar Widget	Alt + 4
Toggle Sidebar Widget	Alt + 5
Toggle Sidebar Widget	Alt + 6
Toggle Sidebar Widget	Alt + 7
Toggle Sidebar Widget	Alt + 8
Toggle Sidebar Widget	Alt + 9
Toggle Sidebar Widget	Alt + 0
Toggle Sidebar Widget	Alt + Shift + 1
Toggle Sidebar Widget	Alt + Shift + 2
Toggle Sidebar Widget	Alt + Shift + 3
Toggle Sidebar Widget	Alt + Shift + 4
Toggle Sidebar Widget	Alt + Shift + 5
Toggle Sidebar Widget	Alt + Shift + 6
Toggle Sidebar Widget	Alt + Shift + 7
Toggle Sidebar Widget	Alt + Shift + 8
Toggle Sidebar Widget	Alt + Shift + 9
Toggle Sidebar Widget	Alt + Shift + 0
Activate Command Palette	Ctrl + Shift + C
Show Keyboard Shortcuts…	Ctrl + Shift + H
Pause	F9
Next	F10
Debugger Panel	Ctrl + Shift + E
Step In	F11
Step Out	Shift + F11
Terminate	Shift + F9
Save Notebook	Ctrl + S
Save Notebook As…	Ctrl + Shift + S
Reopen Last	Ctrl + Shift + T
Activate Previously Used Tab	Ctrl + Shift + '
Table of Contents	Ctrl + Shift + K
```

#### Para qué Jupyter Notebook
JN es empelado especialmente para exploraciones y exploraciones de datos así como para Data Análisis y Data Visualization
```html
import pandas
df=pandas.read_csv("downloads/temps_today.csv")
df
# Output: tabla del archivo
```
También puede emplearse para **Web scrapping**

## Clase 107
### Cargando archivos CSV
- Descargamos los archivos supermarkets
- Abrimos jupyter notebook en su ubicación
- Creamos un Nuevo>Python3(ipkernel)
- Empezamos a jugar!
- Antes de cargar estos archivos de supermarkets en Python, aquí nos muestran un truco para listar los documentos y poder copiar los nombres directamente:
```html
import os
os.listdir()
# Shift + Enter
# Nos lanzará la lista de archivos
['.ipynb_checkpoints',
 'fruits.txt',
 'supermarkets-commas.txt',
 'supermarkets-semi-colons.txt',
 'supermarkets.csv',
 'supermarkets.json',
 'supermarkets.xlsx',
 'temps_today.csv',
 'Untitled.ipynb',
 'verduras.txt']

 # Continuamos:
 import pandas
 df1=pandas.read_csv('supermarkets.csv')
 df1
```
![Output Clase 107](/img/Clase107.png)

Una vez que cargamos el DataFrame podemos hacer infinidad de operaciones con él y finalmente podemos exportarlo a csv, excel, etc.

## Clase 108
### Exercise: Loading JSON Files
In  the previous lecture, you learned that you can load a CSV file with this code:
```html
import pandas
df1 = pandas.read_csv("supermarkets.csv")
------------------------------------------
# Para .Json

df2=pandas.read_json('supermarkets.json')
df2
```
Try loading the supermarkets.json file for this exercise using **read_json** instead of read_csv. The supermarkets.json file can be found inside the supermarkets.zip file attached in the previous lecture.



## Clase 11
### 
## Clase 11
### 
## Clase 11
### 
## Clase 11
### 










