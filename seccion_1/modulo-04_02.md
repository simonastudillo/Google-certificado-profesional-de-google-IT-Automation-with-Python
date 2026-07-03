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