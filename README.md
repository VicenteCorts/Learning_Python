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

## Clase 110
### Note on Loading Excel Files
In the next lecture, you will learn **how to load Excel files** in Python with pandas. For this, you need pandas (which you have already installed) and also two other dependencies that pandas needs for opening Excel files. You can install them with pip:
```html
pip3.13 install openpyxl (needed to load Excel .xlsx files)

pip3.13 install xlrd (needed to load Excel old .xls files)
```

## Clase 111
### Cargando Archivos Excel
```html
# Seguimos trabajando en jupyter notebook

df3=pandas.read_excel('supermarkets.xlsx')
df3
```
Si queremos trabajar sobre una de las hojas concretas del excel deberemos cambiar la syntaxis usando su índice o el nombre de la hoja concreta **sheet_name=0**:
```html
df4=pandas.read_excel('AustinJohnHOMELivingDexSV_1.3.2_2.xlsx', sheet_name=0)
df4
```

## Clase 112
###  Cargando Archivos de Texto plano
En el primer ejemplo emplearemos el archvio cuyos datos vienen separados por **,**:
```html
df4=pandas.read_csv('supermarkets-commas.txt')
df4
```
**CSV**: caracter separator values
<br>

Cuando el caracter separador son comas, no es necesario añadir parámetro indicando cuál es el separador de CSV; sin embargo, en el siguiente ejemplo, el elemento separador es "**;**" por lo que debemos añadir parámetro indicándolo:
```html
# Para ver información sobre el método read_csv, que se encuentra dentro de la librería pandas
pandas.read_csv?
---------------------
# la palabra clave para determinar el separador es (sep="")
df5=pandas.read_csv('supermarkets-semi-colons.txt', sep=";")
df5
```

## Clase 113
### Set Table Header Row
En ocasiones los datos pueden venir sin los encabezados. Para manipular la fila de los **Headers** y dejarla "vacía" emplearemos el siguiente código **header=None**:
```html
df1=pandas.read_csv('verduras.txt', header=None)
df1
```

## Clase 114
### Set Columns Names
Para asignar nombres a este encabezado vacío, lo haremos de la siguiente forma:
```html
# Dentro de la lista deben haber tantos elementos como columnas tenga la tabla
df1.columns = ["Nombre del alimento"]
df1
```

## Clase 115
### Set index Columns
El concepto de **índice** dentro de las tablas con las que estamos trabajando, nos permitirá seleccionar una **porción** de los datos para extraerlos y/o manipularlos. **Con esto lo que hacemos es establecer una de las columnas como índice de cada fila** -> haciendo que su posición de columna desaparezca.
```html
df2.set_index("ID")
```
Cuando hacemos uso del método set_index no estamos reescribiendo ni sobreescribiendo el Data Frame, sino que crea una addición temporal en la tabla para reflejar los resultados.
<br>

Si queremos mantener los cambios, podemos almacenar la operación en una nueva variable o emplear el parámetro **inplace=True** en el objeto original para que los cambios sean permanentes:
```html
dfi = df2.set_index("ID")
dfi
-----------------------------
# También se puede modificar de manera permanente el objeto inicial con:
df2.set_index("ID", inplace=True)
df2
```
En el siguiente ejemplo veremos cómo hacer para que a la hora de establecer una de las columnas como índice (mediante set_index), esta columna permanezca en su posición de columna:
```html
df2.set_index("Address", inplace=True)
df2
```

## Clase 116
### Filtrar o Seleccionar Datos de un DataFrame de pandas
Para manipular los DataFrames añadiendo y eliminando columnas o filas, primero debemos entender como están indexados los DF. A continuación veremos cómo están indexados los DF y como hacerles **"Slice"** para extraer una porción deseada de estas tablas.
<br>

Trabajaremos sobre esta tabla modificada con el índice "inplaced" de Address:
![Tabla Clase 116](/img/Clase116.png)
Existen varias formas de extraer estas porciones:

1. Label-base-indexing -> Se emplea el método **loc**:
```html
df1.loc["735 Dolores St":"332 Hill St","Country":"Employees"]
```
![Output Clase 116](/img/Clase116_2.png)
Tambien podemos acceder a celdas únicas modificando el código anterior:
```html
df1.loc["332 Hill St","Country"]
```
Si queremos una columna completa:
```html
df1.loc[:,"Country"]
# Incluso podemos pasarlo en formato lista
list(df1.loc[:,"Country"])
```

2. Position-base-indexing -> **Forma más común de trabajar**. Esta vez se emplea el método **iloc** en vez de **loc**:
```html
df1.iloc[1:4,1:4]
# El último número de los rangos no se incluye en el output, por lo que si queremos extraer las líneas de la 1 (empieza por el indice 0) hasta la 3, debemos indicar 1:4
```
![Output Clase 116](/img/Clase116_3.png)
Tambien podemos acceder a celdas únicas modificando el código anterior:
```html
df1.iloc[1,4]
```
Si queremos las columnas completas:
```html
df1.iloc[:,1:4]
```

## Clase 117
### Borrar Columnas y Filas
Para borrar haremos uso del método **drop**. Tener en cuenta que no es una operación de "inplace" por lo que podemos trabajar de forma segura sin perder o actualizar datos.

#### ELIMINAR COLUMNAS
```html
df1.drop("City", axis=1)
# El "1" puede ser 0 o 1 en función de si queremos borrar filas o columnas (respectivamente)
or
df1.drop(columns="City")
```

Para elimnar múltiples columnas debemos acceder a sus índices de la sigueinte forma:
```html
# Descubrir cuáles son los índices de las columnas: 
df1.columns

# Borrar columnas concretas:
df1.drop(['City', 'Country', 'State'], axis=1)
or
df1.drop(df1.columns[[1, 3, 5]], axis=1)

# Borrar intervalo de columnas:
df1.drop(columns=df1.columns[0:3])
or
df1.drop(df1.columns[0:3], axis=1)
```

#### ELIMINAR FILAS 
```html
df1.drop("3666 21st St", axis=0)
# El "0" puede ser 0 o 1 en función de si queremos borrar filas o columnas (respectivamente)
or
df1.drop("3666 21st St")
``` 

Para elimnar múltiples filas debemos acceder a sus índices de la sigueinte forma:
```html
# Descubrir cuáles son los índices: 
df1.index

# Borrar filas concretas:
df1.drop(['3666 21st St', '332 Hill St'])
or
df1.drop([1, 2], axis=0)

# Borrar intervalo completo de filas:
df1.drop(df1.loc["3666 21st St":"3995 23rd St"].index)
or
df1.drop(df1.iloc[1:5].index)
```

## Clase 118
### Update y Add nuevas Columnas y Filas
#### ADD COLUMNAS
A la hora de crear una nueva columna, debemos tener en cuenta el número de valores que tenemos que indroducir en esta, porque si dejamos algún valor vacío dara ERROR:
```html
# Ver total de valores necesarios para crear columna:
len(df1.index)
# 6 -> debemos completar la columna con 6 valores
```
Para crear una columna usaremos el sigueinte código:
```html
df1["Continent"] = df1.shape[0]*["Europe"]
df1

or

df1["Continent"] = ¡["Europe", "Australia", "Europe", "America, "America", "Asia"]
df1
```
Del primer modo introducimos una columna con el Header "Continent" y los 6 valores necesarios con "Europe". al usar df1.shape nos devuelve (6,8) es decir (6 filas, 8 columnas). Al hacer uso de "df1.shape[0]*["Valor"]", le estamos diciendo a la consola Jupyter Notebook que introduzca ["Valor"] tantas veces como filas haya.

#### UPDATE COLUMNAS
```html
# De forma general afectando a todas las filas de la columna:
df1["Continent"] = df1["Address"] + ", " + "Europe"
df1

or -para tipo int-

df1["Continent"] = df1["Employees"].astype(str) + ", " + "Europe"
df1

# De forma específica, cambiando solo uno de los datos
df1.at[índice, 'nombre_columna'] = nuevo_valor
df1.loc[índice, 'nombre_columna'] = nuevo_valor
df1.iloc[número_fila, número_columna] = nuevo_valor
```

