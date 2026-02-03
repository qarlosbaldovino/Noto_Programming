# Funciones PYTHON <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/960px-Python-logo-notext.svg.png" width="30">

1.  [Funciones interesantes](#id1)
    *   [Maketrans y translate](#id1)
    *   [For](#id1.2)
    *   [Funciones Lambda](#id1.3)
    *   [Excepciones](#id1.4)
2.  [Listas](#id2)
    *   [Enumerate](#id2.2)
    *   [Zip](#id2.3)

<div id = 'id1'/>

## Funciones interesantes
### str.**maketrans** y **translate**
 ```python
 testword = str.maketrans('aei' + 'aei'.upper() ,"AEI" + "AEI".lower())
```
_Lo que hace __maketrans__ es hacer el translado de palabras a su CODIGO ASCII y hacer una especie de __diccionario__ con la primer letra del primer parametro y la primer letra del segundo parametro, y así con todos los restantes._

```
{97: 65, 101: 69, 105: 73, 65: 97, 69: 101, 73: 105}
a    A    e    E   i   I    A   a   E   e   I    i
```
_97 es 'a' y 65 es 'A'_

Esto nos va a servir para hacer la traduccion de nuestra palabra con __translate()__

```python
new_word = 'cACa'.translate(testword)
print(new_word)
```
_tenemos la palabra "cACa" y vamos a usar __translate__ y le vamos a pasar como parametro al diccionario que hemos creado: _testword__

_Lo que estamos por hacer es cuando tenemos 'A', nos pasará a: 'a'. y viceversa. Tenemos finalmente este resultado:_

```
caCA
```
---
<div id = 'id1.2'/>

### **for** 
Formas de usarlo:
```python
numeros = [1,2,3,4,5]

for num in numeros:
    if num % 2 == 0:
        print(f"{num} es par")
```
```python
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
```
---
<div id = 'id1.3'/>

### **Funciones Lambda**

Se las conoce como _**funciones anonimas**_ (porque no llevan nombre) y son una alternativa a las funciones creadas con _**def**_. Se las usan normalmente dentro de funciones complejas como _**filter()**_ o _**map()**_.
```python
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
```
_output_
```python
[2, 4]
[1, 4, 9, 16, 25]
```
---
<div id = 'id1.4'/>

### **Excepciones** (_try,except,else y finally_)

Las excepciones nos pueden servir para poder _"atrapar"_, anticiparnos, manejar y responder por **errores**

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')
```
_Acá estamos haciendo una división en **try**  y si por alguna razón dividimos por **0**, entra a la excepción y nos imprime el error. Con **finally** se imprime si o sí. Le estamos canchereando que este codigo siempre anda y nunca se rompe._
```python
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')
```
_Acá podemos hacer un grupo de excepciónes y darle un nombre **e**, e incluso imprimir el error que nos da el compilador._
---
<div id = 'id1.5'/>

### **Raise**
Con __raise__ podemos de alguna manera _"lanzar"_ nuestros propios erroes.

```python
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
```
En este caso si la edad es menor a 0, generamos un _ValueError_

```python
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')
```
Podemos tambien imprimir tanta el mensaje original como tambien agregarle el nuestro:

• En primer caso _From None_ solo imprime nuestro mensaje.

• En el segundo caso _From e_ ademas del mensaje, imprime el error del compilador.

### Assert
Tambien tenemos _assert_ que es una forma mas abreviada de _raise_ y _AssertionError_

```python
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')
```


---
<div id = 'id2'/>

## Listas
### **append()** y **insert()**
```python
languages = ['Spanish', 'English', 'Japanese']
languages.append('Chinese')

print(languages)

languages.insert(0,'Cantonese')

print(languages)
```
_output_
```python
#Append (final)
['Spanish', 'English', 'Japanese', 'Chinese'] 
#Insert index 0 
['Cantonese', 'Spanish', 'English', 'Japanese', 'Chinese']
```
---
<div id = 'id2.2'/>

### **enumerate**
```python
languages = ['Spanish', 'English', 'Japanese']
enumerate_languages = list(enumerate(languages), start = 1)
```
_output_
```
[(1, 'Spanish'), (2, 'English'), (3, 'Japanese')]
```
_Como vemos, __enumerate()__ nos crea una lista de tuplas con numero de orden y el valor de item de la lista_.

##### _Otro uso:_
```python
for index, lang in enumerate(languages, start = 1):
    print(index,lang)
```
---
<div id = 'id2.3'/>

### **Zip**
```python
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Qoqo")

x = list(zip(a, b))

print(x)
```
_Como vemos, __zip()__ es similar a __enumerate()__ pero podemos tenemos que pasarle dos parámetros para que los una._

_output_
```
[('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
```


_En este caso, vemos que _"Qoqo"_ sobra y no lo imprime porque no puede unirlo con otro valor del primer parámetro (_a_)_