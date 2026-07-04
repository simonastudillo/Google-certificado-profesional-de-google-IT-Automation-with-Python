# List (listas)

## Reseña: Qué es una lista?
- Los siguientes bloques de código se usarán en el próximo video:
```Python
x = ["Now", "we", "are", "cooking!"]

type(x)
print(x)
len(x)
"are" in x
"Today" in x
print(x[0])
print(x[3])
print(x[4])

#This last line will throw an error

x[1:3]
x[:2]
x[2:]
```

---

## Qué es una lista?
- Las listas están hechas para almacenar múltiples elementos en una sola variable.
- Piensa en ellas como cajas largas con el espacio adentro del caja dividido en diferentes ranuras
- cada una de ella contiene un valor asociado.
- usamos los corchetes `[]` para crear una lista y separar los elementos con comas `,`.
- Es del tipo `<class 'list'>` y puede contener cualquier tipo de dato, incluso otras listas.
- Podemos usar funciones como `len()` para obtener el número de elementos en la lista
- al igual que con las cadenas, podemos usar el operador `in` para verificar si un elemento está en la lista.
- tambien, como en las cdenas podemos usar indices para acceder a los elementos de la lista, y podemos usar slicing para obtener sublistas.

---

## Listas definidas
- Las listas se definen usando corchetes, con los elementos separados por comas: `my_list = ["This", "is", "a", "list"].`
- Puedes usar la palabra clave `in` para comprobar si una lista contiene un elemento determinado. Si el elemento está presente, devolverá `True`. Si no se encuentra en la lista, devolverá `False`. - Por ejemplo, `"This"` en `my_list` devolvería `True` en nuestro ejemplo.
- También puedes usar índices para acceder a elementos específicos según su posición.
- Puedes acceder al primer elemento de una lista con `my_list[0]`, lo que te permitiría acceder a la cadena "This".
- En Python, las listas y las cadenas son bastante similares.
- Ambas son ejemplos de secuencias de datos. Las secuencias tienen propiedades similares, como:
1. Poder iterar sobre ellas usando bucles `for`. 
2. Admitir la indexación;
3. Utilizar la función `len` para hallar la longitud de la secuencia;
4. Utilizar el operador de suma (+) para concatenar; y
5. Utilizar la palabra clave `in` para comprobar si la secuencia contiene un valor. Comprender estos conceptos permite aplicarlos también a otros tipos de secuencias.

---

## Reseña: Modificar el contenido de una lista
- Los siguientes bloques de código se usarán en el próximo video:
```Python
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.remove("Pear")
#This will throw an error

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)
```

---

## Modificar el contenido de una lista
- La diferencia entre string y listas es que las listas son mutables, lo que significa que podemos cambiar sus elementos después de haberlas creado.
- `append()` agrega un elemento al final de la lista.
- `insert()` agrega un elemento en una posición específica de la lista.
- `remove()` elimina un elemento de la lista.
- `pop()` elimina un elemento de la lista en una posición específica y devuelve el elemento eliminado.
- La diferencia entre `remove()` y `pop()` es que `remove()` elimina un elemento por su valor, mientras que `pop()` elimina un elemento por su índice.

---

## Reseña: Listas y tuplas
- Los siguientes bloques de código se usarán en el próximo video:
```Python
fullname = ('Grace', 'M', 'Hopper')

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
type(result)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(result)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
hours, minutes, seconds = result
print(hours, minutes, seconds)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
```

---

## Listas y tuplas
- `string`: son una secuencia de caracteres, y son inmutables.
- `list`: son una secuencia de elementos, y son mutables.
- `tuple`: son una secuencia de elementos, y son inmutables.
- Para definir una tupla, usamos paréntesis `()` en lugar de corchetes `[]`.
- Ejemplo: `my_tuple = ("This", "is", "a", "tuple")`
- Cuando usas tuplas, la posición de los elementos suelen tener un significado, por eso son inmutables.
- Las tuplas se puedes descomponer en variables individuales, lo que se conoce como "unpacking". 
- Esto es útil cuando una función devuelve múltiples valores, ya que podemos asignar cada valor a una variable diferente.
- ejemplo: `hours, minutes, seconds = convert_seconds(5000)` asigna los valores devueltos por la función a las variables `hours`, `minutes` y `seconds`.

---

## Tuplas
- Las tuplas son como las listas, en el sentido que pueden contener múltiples elementos de diferentes tipos, pero son inmutables.
- Esto quiere decir que una vez que se crea una tupla, no se puede cambiar su contenido, ni agregar, ni eliminar elementos.
- Son útiles cuando queremos preservar la integridad de los datos, ya que no se pueden modificar accidentalmente.
- Son usados generalmente como valores de retorno de funciones, para devolver múltiples valores a la vez.

---

## Reseña: Iterando sobre listas y tuplas
- Los siguientes bloques de código se usarán en el próximo video:
```Python
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
```

---

## Iterando sobre listas y tuplas
- Podemos usar bucles `for` para iterar sobre listas y tuplas.
- Esto se hace usando la sintaxis `for item in sequence:`, donde `sequence` puede ser una lista o una tupla.
- Podemos usar la función `enumerate()` para obtener tanto el índice como el valor de cada elemento en la secuencia.
- También podemos usar la técnica de "unpacking" para descomponer los elementos de una tupla en variables individuales dentro del bucle `for`.
- Para descomponer una tupla en variables individuales, podemos usar la sintaxis `for var1, var2 in sequence:`, donde `sequence` es una lista de tuplas.
- Error común: Querer acceder a un elemento de una lista o tupla usando un índice, aunque es común en otros lenguajes, en Python es posible pero no es recomendado, ya que es más eficiente iterar directamente sobre los elementos de la secuencia.

---

## Iterar sobre listas usando `enumerate()`
- Los bucles `for` permiten recorrer cada elemento de la lista, pasando el elemento al bucle `for` como una variable.
- ¿qué ocurre si queremos acceder a los elementos de una lista, junto con el índice del elemento en cuestión?
- Esto se puede hacer usando la función `enumerate()`.
- La función `enumerate()` recibe una lista como parámetro y devuelve una tupla para cada elemento de la lista.
- El primer valor de la tupla es el índice y el segundo valor es el elemento en sí.