#### ADD FILAS
Para añadir nuevas filas tomaremos un camino diferente, en primer lugar haremos una **conversión de la tabla (.T)**, para poner los índices en las columnas y las columnas en los índices:
```html
df1_t=df1.T
df1_t
```
![Conversión Tabla Clase 118](/img/Clase118.png)
Y posteriormente, trabajamos como si la fila a crear o modificar se tratase de una nueva columna siguiendo el apartado anterior de esta misma clase (respetando siempre el **tipo de dato, el orden y el número de valores a introducir**):
```html
df1_t["My Address"] = [7,"Mi ciudad", "Mi provincia?", "Mi país", "Mi tienda", 11, "Europa occidental"]
df1_t
```
Y finalmente deshacemos la **conversión de la tabla (.T)**:
```html
df1=df1_t.T
df1
```

#### AÑADIR FILA SEGÚN CLAUDE
Otra forma menos enrevesada según **CLAUDE** sería:
```html
df1.loc['My Address2'] = [7,"Mi ciudad", "Mi provincia?", "Mi país", "Mi tienda", 11, "Europa occidental"]
df1
```

#### UPDATE FILA
Con los elementos vistos hasta ahora, no habría problema, podemos optar por la versión de la conversión de tabla y seguir el ejemplo de la modificación de columna o directamente emplear el ejemplo de Claude y añadir los valores que nos interesen.
```html
list(df1.iloc[4])
# [5, 'San Francisco', 'California', 'USA', 'Sanchez', 12, '12, Europe']
```

## Clase 119
### Note
We are going to use **Nominatim()** in the next video. Nominatim() currently has a bug. To fix this problem, whenever you see these lines in the next video:
```html
from geopy.geocoders import Nominatim
nom = Nominatim()
```
change them to these
```html
from geopy.geocoders import ArcGIS
nom = ArcGIS()
The rest of the code remains the same.
```

## Clase 120
### Data Analysis Example: Converting Addresses to Coordinates
Vamos a convertir los datos del DataFrame en coordenadas geográficas **(GEOCODING y REVERSEGEOCODING)** para trabajar con ellos. Crearemos dos columnas nuevas para la latitud y la altitud. Pandas no puede hacer este geocoding por ello emplearemos otra librería llamada **GEOPY**. El cual instalaremos mediante:
```html
# Consola normal
pip3.13 install geopy

# Jupyter Notebook
import geopy
dir(geopy)
# Output
['ArcGIS',
 'AzureMaps',
 'BANFrance',
 'Baidu',
 'BaiduV3',
 'Bing',
 'DataBC',
 'GeoNames',
 'GeocodeEarth',
 'Geocodio',
 'Geokeo',
 'Geolake',
 'GoogleV3',
 'Here',
 'HereV7',
 'IGNFrance',
 'LiveAddress',
 'Location',
 'MapBox',
 'MapQuest',
 'MapTiler',
 'Nominatim',
 'OpenCage',
 'OpenMapQuest',
 'Pelias',
 'Photon',
 'PickPoint',
 'Point',
 'Timezone',
 'TomTom',
 'What3Words',
 'What3WordsV3',
 'Woosmap',
 'Yandex',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 '__version__',
 '__version_info__',
 'adapters',
 'compat',
 'exc',
 'format',
 'geocoders',
 'get_geocoder_for_service',
 'get_version',
 'location',
 'point',
 'timezone',
 'units',
 'util']

# Jupyter Notebook
from geopy.geocoders import ArcGIS
nom = ArcGIS()
```
Tras esta preparación inicial, comenzaremos con la geocodificación:
```html
nom.geocode("3666 21st St, San Francisco, CA 94114")
# Output con altitud y latitud:
Location(3666 21st St, San Francisco, California, 94114, (37.756632001957, -122.429411011948, 0.0))
# Puede no lanzar output en caso de que la dirección sea inventada. -> None

# Guardaremos el resultado en una variable para poder trabajar con ella:
n=nom.geocode("3666 21st St, San Francisco, CA 94114")
n.latitude
# 37.756632001957
n.longitude
# -122.429411011948
type(n)
# geopy.location.Location
```
Ahora construiremos las nuevas columnas para llevar a cabo la recopilación de datos del geocoding:
```html
# Restauramos el archivo inicial para emplear sus ubicaciones:
df1=pandas.read_csv('supermarkets.csv')
df1

# Modificamos la columna "Address" para que contenda la dirección completa y trabajar posteriormente con los datos de esta columna:
df1["Address"] = df1["Address"]+ ", "+ df1["City"]+ ", "+ df1["State"]+ ", "+ df1["Country"]
df1

# Ahora emplearemos los datos de la nueva columna para la geocodificación:
# usaremos el método de pandas: .apply():
df1["Coordinates"] = df1["Address"].apply(nom.geocode)
df1

df1.Coordinates
df1.Coordinates[0].latitude -> Lanzará la latitud

# Ahora crearemos una columna específica para la latitud:
df1["Latitude"] = df1["Coordinates"].apply(lambda x: x.latitude)
df1

# Ahora crearemos una columna específica para la longitud:
df1["Longitude"] = df1["Coordinates"].apply(lambda x: x.longitude)
df1
```
Cuidado:
```html
Puede darnos un error en caso de que alguna de las direcciones no 
sea real e intente aplicarle los métodos .latitude y/o .logitude; 
para solucionar este problma podemos modificar el código con un
condicional:

# Ahora crearemos una columna específica para la latitud:
df1["Latitude"] = df1["Coordinates"].apply(lambda x: x.latitude if x 1= None else None)
df1

# Ahora crearemos una columna específica para la longitud:
df1["Longitude"] = df1["Coordinates"].apply(lambda x: x.longitude if x 1= None else None)
df1
```

# Section 14
## Clase 121
### Qué es NumPy
Documentación: https://numpy.org/doc/
<br>

NumPy is an open source project that enables numerical computing with Python. (Ejemplo de la imagen pixelada en escala de grises y sus valores representados con listas de números)
```html
# Jupyter Notebook: array n unidireccional
import numpy
n=numpy.arange(27)
n
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
type(n)
-> numpy.ndarray

# array bidimensional:
n.reshape(3,9)
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23, 24, 25, 26]])

# array tridimencional:
n.reshape(3,3,3)
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])

# Otro ejemplo asociado a la imagen de píxeles grises
m=numpy.asarray([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])  
m
array([[1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5]])
print(m)
[[1 2 3 4 5]
 [1 2 3 4 5]
 [1 2 3 4 5]]
type(m)
-> numpy.ndarray
```

## Clase 122
### Installing OpenCV
Documentation-> https://opencv.org/
<br>

In the next lecture, and in Section 17, we will use the **OpenCV** image processing library. Let us first make sure you have installed the OpenCV library. **OpenCV is also referred to as cv2** in Python.

#### How to Install OpenCV
To install OpenCV for Python 3.13 on Windows, execute the following in the terminal:
```html
py -3.13 -m pip install opencv-python
```
Once the installation completes, open a Python session and try:
```html
import cv2 
```
If you get no errors, you installed OpenCV successfully. **If you find errors, check FAQs**: https://www.udemy.com/course/former-python-mega-course-build-10-real-world-applications/learn/lecture/34362806#overview

## Clase 123
### Convert Images to Numpy Arrays
Tras la instalación correcta de la clase anterior, comenzaremos por cargar la imagen de los píxeles grises en python:
```html
# jupyter Notebook
import cv2
im_g=cv2.imread("img/smallgray.png", 0)
im_g
# 0= leer la imagen en escala de grises
# 1= leer la imagen en rbg
array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8)

# si cambiamos el parámetro de 0 a 1 obtendremos un array tridimensional, correspondiente a R, G, B de cada color
im_g=cv2.imread("img/smallgray.png", 1)
im_g
array([[[187, 187, 187],
        [158, 158, 158],
        [104, 104, 104],
        [121, 121, 121],
        [143, 143, 143]],

       [[198, 198, 198],
        [125, 125, 125],
        [255, 255, 255],
        [255, 255, 255],
        [147, 147, 147]],

       [[209, 209, 209],
        [134, 134, 134],
        [255, 255, 255],
        [ 97,  97,  97],
        [182, 182, 182]]], dtype=uint8)
```
No solo podemos leer las imagenes, también podemos escribir en ellas:
```html
# Creamos un nuevo archivo de imagen empleando el array de la imagen que teníamos en un principio:
cv2.imwrite("img/newsmallgray.png",im_g)
-> True
```

