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




















