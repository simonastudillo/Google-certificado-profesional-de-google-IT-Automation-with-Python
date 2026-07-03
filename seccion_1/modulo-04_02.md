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