## Clase 124
### Indexing, Slicing, and Iterating Numpy Arrays
Hacer Slice a una lista:
```html
a=[1, 2, 3]
a[:1]
a[1:2]
```
#### INDEXAR EN ARRAY NUMPY
Con los **array Numpy** funciona de la misma manera, teniendo en cuenta que pueden ser de 1, 2 o 3 dimensiones
```html
# Vamos a extraer una porción de la imagen de píxeles grises (im_g):
# Recuperamos la imagen en formato numpy array
im_g=cv2.imread("img/smallgray.png", 0)
im_g

# Seleccionamos el índice de las filas que vamos a hacer Slice, seguido del índice de las columnas:
im_g[0:2, 2:4 ]
array([[104, 121],
       [255, 255]], dtype=uint8)
im_g.shape
-> (3, 5)
```
#### ITERAR EN ARRAY NUMPY
Existen dos formas:
1. iterar el array o matriz Mediante Bucle for:
```html
for i in im_g:
    print(i)
# Output:
[187 158 104 121 143]
[198 125 255 255 147]
[209 134 255  97 182]
---------------------------
# Para iterar a través de las columnas emplearemos la trasnformación de tabla ".T"
for i in im_g.T:
    print(i)
# Output:
[187 198 209]
[158 125 134]
[104 255 255]
[121 255  97]
[143 147 182]
```
2. iterar el valor a valor Mediante Bucle for:
```html
for i in im_g.flat:
    print(i)
# Output:
187
158
104
121
143
198
125
255
255
147
209
134
255
97
182
```

## Clase 125
### Stacking and Splitting Numpy Arrays
Operaciones más específicas. **Stacking** array Numpy supone concatenarlos. Mientras que **Spliting** implica separarlos en arrays más pequeños.
#### STACKING
**Stack Horizontal**
```html
# hstack = horizontal stack
# .hstack solo admite un valor dentro, así que para concatenar debemos introducir una tupla:
# .hstack juntará los arrays de manera horizontal, quedará el mismo número de filas pero el de columnas será la suma de las columnas de ambos arrays de la tupla
ims=numpy.hstack((im_g, im_g))
ims
# Output:
array([[187, 158, 104, 121, 143, 187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147, 198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182, 209, 134, 255,  97, 182]], dtype=uint8)
```
**Stack Vertical**
```html
# vstack = vertical stack
# .vstack solo admite un valor dentro, así que para concatenar debemos introducir una tupla:
# .vstack juntará los arrays de manera vertical, quedará el mismo número de columnas pero el de filas será la suma de las filas de ambos arrays de la tupla
ims=numpy.vstack((im_g, im_g))
ims
# Output:
array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182],
       [187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8)
```
#### SPLITTING
**Split horizontal**
```html
# hsplit -> para dividir en base a columnas
lst=numpy.hsplit(ims, 5)
lst
[array([[187],
        [198],
        [209],
        [187],
        [198],
        [209]], dtype=uint8),
 array([[158],
        [125],
        [134],
        [158],
        [125],
        [134]], dtype=uint8),
 array([[104],
        [255],
        [255],
        [104],
        [255],
        [255]], dtype=uint8),
 array([[121],
        [255],
        [ 97],
        [121],
        [255],
        [ 97]], dtype=uint8),
 array([[143],
        [147],
        [182],
        [143],
        [147],
        [182]], dtype=uint8)]
```
**Split vertical**
```html
# vsplit -> para dividir en base a filas
lst=numpy.vsplit(ims, 3)
lst
[array([[187, 158, 104, 121, 143],
        [198, 125, 255, 255, 147]], dtype=uint8),
 array([[209, 134, 255,  97, 182],
        [187, 158, 104, 121, 143]], dtype=uint8),
 array([[198, 125, 255, 255, 147],
        [209, 134, 255,  97, 182]], dtype=uint8)]
```

# Section15
## Clase 126
### Welcome to the First App
Congratulations on reaching the applications part! The following videos will guide you on how to build a program that generates interactive web maps with Python. The program combines the core Python building blocks such as conditionals, for-loops, functions, and file processing with the extras of a third-party Python library used to generate beautiful web maps.
<br>

This will help you practice the Python core concepts, and you will also learn how to approach and use third-party Python libraries. Every other real-world program you will build during your Python career will also combine the Python building blocks with specialized third-party libraries, so this app introduces you into the world of making real-world programs with Python.
<br>

To make the most of the videos, try to play around with the code that you see in the videos. Try to experiment with the code, change it, add more functionalities if you can, and see how the output changes. You will succeed if you do that.

## Clase 127
### Demo Web Map
Trabajaremos con la librería **Folium**. La aplicación recogerá tres capas, una priemra de mapa, una segunda que refleje la población y una tercera que muestre los volcanes por zonas.

## Clase 128
### Creando mapa html con Python
Documentación Folium: https://python-visualization.github.io/folium/latest/
<br>

En primer lugar necesitaremos la librería **Folium**. Folium permite que python se traduzca a html javascript y css; permitiendo crear webmaps usando código de python. PAra empezar a usarlo:
```html
pip3.13 install folium
```
Nos puede pedir que instalemos ademas jinja2, un paquete anexo de folium. Pero por defecto a nosotros nos lo instala con el comando anterior. **Ahora Comprobamos que folium funciona correctamente:**
```html
py -3
>>> import folium
>>> 
# Si no nos da error todo está en orden
```
Folium trabaja con objetos **map**
```html
>>> dir(folium)
['Choropleth', 'Circle', 'CircleMarker', 'ClickForLatLng', 'ClickForMarker',
'ColorLine', 'ColorMap', 'CssLink', 'CustomIcon', 'Div', 'DivIcon',
'Element', 'FeatureGroup', 'Figure', 'FitBounds', 'FitOverlays',
'GeoJson', 'GeoJsonPopup', 'GeoJsonTooltip', 'Html', 'IFrame', 
'Icon', 'JavascriptLink', 'JsCode', 'LatLngPopup', 'LayerControl',
'LinearColormap', 'Link', 'MacroElement', 'Map', 'Marker', 'PolyLine',
'Polygon', 'Popup', 'Rectangle', 'RegularPolygonMarker', 'StepColormap',
'TileLayer', 'Tooltip', 'TopoJson', 'Vega', 'VegaLite', 'WmsTileLayer',
'__all__', '__builtins__', '__cached__', '__doc__', '__file__',
'__loader__', '__name__', '__package__', '__path__', '__spec__',
'__version__', '_version', 'branca', 'elements', 'features', 'folium',
'map', 'raster_layers', 'utilities', 'vector_layers']
>>> help(folium.map)
(...................)
```
Ahora **crearemos un obejto map**. Para ello necesitamos la latitud y longitud del punto donde queremos que inicie el mapa:
- latitud: va de -90 a 90
- longitud: -180 a 180
```html
>>> map = folium.Map(location=[40.42402, -3.711145])
>>> map
<folium.folium.Map object at 0x000001F55AC3B4D0>
```
Posteriormente con el siguiente código creamos un archivo html para utilizar, el cual iniciará en el punto de coordenadas establecido:
```html
# Sevilla:
>>> map = folium.Map(location=[37.38283, -5.97317])
>>> map.save("Map1.html")
----------------------------------
# Podemos añadir diferentes parámetros e ir jungando
# Zoom:
>>> map = folium.Map(location=[37.38283, -5.97317], zoom_start=15)
>>> map.save("Map1.html")
```

## Clase 129
###Note
In the next lecture, I use this in the code:
```html
tiles = "Mapbox Bright"
tiles = "Stamen Terrain"
# Please use this instead:

tiles = "OpenTopoMap"
```
Mapbox Bright and Stamen Terrain are both types of base maps, but **Mapbox Bright doesn't work anymore**. Stamen Terrain works great, and you will see it creates a beautiful terrain map.

## Clase 130
### Map Marker
Investigando más entre los parámetros de **folium.map**, encontramos **tiles** para modificar el fondo del mapa o el tipo (político, topográfico, etc):
```html
import folium
# Sevilla:
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")
map.save("Map1.html")
```
#### Otros ejemplos de tiles:
```html
# Stamen parece que ya no da soporte y no funciona
# Stamen Terrain
map = folium.Map(location=[37.38283, -5.97317], tiles="Stamen Terrain", attr="Stamen")

# Stamen Watercolor
map = folium.Map(location=[37.38283, -5.97317], tiles="Stamen Watercolor", attr="Stamen")

# OpenStreetMap
map = folium.Map(location=[37.38283, -5.97317], tiles="OpenStreetMap")

# Otros estilos
map = folium.Map(location=[37.38283, -5.97317], tiles="CartoDB positron", attr="CartoDB")
```
#### Incluir puntos o marcadores en el mapa
```html
dir(folium)
(...)
# En esta ocsaión ejecutamos el archivo .py directamente:
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

map.add_child(folium.Marker(location=[37.38, -5.97], popup="Ey soy un Marker", icon=folium.Icon(color='green')))

map.save("Map1.html")
```
Una forma mejor de hacerlo es añadiendo un **FeatureGroup** (fg) para facilitar el trabajo posterior:
```html
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[37.38, -5.97], popup="Markador 1", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
```

