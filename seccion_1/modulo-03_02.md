# For loops

## Reseña: Qué es un bucle for?
- Los siguientes bloques de código se usarán en el próximo video:
```Python
for x in range(5):
    print(x)
```

```Python
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
```

```Python
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
```

---

## Qué es un bucle for?
- Un bucle for itera sobre una secuencia de valores.
- Se inicia por la `keyword` `for`, seguido de una variable que representa cada elemento de la secuencia, la palabra clave `in`, y finalmente la secuencia sobre la que se itera.
- En Python y en ​muchos otros lenguajes de programación, ​un rango de números comenzará con ​el valor cero de forma predeterminada
- La lista de números ​generados será uno menos que el valor dado. 
- Al usar un bucle for, ​apuntamos la variable definida entre for e in, ​en este caso, x a cada elemento de la secuencia
- Esto significa que en la primera iteración, ​x apunta a una, ​en la segunda, apunta a dos, y así sucesivamente
- Cualquier código que pongamos en el body se ejecutará en cada uno de los valores, un valor a la vez.
- la potencia del bucle for es que ​podemos usarlo para iterar sobre ​una secuencia de valores de cualquier tipo, ​no solo sobre un rango de números
- Por ejemplo, puede ​usarlos para copiar archivos a máquinas, ​procesar el contenido de los archivos, ​instalar software automáticamente y mucho más. 
- Utiliza bucles `for` cuando haya ​una secuencia de elementos que quieras repetir.
- Utilice bucles while cuando desee ​repetir una acción hasta que cambie una condición