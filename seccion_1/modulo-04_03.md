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