## Clase 131
### Bucle For para añadir múltiples marcadores
La opción más rústica sería añadir el código **fg.add_child tantas veces como deseemos** y modificar la **location** para establecer los diferentes marcadores:
```html
# Sevilla:
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[37.38, -5.97], popup="Markador 1", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[37.387, -5.977], popup="Markador 2", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[37.385, -5.975], popup="Markador 3", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("Map1.html")
```
Pero la forma óptima de hacerlo sería mediante un **bucle for**:
```html
# Sevilla:
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

fg = folium.FeatureGroup(name="My Map")

i = 1
for coordinates in [[37.38, -5.97],[37.387, -5.977],[37.385, -5.975]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Markador {}".format(i), icon=folium.Icon(color='green')))
    i = i+1

map.add_child(fg)

map.save("Map1.html")
```
Sin embargo, en este código anterior, introducimos manualmente las localizaciones, pero en situaciones reales, estas **locations** nos vendrán dadas en un excel, csv, json, etc. En la siguiente clase completaremos el código mediante el acceso y manipulación de archivos.

## Clase 132
### Procesamiento de archivos + Marcadores
Ahora completaremos el código mediante el acceso y manipulación de archivos para crear marcadores a través de bucle for:
- Primero accederemos al archivo para ver si podemos leer la información contenida
```html
>>>import pandas
>>>data = pandas.read_csv("downloads/Calles_Sevilla.csv")
>>>data
# Todo OK
```
- Luego, crearemos dos listas mediante pandas; una para la latitud y otra para la longitud. Y posteriormente iterar ambas listas medianto bucles for:
```html
>>> data.columns
Index(['NOMBRE', 'NUMERO', 'LOCALIZACION', 'YEAR-CREATION', 'LAT', 'LON'], dtype='object')

# LATITUDES
>>> lat = list(data["LAT"])
>>> lat
[37.3886, 37.3839, 37.3984, 37.3823, 37.3827, 37.3869, 37.3903, 37.3846, 37.3912, 
37.3936, 37.3893, 37.3723, 37.3925, 37.3932, 37.396, 37.3831, 37.3829, 37.3806, 37.3803, 37.3809, 37.3797, 37.3811, 37.3872, 37.4031, 37.4009, 37.4012, 37.4004, 37.4017, 37.4058, 37.4043, 37.4049, 37.4046, 37.4005, 37.3779, 37.3807, 37.38, 37.3824, 37.3862, 37.3877, 37.3897, 37.3908, 37.3923, 37.3895, 37.3864, 37.386, 37.3856, 37.389, 37.3791, 37.3748, 37.3759, 37.3721, 37.373, 37.3745, 37.3753, 37.3756, 37.3751, 37.3757, 37.3762, 37.3764, 37.376, 37.3758, 37.3767, 37.3769, 37.3772, 37.3774, 37.3777, 37.378, 37.3782, 37.3785, 37.3787, 37.3789, 37.3792, 37.3794, 37.3797, 37.3799, 37.3802, 37.3804, 37.3807, 37.3809, 37.3812]

# LONGITUDES
>>> lon = list(data["LON"])
>>> lon
[-5.9953, -6.0007, -5.9927, -6.0034, -6.0045, -5.9936, -5.9948, -5.9924, -5.9933, 
-5.9901, -5.9952, -6.0012, -5.9964, -5.9908, -5.9852, -6.0049, -6.0058, -5.9902, -5.9774, -5.9756, -5.9745, -5.9725, -5.9752, -5.9843, -5.9867, -5.9904, -5.9929, -5.9911, -5.9871, -5.985, -5.9921, -5.9903, -5.9932, -6.0056, -6.005, -6.0065, -6.0021, -6.0004, -6.0008, -5.9961, -5.998, -5.9973, -5.9951, -5.9921, -5.9895, -5.9886, -5.994, -6.0072, -5.9976, -5.9971, -6.0005, -5.9986, -5.998, -5.9987, -5.9979, -5.9981, -5.9973, -5.9966, -5.9979, -5.9984, -5.9982, -5.9962, -5.9959, -5.9954, -5.995, -5.9946, -5.9941, -5.9936, -5.9932, -5.9928, -5.9924, -5.992, -5.9915, -5.9911, -5.9906, -5.9902, -5.9898, -5.9894, -5.989, -5.9885]
>>> 
```
El resultado en código sería:
```html
# Librerías Importadas
import pandas
import folium

# Acceder al archivo y extraer las LAT y LON
data = pandas.read_csv("downloads/Calles_Sevilla.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
nom = list(data["NOMBRE"])

# Crear mapa
map = folium.Map(location=[37.38283, -5.97317], zoom_start=15, tiles="OpenTopoMap")

# Crear Marcadores FeatureGroup
fg = folium.FeatureGroup(name="My Map")

# Bucle para recorrer las listas de LAT y LON (itera dos listas de manera simultánea)
for lt, ln, n in zip(lat, lon, nom):
    fg.add_child(folium.Marker(location=[lt, ln], popup=n, icon=folium.Icon(color='green')))

# Afianzar Marcadores
map.add_child(fg)

# Crear archivo de mapa web
map.save("Map1.html")
```

#### Bucle For para varias listas:
Atención a la forma de declarar un bucle for para iterar por dos listas:
```html
>>> for i,j in zip([1,2,3],[4,5,6]):
...     print(i, "and", j)
... 
1 and 4
2 and 5
3 and 6
>>> 
```

## Clase 133
### Practicing String Manipulation by Adding Text on the Map Popup Window.
En el ejemplo de la clase anterior
```html
for lt, ln, n in zip(lat, lon, nom):
    fg.add_child(folium.Marker(location=[lt, ln], popup=n, icon=folium.Icon(color='green')))
```
Nosotros no presentamos problemas con "popup=n", porque se trata de un string. Pero si quisiéramos meter en el marcador un valor que sea int o float deberemos hacer conversiones.
```html
# Si "n" fuera int o float:
for lt, ln, n in zip(lat, lon, nom):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(n), icon=folium.Icon(color='green')))

# Nota: puede ser que se lance una webmap negra si el string contiene comillas ('). Para evitar eso, cambiar el popup a:
popup=folium.Popup(str(n), parse_html=True)

# Aunque para strings simples como puede ser un número suelto no debería dar problemas mayores.
```
Podemos dar estilos o modificar el popup añadiendo más información:
```html
for lt, ln, n in zip(lat, lon, nom):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Calle "+ n, icon=folium.Icon(color='green')))
```

## Clase 134
### Adding HTML on Popups
Note that if you want to have stylized text (bold, different fonts, etc) in the popup window you can use HTML. Here's an example:
```html
import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
 
html = """<h4>Volcano information:</h4>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
 
map.add_child(fg)
map.save("Map_html_popup_simple.html")
```
You can even put links in the popup window. For example, the code below will produce a popup window with the name of the volcano as a link which does a Google search for that particular volcano when clicked:
```html
import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
map.add_child(fg)
map.save("Map_html_popup_advanced.html")
```

## Clase 135
### Practicing Functions by Creating a Color Generation Function for Markers
Añadiremos una función para detemrinar el color del marcador en función de la información de la coordenada que obtenemos:
```html
# Calase 135 Función para determinar el color en función de si es calle avda u otro
def determinar_color(calle):
    calle = calle.lower()
    color_variador = {
        'calle': 'blue',
        'avenida': 'red', 
        'plaza': 'green',
        'paseo': 'purple',
        'camino': 'orange',
        'boulevard': 'pink'
    }
    for tipo, color in color_variador.items():
        if tipo in calle:
            return color
    return 'gray'

# Y modificamos el FeatureGroup del bucle for para incluir el color en el icono:
fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=determinar_color(n))))
```

