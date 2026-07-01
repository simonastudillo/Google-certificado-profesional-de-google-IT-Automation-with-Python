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

---

## Más ejemplos de bucles for
- La función de rango genera una secuencia ​de números que comienzan por cero
- Para comenzar con un número diferente a 0, la función range también ​nos permite especificar ​el primer elemento de la lista que se va a generar
- Lo hacemos indicando 2 parámetros: el primer parámetro es el número inicial y el segundo parámetro es el número final
- De haber comenzado con 0 todo el producto sería 0, ya que cualquier número multiplicado por 0 es 0
- A la función `range` también se le puede pasar un tercer parámetro, que es el paso, es decir, el incremento entre cada número en la secuencia
- ejemplo `range(0, 101, 10)` genera la secuencia 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

>[!TIP]
> Se utiliza 101 como el segundo parámetro en la función `range` para incluir 100 en la secuencia, ya que el segundo parámetro es exclusivo y no se incluye en la secuencia generada.

---

## Un análisis más detallado de la función Range()
- La `keyword` `in` cuando es usada con la función `range()` genera una secuencia de números, los cuales pueden ser usados en el bucle `for` para controlar el punto de partida, el punto final y el incremento de la secuencia.
```Python
 for n in range(x, y, z):
    print(n)
```
- La función `range()` usa una lista de indices que apuntan a valores `integer`, que comienzan con 0.
- Los valores númericos 0, 1, 2, 3, 4 se correlacionar con las posiciones del índice ordinal 1.º, 2.º, 3.º, 4.º, 5.º
- Entonces cuando un llamado al rango de la quinta posición usando `range(5)` apunta al valor númerico 4, que es el último valor de la secuencia generada.

- La función `range()`puede tener hasta 3 parámetros: `range(start, stop, step)`, donde:
    - `start` es el valor inicial de la secuencia (inclusive)
    - `stop` es el valor final de la secuencia (exclusive)
    - `step` es el incremento entre cada número en la secuencia
- Ejemplos
```Python
# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will 
# output the resulting value of "n" as the loop counts from 0 to 10 
# (end-of-range index 11) in incremental steps of 2. This is one 
# method that can be used in Python to print a list of even numbers.


for n in range(0,11,2):
    print(n)


# The loop should print 0, 2, 4, 6, 8, 10
```

```Python
# This loop iterates on the value of the "number" variable in a range
# of 2 to 7+1 (the value of the end-of-range index 7 is excluded, so 
# +1 has been added to the parameter to include the numeric value 7 in 
# the range). The incremental value for the loop is the default of +1.
# The print() function will output the resulting value of "number" 
# multiplied by 3.


for number in range(2,7+1):
    print(number*3)


# The loop should print 6, 9, 12, 15, 18, 21
```


```Python
# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third 
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).


for x in range(2, -2, -1):
    print(x)


# The loop should print 2, 1, 0, -1
```