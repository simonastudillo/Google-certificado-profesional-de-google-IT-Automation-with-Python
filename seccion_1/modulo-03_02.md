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

---

# Reseña: Más ejemplos de bucles for
- Los siguientes bloques de código se usarán en el próximo video:

- Ejemplo 1:
    - Define la variable `product` como 1
    - Usa el `loop` para iterar sobre los números del 1 al 9
    - Multiplica `product` por cada número en el rango
    - Esto significa que en la primera iteración, `product` es 1 * 1 = 1, en la segunda iteración, `product` es 1 * 2 = 2, y así sucesivamente
```Python
product = 1
for n in range(1,10):
  product = product * n

print(product)
```

- Ejemplo 2:
    - Define la función `to_celsius` que convierte grados Fahrenheit a Celsius
    - Usa un bucle for para iterar sobre los números del 0 al 100
    - En cada iteración, imprime el valor de `x` y su conversión a Celsius usando la función `to_celsius`
    - Esto significa que en la primera iteración, `x` es 0 y su conversión a Celsius es -17.77777777777778, en la segunda iteración, `x` es 10 y su conversión a Celsius es -12.222222222222221, y así sucesivamente
```Python
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))
```