## Clase 136
### Exercise: Add and Stylize Markers Coding Exercise
Replace the icon markers we added in the previous lectures with circle markers shown in the screenshot below. There's a tip in the next lecture.

## Clase 137
### Tip on Adding and Stylizing Markers. Exercise Tip
You can use **dir(folium)**  to look for possible methods of creating circle markers. Among the methods you will see Marker, which we previously used. 
<br>

Once you locate the method, consider using **the help  function** to look for possible arguments you can pass to the method for styling the circle markers.

## Clase 138
### Solution: Add and Stylize Markers
```html
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), fill_color = determinar_color(n), color = 'grey', fill_opacity=1))

# Si da error y no se rellena el cículo de color emplearmeos como parámetro adicional:
fill=True 
```
## Clase 139
### Exploring the Population JSON Data
Ahora en el curso se establece una capa adicional al mapa en la que se representa mediante polígonos la población de estados unidos. Nosotros modificaremos esto levemente para representar mediante polígonos el año de construcción de las calles, veamos si es posible.
<br>

Para crear una capa con polígonos emplearemos el objeto **Folium.GeoJson**. En el curso trabajan con el archivo world.json, a través de ChatGPT crearemos sevilla_zonas.json (importante añadir la geometría y la población)

## Clase 140
### Practicing JSON Data by Adding a Population Map Layer from the Data
Tras la creación del archivo que vamos a emplear y una primera toma de contacto, vamos a añadir dicho archivo a neustro código para elaborar la capa de población para nuestro mapa:
```html
fg.add_child(folium.GeoJson(data=(open("downloads/sevilla_zonas_with_pop.json", 'r', encoding='utf-8').read())))
# Los polígonos son mejorables pero al menos los marca en el mapa.
```
Podemos añadir puntos o líneas a través del GeoJson, todo en base a su contenido. En la siguiente clase haremos que estos cambien de color en función de su población.

## Clase 141
### Stylizing the Population Layer
Ahora probaremos algunos métodos y funciones para editar el estilo de la capa de polígonos:
- Para añadir estilos empeleamos el parámetro style_function
- Este requere de una función lambda (funciones de una sola línea)
```html
fg.add_child(folium.GeoJson(data=open("downloads/sevilla_zonas_with_pop.json", 'r', encoding='utf-8').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP']< 50000 
    else 'yellow' if 50000 <= x['properties']['POP']< 100000 else 'red' }))
```

## Clase 142
### Adding a Layer Control Panel
Actualmente el mapa tiene una capa de mapa, una de marcadores y otra de polígonos. Ahora añadiremos una última capa de panel de control para poder esconder las capas de marcadores y polígonos a voluntad.
```html
# Al final del código pero antes del map.save()
map.add_child(folium.LayerControl())
```
Con este código podemos desactivar la capa Mymap, que actualmente lo contiene todo (marcadores y polígonos; el mapa no se puede ocultar). Separemos ahora ambas capas para poder tener un control más preciso.
- Para ello separamos los Feature Groups añadiéndoles una letra más (**fgm** para marcadore sy **fgp** para polígonos).
- Creamos los map.add_child() correspondientes
- Y modificamos las variables necesarias dentro del código:
```html
# Crear Marcadores FeatureGroup
fgm = folium.FeatureGroup(name="My Map Marcadores")

# Bucle para recorrer las listas de LAT y LON (itera dos listas de manera simultánea)
for lt, ln, n in zip(lat, lon, nom):
    iframe = folium.IFrame(html=html % str(n), width=200, height=100)
    fgm.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), fill_color = determinar_color(n), color = 'grey', fill_opacity=1))

# Crear Polígonos FeatureGroup
fgp = folium.FeatureGroup(name="My Map Polígonos")

# Clase 139 - Añadir polígonos al mapa (Folium.GeoJson)
fgp.add_child(folium.GeoJson(data=open("downloads/sevilla_zonas_with_pop.json", 'r', encoding='utf-8').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP']< 50000 
    else 'yellow' if 50000 <= x['properties']['POP']< 100000 else 'red' }))

# Afianzar Marcadores
map.add_child(fgm)

# Afianzar Polígonos
map.add_child(fgp)

# Clase 142 - Capa de control
map.add_child(folium.LayerControl())

# Crear archivo de mapa web
map.save("Map1.html")
```

# Section16
## Clase 144
### Fixing Programming Errors - Syntax Errors
Cuando tenemos errores podemos encontrar:
- Syntax Errors
- Eceptions
<br>

Tenemos este código con errores:
```html
# Clase 143
print(1)
int(9)
int 9
print(2)
print 3
```
Al correr este código, se detendrá en el primer error que encontremos:
```html
File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world 
Applications\Python\section16.py", line 4
    int 9
        ^
SyntaxError: invalid syntax
```
Si lo corregimos y corremos el código este se detendrá en la sigueinte línea con errores.
```html
int(99)
  File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world 
Applications\Python\section16.py", line 6
    print 3
    ^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```
Ahora tenemos un error con mayor descripción donde nos recomienda correcciones. Esto dependerá del propio error. Lo corregimos; y en caso de no tener más errores el código se ejecutará por completo.

## Clase 145
### Runtime Errors
Todo error que no sea un **Syntax Error** se denomina **Exception**. Este será nuestro código erróneo:
```html
a = 1
b = "2"
print(int(2.5)
print ( a + b )
```
Al ejecutarlo:
```html
Applications\Python\section16.py", line 13
    print(int(2.5)
         ^
SyntaxError: '(' was never closed
```
El programa priemro busca los **syntax errors**, y una vez están corregidos, busca **Exceptions**. Al corregir ese paréntesis anterior y ejecutar el código nos lanzará el sigueinte error:
```html
  File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world 
Applications\Python\section16.py", line 14, in <module>
    print( a + b )
           ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Corrección:
a = 1
b = "2"
print(int(2.5))
print( a + float(b))
```

## Clase 146
### How to Fix Difficult Errors
```html
# Código:
a = 1
b = "2"
c = 3
print(int(2.5))
print( c/0)

# Error:
  File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world Applications\Python\section16.py", line 24, in <module>
    print( c/0)
           ~^~
ZeroDivisionError: division by zero
```
Hay Errores que vienen definidos por su propio nombre como es este caso de **ZeroDivisionError**. Si no sabemos la causa de ese error, la mejor solución es buscar el propio error en Google e investigar. -> Stackoverflow

## Clase 147
### How to ask good questions (StackOverFlow)
(...)

## Clase 148
### Making the Code Handle Errors by Itself
```html
# Código
def divide(a,b):
    return a/b
print(divide(1,0))

# Error:
  File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world Applications\Python\section16.py", line 30, in <module>
    print(divide(1,0))
          ~~~~~~^^^^^
  File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world Applications\Python\section16.py", line 29, in divide
    return a/b
           ~^~
ZeroDivisionError: division by zero
```
Ahora haremos uso de **try: except:**:
```html
def divide(a,b):
    try:
        return a/b
    except:
        return "Zero division can't be done"

print(divide(1,0))
```

# Section17
## Clase 150
### Instalando la Librería OpenCV
**OpenCV** (Computer Vision).-> https://opencv.org/
<br>

If you haven't installed OpenCV yet, please do so by following the instructions below.  If you don't know if you have OpenCV, please open Python and type import cv2. If you don't get an error, it means OpenCV is installed.
<br>

To install:
1. Open the command line and type:
```html
pip install opencv-python 
```
2. Then open a Python session and try:
```html
import cv2 
```
3. If you get no errors, that means you installed OpenCV successfully. If you get an error, please see the FAQs below:

FAQs -> https://www.udemy.com/course/former-python-mega-course-build-10-real-world-applications/learn/lecture/34362862#announcements

## Clase 151
### Loading, Displaying, Resizing, and Creating Images
Ahora manipularemos la imagen "galaxy.jpg".
- primero debemos importar la librería
- luego crearemos la imagen con el método cv2.imread()
- dentro de este método tenemos que especificar como parámetro, cómo queremos leer la imagen: 1 para leerla con colores, 0 para escala de grises, -1 colores con trasparencias.

