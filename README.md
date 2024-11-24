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
### 
