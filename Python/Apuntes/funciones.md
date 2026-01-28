# Funciones
## Funciones interesantes
### str.**maketrans** y **translate**
 ```python
 testword = str.maketrans('aei' + 'aei'.upper() ,"AEI" + "AEI".lower())
```
_lo que hace __maketrans__ es hacer el translado de palabras a su CODIGO ASCII y hacer una especie de __diccionario__ con la primer letra del primer parametro y la primer letra del segundo parametro, y así con todos los restantes._

```
{97: 65, 101: 69, 105: 73, 65: 97, 69: 101, 73: 105}
a    A    e    E   i   I    A   a   E   e   I    i
```
_97 es 'a' y 65 es 'A'...

Esto nos va a servir para hacer la traduccion de nuestra palabra con __translate()__

```python
new_word = 'cACa'.translate(testword)
print(new_word)
```
_tenemos la palabra "cACa" y vamos a usar __translate__ y le vamos a pasar como parametro al diccionario que hemos creado: _testword_

_Lo que estamos por hacer es cuando tenemos 'A', nos pasará a: 'a'. y viceversa. Tenemos finalmente este resultado:

```
caCA
```
---
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


_En este caso, vemos que _"Qoqo"_ sobra y no lo imprime porque no puede unirlo con otro valor del primer parámetro (_a_).

**_Otro uso:_**
```python
for index, lang in enumerate(languages, start = 1):
    print(index,lang)
```