#### Cargar la imagen
```html
import cv2

# Cargar la imagen
img = cv2.imread("img/galaxy.jpg", 0)

print(type(img))-> tipo de dato de la variable
print(img)-> array de escala de grises
print(img.shape)-> para ver la coneitdad de píxeles
print(img.ndim) -> para ver las dimensiones del array

# Output:
<class 'numpy.ndarray'>
[[14 18 14 ... 20 15 16]
 [12 16 12 ... 20 15 17]
 [12 13 16 ... 14 24 21]
 ...
 [ 0  0  0 ...  5  8 14]
 [ 0  0  0 ...  2  3  9]
 [ 1  1  1 ...  1  1  3]]
 (1485, 990)
 2
```
Si por el contrario probamos a cargar la imagen en color, los outputs varíarían:
```html
# Cargar la imagen con color
img = cv2.imread("img/galaxy.jpg", 1)

# Output
<class 'numpy.ndarray'>
[[[19 15 10]
  [23 19 14]
  [21 15  8]
  ...
  [27 22 13]
  [22 17  8]
  [23 18  9]]

 [[17 13  8]
  [21 17 12]
  [19 13  6]
  ...
  [27 22 13]
  [22 17  8]
  [24 19 10]]

 [[17 14  6]
  [18 15  7]
  [21 18 10]
  ...
  [23 16  7]
  [33 26 17]
  [30 23 14]]

 ...

 [[ 0  0  0]
  [ 0  0  0]
  [ 0  0  0]
  ...
  [ 5  5  5]
  [ 8  8  8]
  [14 14 14]]

 [[ 0  0  0]
  [ 0  0  0]
  [ 0  0  0]
  ...
  [ 2  2  2]
  [ 3  3  3]
  [ 9  9  9]]

 [[ 1  1  1]
  [ 1  1  1]
  [ 1  1  1]
  ...
  [ 1  1  1]
  [ 1  1  1]
  [ 3  3  3]]]
(1485, 990, 3)
3
```
#### Mostrar la imagen:
```html
cv2.imshow("Galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# INFO
0: cerrar ventana con cualquier tecla
2000: la ventana se cerrará en 2 segundos
cv2.destroyAllWindows(): Para cerrar todas las ventanas
```

#### Resize Image
```html
resized_image=cv2.resize(img, (1000, 500))
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
La imagen se ve muy achatada debido a los valores que hemos introducido, podemos modificarlos para dejarla a nuestro gusto:
```html
resized_image=cv2.resize(img, (500, 1000))
``` 
O podemos mantener el ratio de la imagen de la sigueinte fomra:
```html
resized_image=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
```

#### Escribir imagen
En este caso, no la modificamos pero la guardamos. tomaremos la imagen resized y la guardaremos como nueva imagen con **cv2.imwrite("img/Galaxy_resized.jpg", resized_image)**:
```html
resized_image=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("img/Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Clase 152
### Exercise: Batch Image Resizing
Write a script that resizes all images in a directory to 100x100. You can find an attached ZIP file with some image files in the Resources.

## Clase 153
### Solution: Batch Image Resizing
```html
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
```
I first created a list containing the image file paths and then iterated through the aforementioned list.
<br>

The loop: reads each image, resizes, displays the image, waits for the user input key, closes the window once the key is pressed, and writes the resized image. The name of the resized image will be "resized" plus the existing file name of the original image.

## Clase 154
### Solution Further Explained
Para realizar el ejercicio anterior emplearemos la librería **glob** ->https://docs.python.org/3/library/glob.html
<br>

Glob encuentra el path de los archivos indicándole parte del path, en este caso, todos los que temrinen en jpg:
```html
images=glob.glob("*.jpg")
```

Para mi caso, que quiero guardarlas en una carpeta específica, tendré que importar os y añadir variables para las carpetas:
```html
# Ejercicio de resize de imagenes Clase 152-153
import cv2
import glob
import os

folder = "img/152/"
images=glob.glob(folder + "*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(400)
    cv2.destroyAllWindows()
->  filename = os.path.basename(image)
->  output_path = os.path.join(folder, "resized_" + filename)
    cv2.imwrite(output_path,re)
```

## Clase 155
### Detecting Faces in Images
Haarcascades: https://github.com/opencv/opencv/tree/master/data/haarcascades
<br>

Sirve para buscar modelos, en concreto estaremos trabajando con haarcascade de **frontal_face**. Para ello nos apoyaremos en la librería anterior opencv.
```html
# Importamos la librería
import cv2
# Creamos el objeto haarcascade
face_cascade=cv2.CascadeClassifier("img/haarcascade_frontalface_default.xml")
# Cargar imagen con cara frontal -> FUNCIONA MEJOR CON IMÁGENES EN ESCALA DE GRISES
img=cv2.imread("img/photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convierte la imagen a escala de grises
```
Ahora aplicaremos el método de búsqueda de caras:
```html
# Método para aplicar haarcascade-> los números pueden variar en funcióin de la búsqueda que queramos hacer
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

print(type(faces))
print(faces)
# Nos devolverá el array de dónde se sitúa la cara (detecta la cara en forma de rectángulo):
<class 'numpy.ndarray'>
[[157  84 379 379]]
```
Ahora mostraremos un rectángulo en la imagen apuntando al array que nos ha devuelto la búsqueda de caras:
```html
# Dibujando la salida del método anterior en forma de rectángulo
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
# img=cv2.rectangle(img, (punto de incio), (punto de inicio+valores de alto y ancho), (color en rgb), grosor del rectángulo)
```
Por último en el método cv2.imshow() incluimos la imagen original para aplicar el rectángulo. código completo:
```html
# Importamos la librería
import cv2

# Creamos el objeto haarcascade
face_cascade=cv2.CascadeClassifier("img/haarcascade_frontalface_default.xml")

# Cargar imagen con cara frontal
img=cv2.imread("img/photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convierte la imagen a escala de grises

# Método para aplicar haarcascade
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

# Dibujando la salida del método anterior en forma de rectángulo
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

# Datos para revisar
print(type(faces))
print(faces)

# Resizing
re=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

# Mostrar Imagen editada
cv2.imshow("Cara", re)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Clase 156
### Capturing Video with Python
En esta clase aprenderemos a capturar video mediante Opencv. 
```html
# Importamos Librerías
import cv2, time

# Crear objeto video - el número indica qué cámara actuará- al tener solo una, marcamos el primer índice: 0
video=cv2.VideoCapture(0)
```
Comprobaremos que está funcionando la webcam:
```html
# Revisión de los frames que captura la webcam
check, frame = video.read()
print(check)
print(frame)

# Ralentizar la ejecución del script para comprobar si la webcam se activa
time.sleep(3)

# Liberar/Parar la webcam
video.release() 
------------------------------
# Output:
True
[[[100  82  41]
  [100  82  41]
  [ 98  81  41]
  ...
  [ 51  49  28]
  [ 51  49  29]
  [ 52  49  29]]
 ...
 [[ 53  48  23]
  [ 52  47  22]
  [ 50  45  20]
  ...
  [ 18  18   2]
  [ 22  23   7]
  [ 18  19   3]]]
```
En el siguiente test, haremos que python lance el primer frame que captura la cámara en este proceso:
```html
# Mostrar Captura de Video
cv2.imshow("Capturing", frame)

# Liberar/Parar la webcam y las ventanas de testing de captura
cv2.waitKey(0)
video.release() 
cv2.destroyAllWindows
```
Otra de las pruebas que haremos será pasar el frame a escala de grises y cambiaremos la muestra de la captura de video a escala de grises:
```html
# Revisión de los frames que captura la webcam
check, frame = video.read()
print(check)
print(frame) # Por defecto es el primer frame que la cámara captura

-> # Imagen en gris (tests)
gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Ralentizar la ejecución del script para comprobar si la webcam se activa
time.sleep(3)

# Mostrar Captura de Video
-> cv2.imshow("Capturing", gray)
```

#### Trabajando con Vídeo, no frames
Para ello, haremos uso de un buble while, para ir viendo todos los frames de la webcam hasta que indiquemos que se detenga.
- eliminaremos el time.sleep()
- Cambiaremos el cv2.waitKey y pondremos un condicional para forzar la salida del bucle
- Cambiaremos la cv2.waitKey() a 1000
<br>
Código completo:
```html
# Importamos Librerías
import cv2, time

# Crear objeto video - el número indica qué cámara actuará- al tener solo una, marcamos el primer índice: 0
video=cv2.VideoCapture(0)

# Bucle While para pasar de formato imagen (frame) a video (bucle de frames)
while True:
    # Revisión de los frames que captura la webcam
    check, frame = video.read()
    # print(check)
    # print(frame) # Por defecto es el primer frame que la cámara captura

    # Imagen en gris (tests)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ralentizar la ejecución del script para comprobar si la webcam se activa
    # time.sleep(3)

    # Mostrar Captura de Video
    cv2.imshow("Capturing", gray)

    # Liberar/Parar la webcam y las ventanas de testing de captura
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release() 
cv2.destroyAllWindows
print("Webcam Off")
```
Por último, podemos saber cuantos frames se están generando de la sigueinte manera, por si es de utilidad en un futuro:
```html
# Variable para contar frames (por curiosear)
a=1

# Bucle While para pasar de formato imagen (frame) a video (bucle de frames)
while True:
    # Contando frames
    a = a + 1
    (...)
    (...)

(...)
print("Total de frames: {}".format(a))
```

# Section18
## Clase 158
### Detecting Moving Objects from the Webcam
Trabajaremos con las librerias **Opencv y Time**
<br>

Ahora elaboraremos una aplicación para detectar movimiento a través de la webcam y registrar dichos movimientos en formato CSV.
<br>

Comenzaremos a trabajar con el código de la clase anterior pero en formato optimizado:
```html
import cv2, time

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Capturing", gray)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release() 
cv2.destroyAllWindows
print("Webcam Off")
```
Ahora el proceso consisitirá en tomas una primera captura del entorno que vigilará nuestra webcam sin elementos móviles. Posteriormente Python comparará ese frame con los que vayan pasadno por cámara. estos nuevos frames se pasarán a escala de grises y posteriormente se crearán siluetas en blanco y negro para destacarlas aun más. Si estas siluetas superan un área de píxeles determinada, el programa las reconocerá como elementos nuevos y analizará su movimeinto. Elaboraremos un cuadro de color en la cámara para señalar cuáles son los objetos en movimiento.
```html
# Los apartados con titulación comentada verde son los que se añaden para el nuevo proyecto:

import cv2, time

# Frame inicial para comparación
frame0=None

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Conversión a blureado del frame (hay que pasarle por parámetro: imagen, nivel de blur, desviación estándar -0-)
    gray=cv2.GaussianBlur(gray,(21,21),0)


    # Condicional para comprobar si existe el frame inicial de comparación. En la segunda iteración del bucle "frame0" ya tiene valor entonces no entra en este condicional
    if frame0 is None:
        # El frame inicial será la variable "gray" que toma el primer frame de la cámara y lo convierte en escala de grises
        frame0 = gray 
        continue

    # Calcular diferencia entre el frame0 y el frame actual
    delta_frame=cv2.absdiff(frame0, gray)

    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame)


    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release() 
