# Diccionarios

## Reseña: Qué es un diccionario
- Los siguientes bloques de código se usarán en el próximo video:
```Python
x = {}
type(x)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["txt"]

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
"jpg" in file_counts
"html" in file_counts

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["cfg"] = 8
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["csv"] = 17
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23, 'cfg':8}
del file_counts["cfg"]
print(file_counts)
```

---

## Qué es un diccionario
- Son usados para organizar elementos en colecciones
- Los datos en diccionarios adoptan la forma de pares de clave-valor
- Separamos clave de valor con dos puntos (:)
- Ejemplo: `{"clave1": valor1, "clave2": valor2, "clave3": valor3}`
- a diferencia de listas o tuplas, puedes usar otros elementos que sean integer como indices, como strings, floats, o incluso tuplas como claves
- Para acceder a un valor en un diccionario, usamos la clave entre corchetes: `diccionario[clave]`
- Para agregar un nuevo par clave-valor, usamos la sintaxis: `diccionario[nueva_clave] = nuevo_valor`
- Podemos modificar un archivo usando la misma sintaxis que para agregar un nuevo par clave-valor, ejemplo: `diccionario[clave_existente] = nuevo_valor`
- Para eliminar un par clave-valor, usamos la sintaxis: `del diccionario[clave]`

---

## Definición de diccionarios
- Los diccionarios son otra estructura de datos en Python, similares a las listas.
- Para crear un diccionario, se utilizan llaves: {}.
- Al almacenar valores en un diccionario, primero se especifica la clave, seguida del valor correspondiente, separados por dos puntos.
- Por ejemplo, `animals = { "bears":10, "lions":1, "tigers":2 }` crea un diccionario con tres pares clave-valor, almacenados en la variable `animals`.
- La clave "osos" apunta al valor entero 10, mientras que la clave "leones" apunta al valor entero 1, y "tigres" apunta al valor entero 2.
- Puedes acceder a los valores haciendo referencia a la clave, así: `animales["osos"]`. Esto devolverá el entero 10
- Puedes comprobar si una clave está contenida en un diccionario usando la palabra clave `in`.
- Al igual que en otros usos de esta palabra clave, devolverá `True` si la clave se encuentra en el diccionario; de lo contrario, devolverá `False`.
- Los diccionarios son mutables, lo que significa que se pueden modificar añadiendo, eliminando y reemplazando elementos, de forma similar a las listas.
- Puedes añadir un nuevo par clave-valor a un diccionario: `animales["cebras"] = 2`.
- Puedes modificar el valor de una clave: `animals["bears"] = 11` cambiaría el valor almacenado en la clave `bears` de 10 a 11.
- Puedes eliminar elementos de un diccionario usando la palabra clave `del`: `del animals["lions"]`, eliminarías el par clave-valor del diccionario `animals`.

---

## Reseña: Iterando sobre el contenido de un diccionario
- Los siguientes bloques de código se usarán en el próximo video:
```Python
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts.keys()
file_counts.values()

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in file_counts.values():
  print(value)

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")
```