cv2.destroyAllWindows
print("Webcam Off")
```
Hasta aquí tenemos dos salidas de video una en gris y otra en delta frame, que sería la comparación del primer frame con los frames que se vayan capturando cada milisegundo.
<br>

Ahora añadiremos la capa de **Threshold** para crear una imagen en blanco y negro, dando lugar asiluetas que resultan de calcular la diferencia entre en frame0 y el frame "gris", haciendo que si hay una diferencia entre sus valores de 30 estos píxeles cambien a **blanco**:
```html
# Calcular la diferencia entre los valores del frame gray y el delta frame. Si estos valores superan el 30 haremos que python los determine como movimiento:
thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Gray frame", gray)
cv2.imshow("Delta frame", delta_frame) # para mostrar el video en deltaframe
cv2.imshow("Threshhold frame", thresh_frame) # para mostrar el video en threshold, blanco y negro por siluetas
```
Ahora createmos dilated frames: que es hacer que el thresh_frame sea más smooth:
```html
# Calcular la diferencia entre los valores del frame gray y el delta frame. Si estos valores superan el 30 haremos que python los determine como movimiento:
thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

# hacer que el thresh_frame sea más "Smooth"
thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
```
Lo siguiente será encontrar el contorno de este dilated treshold frame y dibujar los rectángulos en los objetos detectados. Podemos emplear **"findcontours" o drawcontours"**:
```html
# Creación de contornos para los objetos detectados en el dilated threshold frame
(cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tomar contornos que tengan un ára superior a 1000 pixels
for contour in cnts:
    if cv2.contourArea(contour) < 1000:
        continue

# Cuando el área sea mayor a 1000 pixels crearemos el rectángulo
(x, y, w, h) =cv2.boundingRect(contour)
# Dibujando el rectángulo creado en el frame
cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

cv2.imshow("Gray frame", gray)
cv2.imshow("Delta frame", delta_frame) # para mostrar el video en deltaframe
cv2.imshow("Threshhold frame", thresh_frame) # para mostrar el video en threshold, blanco y negro por siluetas
cv2.imshow("Color", frame) # para ver la imagen en color y con el rectángulo de detección de movimiento
```
Código completo:
```html
# Clase 158-159
# Los apartados con titulación comentada verde son los que se añaden para el nuevo proyecto:

import cv2, time

# Frame inicial para comparación
frame0=None

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Conversión a blureado del frame (hay que pasarle por parámetro: imagen, nivel de blur, desviación estándar -0-)
    gray=cv2.GaussianBlur(gray,(21,21),0)


    # Condicional para comprobar si existe el frame inicial de comparación. En la segunda iteración del bucle "frame0" ya tiene valor entonces no entra en este condicional
    if frame0 is None:
        # El frame inicial será la variable "gray" que toma el primer frame de la cámara y lo convierte en escala de grises
        frame0 = gray 
        continue

    # Calcular diferencia entre el frame0 y el frame actual
    delta_frame=cv2.absdiff(frame0, gray)

    # Calcular la diferencia entre los valores del frame gray y el delta frame. Si estos valores superan el 30 haremos que python los determine como movimiento:
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # hacer que el thresh_frame sea más "Smooth"
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    # Creación de contornos para los objetos detectados en el dilated threshold frame
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Tomar contornos que tengan un ára superior a 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        # Cuando el área sea mayor a 1000 pixels crearemos el rectángulo
        (x, y, w, h) =cv2.boundingRect(contour)
        # Dibujando el rectángulo creado en el frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame) # para mostrar el video en deltaframe
    cv2.imshow("Threshhold frame", thresh_frame) # para mostrar el video en threshold, blanco y negro por siluetas
    cv2.imshow("Color", frame) # para ver la imagen en color y con el rectángulo de detección de movimiento

    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release() 
cv2.destroyAllWindows
print("Webcam Off")
```

## Clase 159
### Storing Object Detection Timestamps in a CSV File
En este apartado crearemos una tabla csv para guardar el tiempo que el programa detecta que los diferentes objetos han estado en movimiento durante la grabación. Para ello, analizaremos el momento de entrada y salida de cada objeto en cámara.
```html
# Añadimos una nueva variable status:
    # Variable para analizar el movimiento
    status=0

# dentro del for loop de la creación de contornos añadimos
    # Tomar contornos que tengan un ára superior a 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        # Si el programa detecta algo con una variación cuya area sea mayor a 1000 pixeles cambiamos la variable status:
        status=1
        (...)

# mostramos la variavle status al final de bucle while
    # Imprimimos la variable status
    print(status)
```

Una vez que la consola imprime 1 y 0 en función de si detecta o no objetos, queremos que cuando la variable status cambie de valor y guardar el tiempo en el que lo hace.
```html
# variable al inicio del programa para recoger los cambios de la variable status
# Variable de lista vacía para rellenar con el valor de "status"
status_list=[]

# Rellenamos status_list con el método append() justo al finalizar el bucle for
    # Rellenando la variable status_list con los valores de la variable status
    status_list.append(status)

# imprimimos el status_list fuera del bucle while:
# Imprimimos la variable status_list
print(status_list)
```
Lo siguiente es conseguir el tiempo que los cambios de la variable status se han llevado a cabo
```html
# Importamos datetime
# importamos datetime
from datetime import datetime 

# Creamos una variable para guardar los tiempos al inicio del programa
# Variable para guardar tiempos de cambios de status
times=[]

# Creamos un condicional despues del status_list.append() para anexar tiempos a la variable times:
    # Condicional para anexar tiempos a la lista times cuando un objeto es detectado
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())

    # Condicional para anexar tiempos a la lista times cuando un objeto deja de ser detectado
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

# Imprimimos el resultado de la liasta times al final
# Imprimimos la variable status_list al finalizar
print(status_list)
# Imprimimos la variable times al finalizar
print(times)
```
Llegados a este punto, dará error en el punto que python, al llegar a la variable times, intenta leer dos objetos dentro de la variable status_list. Pero en el inicio se encuentra vacía hasta que sea rellenada con los 2 primeros frames de la captura de video. Para solucionar esto, añadimos dos valores vacíos a status_list y de este modo solucionamos el error:
```html
# El Error en cuestion:
  File "a:\Programacion Web\(Cursos)-Udemy\Python Mega Course Buils 10 real world Applications\Python\section18.py", line 69, in <module>
    if status_list[-1]==0 and status_list[-2]==1:
                              ~~~~~~~~~~~^^^^
IndexError: list index out of range

# Solución:
status_list=[None, None]
```
Solcionado, sin embargo, puede pasar que el programa termine con un objeto en detección, por lo que dejará uno de los pares de timepo sin su tiempo final. Para solucionar esto añadiremos un bloque en el condicional que cierra el bucle while:
```html
if key==ord('q'):
    # Añadir tiempo final si el progrmaa se cierra con objeto en pantalla (haciendo que no genere tiempo de cierre)
    if status==1:
        times.append(datetime.now())
    break
```
Ahora, pasaremos la lista de times a pandas DataFrame y eso a un archivo csv, este csv tendrá una columna con times de entrada y times de salida:
```html
# improtamos Pandas
import pandas

# Creamos variable al inicio para crear el DataFrame:
# Variable DataFrame de panda para recoger los datos de la lista times
df=pandas.DataFrame(columns=["Start","End"])

# Al final, fuera del bucle while, añadimos un bucle para iterar a través de la lista times e ir añadiendo valores al DataFrame
# Bucle para iterar (tantas veces como valores tenga la lista times, con un step de 2 - valores de 2 en 2-) por la lista times e incluir los datos en la variable DataFrame (df)
for i in range(0, len(times),2):
    new_row=pandas.DataFrame({"Start":[times[i]], "End":[times[i+1]]})
    df=pandas.concat([df, new_row], ignore_index=True)

# Creación del archivo CSV
df.to_csv("downloads/Times.csv")
```
ERROR DE SINTAXIS, REVISAR:
- Create a new row as a separate DataFrame with square brackets around the values to make them lists
- Use pd.concat() instead of the deprecated append() method
- Pass ignore_index=True to reset the index of the combined DataFrame

# Section19
## Clase 160
### Introduction to Bokeh
Bokeh Docs -> https://docs.bokeh.org/en/latest/
<br>

Con Bokeh podemos tomar datos de un csv y mostrarlos de manera gráfica e interactiva (apoyándonos en Jupyter Notebook). Veremos:
- diagramas de líneas
- dispersión de puntos
- gráficos combinados
- Timelines

## Clase 161
### Installing Bokeh
If you haven't installed Bokeh yet, you can easily install it with pip from the terminal:
```html
pip install bokeh 

Or you use pip3:

pip3 install bokeh 
```

## Clase 162
### Your First Bokeh Plot
Necesitaremos instalar Bokeh y Jupyter Notebook
```html
pip3 install bokeh 
pip3 install jupyter notebook
```
Luego iniciaremos Jupyter Notebook, para ello escribimos **jupyter notebook** en la consola (normal) y accedemos a uno de los enlaces que nos lanza para abrir JN en el navegador. Una vez iniciado creamos un New>Python3 (ipkernel); y lo nombramos "Graphs".
<br>

Emplearemos comentarios en JN para entender mejor el desarrollo. A partir de este punto, crearemos todo el contenido de la clase en Jupyter Notebook; para verlo, acceder al archivo Graphs.ipynb.

## Clase 163
### Exercise: Plotting Triangles and Circles
Write two code snippets, each producing the following graphs. The first graph has triangles as glyphs and the second graph has circles as glyphs. You can use triangle , and circle  instead of line. You should have the same coordinates, as shown in the plots below.

![163.a](/img/Clase163a.png)
![163.b](/img/Clase163b.png) 

## Clase 164
### Solution: Plotting Triangles and Circles
####Snippet producing the triangle-based plot
```html
#Making a basic Bokeh line graph
 
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
 
#prepare some data
x=[3,7.5,10]
y=[3,6,9]
 
#prepare the output file
output_file("Line.html")
 
#create a figure object
f=figure()
 
#create line plot
f.triangle(x,y)
 
#write the plot in the figure object
show(f)
```
**DEPRECADO** BokehDeprecationWarning: 'triangle() method' was deprecated in Bokeh 3.4.0 and will be removed, use "scatter(marker='triangle', ...) instead" instead.

#### Snippet producing the circle based plot
```html
#Making a basic Bokeh line graph
 
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
 
#prepare some data
x=[3,7.5,10]
y=[3,6,9]
 
#prepare the output file
output_file("Line.html")
 
#create a figure object
f=figure()
 
#create line plot
f.circle(x,y)
 
#write the plot in the figure object
show(f)
```
HABRIA QUE AÑADIR ADEMÁS EL **RADIO 0,1**

## Clase 165
###  Using Bokeh with Pandas
```html
#Making basic bokeh Graph

#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data
df=pandas.read_csv("downloads/data.csv")
x=df["x"]
y=df["y"]

#prepare de output file
output_file("Line_from_csv.html")

#create figure object
f=figure()

#create line plot
f.line(x,y)
#f.triangle(x,y) -> BokehDeprecationWarning: 'triangle() method' was deprecated in Bokeh 3.4.0 and will be removed, use "scatter(marker='triangle', ...) instead" instead.
#f.circle(x,y,0.1)

#write the plot in the figure boject
show(f)

#Crt+Enter para ver el gráfico
#Jugar con las pestañas laterales
```

## Clase 166
### Exercise: Plotting Education Data
The following line graph shows the percentage of women who have received a bachelor's degree over the years in the USA. The graph was produced from the Year  and Engineering columns of the CSV file provided in the following link: https://pythonizing.github.io/data/bachelors.csv
- Try to reproduce the graph using Bokeh.
![Ejercicio 166](/img/Clase166.png) 

## Clase 167
### Solution: Plotting Education Data
```html
#Plotting percentage of women who received an engineering degree over years
 
#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
 
#prepare some data
df=pandas.read_csv("https://pythonizing.github.io/data/bachelors.csv")
x=df["Year"]
y=df["Engineering"]
 
#prepare the output file
output_file("Line_from_bachelors.html")
 
#create a figure object
f=figure()
 
#create line plot
f.line(x,y)
 
#write the plot in the figure object
show(f)
```

## Clase 168
### Note on Loading Excel Files
In the next lecture, you will learn how to load Excel files in Python with pandas. For this, you need pandas (which you have already installed) and also two other dependencies that pandas needs for opening Excel files. You can install them with pip:
- pip3.13 install openpyxl (needed to load Excel .xlsx files)
- pip3.13 install xlrd (needed to load Excel old .xls files)

## Clase 169
### Changing Plot Properties
You can add a title to the plot, set the figure width and height, change title font, etc. Below is a summary of properties which can be added to change the style of the plot:
```html
import pandas
from bokeh.plotting import figure, output_file, show
 
p=figure(width=500,height=400, tools='pan')
 
p.title.text="Cool Data"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Date"
p.yaxis.axis_label="Intensity"    
 
p.line([1,2,3],[4,5,6])
output_file("graph.html")
show(p)
```

## Clase 170
### Exercise: Plotting Weather Data
Produce the following graph using the data from this Excel file: https://github.com/pythonizing/data/raw/master/verlegenhuken.xlsx
![Ejercicio 170](/img/Clase170.png) 
**Some notes:** Temperature and pressure values in the Excel file have a scale factor of 10; you'll have to divide those values by 10 to get the actual observations.
- And, yes, you can set your own fonts and colors, but be accurate with the rest of the plot elements.

## Clase 171
### Solution: Plotting Weather Data
```html
#CLASE 170
import pandas 
from bokeh.plotting import figure, output_file, show
 
df=pandas.read_excel("downloads/verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
 
p=figure(width=500,height=400,tools='pan')
 
p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"    
 
p.scatter(df["Temperature"],df["Pressure"],size=0.5)
output_file("Weather.html")
show(p)
```
**Cicle**: DEPRECATED-> use scatter instead
**File**: error al intentar tomar la url de github, he descargado el archivo para trbajar con él

## Clase 172
###
## Clase 173
###
## Clase 174
###
## Clase 175
###
## Clase 176
###



