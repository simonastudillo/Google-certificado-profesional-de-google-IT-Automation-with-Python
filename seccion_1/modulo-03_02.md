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

---

## Identificar: Seleccionar la instrucción iterativa correcta
1. You want to print 3 numbers from a list.
```Python
for i in [8,9,10]:
    print(i)
```

2. You want to print the message “Access denied” 5 times.
```Python
for i in range(5):
    print("Access denied")
```

3. You want to print out a sequence of numbers starting at 10 and ending at 30.
```Python
for i in range(10, 31):
    print(i)
```

4. You want to print a message that tells the user to “try again” as long as the value of the attempt variable is 5 or less, and you want to increase the value of this variable by 1 each time it passes through the loop.
```Python
attempt = 1
while attempt <= 5:
    print("Try again")
    attempt += 1
```

5. You want to print out the numbers 20, 19, 18, 17, and 16.
```Python
i = 20
while i >= 15:
    print(i)
    i -= 1
```

6. You want to welcome 3 users from a list by their name (for example, “Welcome, Emerick Larson”).
```Python
users = ["Emerick Larson", "Taylor Smith", "Alex Johnson"]
for user in users:
    print("Welcome, " + user)
```

---

## Reseña: Bucles for anidados
- Los siguientes bloques de código se usarán en el próximo video:

```Python
for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()
```

```Python
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)
```

```Python
for element in long_list:
  do_something(element)

for element1 in long_list:
  for element2 in long_list:
    do_something(element1, element2)
```

---

## Bucles for anidados
- Bucles anidados son bucles dentro de bucles.
- En el ejemplo, se usa un parámetro especial de la función `print()` llamado `end` para evitar que se agregue un salto de línea después de cada impresión. Esto permite que los resultados se impriman en la misma línea.
    - `end=" "` agrega un espacio después de cada impresión en lugar de un salto de línea.
- En el ejemplo tambien se utiliza `print()` sin argumentos para agregar un salto de línea después de cada iteración del bucle externo. Esto asegura que cada conjunto de resultados se imprima en una nueva línea.
- Tener en consideración que los bucles anidados pueden aumentar significativamente la complejidad del código y el tiempo de ejecución, especialmente si se trabaja con listas largas o grandes cantidades de datos. Por lo tanto, es importante usarlos con cuidado y considerar alternativas si es posible.
- Esto no significa que los bucles anidados sean malos, sino que hay que tener cuidado al usarlos y considerar alternativas si es posible.

---

## Strings y bucles for
- `Bucles for`: Te permiten iterar sobre una secuencia de valores, como números, nombres, o lineas en un archivo. Tambien puedes usar bucles for para iterar sobre los caracteres de un string.
- `String`: Es una secuencia de caracteres, como letras, números y símbolos. En Python, los strings se representan entre comillas simples o dobles, por ejemplo `"Hello World"` o `'Python'`.

>[!TIP]
> Recuerda: no puedes mezclar los tipos de comillas en un string. Por ejemplo, `"Hello World'` o `'Python"` no son válidos. Debes usar comillas simples o dobles de manera consistente.

>[!NOTE]
> Si un número está entre comillas, se considera un string. Por ejemplo, `"123"` es un string, mientras que `123` es un número entero.

>[!TIP]
> Todos los bucles for se pueden escribir como bucles while, pero los bucles for son más concisos y fáciles de leer. Por lo tanto, se recomienda usar bucles for cuando sea posible.

---

## Looping sobre un string
- Hacer u loop sobre un string permite al programador examinar cada carácter individualmente.
- Hay muchas manera de hacer un loop sobre un string y el uso de cada una de ella depende del contexto y de lo que se quiera lograr.
- Hacer un loop sobre un string signica iterar sobre cada carácter del string, uno a la vez, y realizar alguna acción con cada carácter.
- For loop
```Python
greeting = 'Hello'
for char in greeting:
	print(char)
# H
# e
# l
# l
# o
```
- Iterar sobre la posición de cada carácter en un string usando `range()` y `len()`
    - `len()` devuelve la longitud del string, es decir, el número de caracteres que contiene.
```Python
for i in range(len(greeting)):
	print(i)
```
- While loop con indices:  El índice es un número que representa la posición de un carácter en un string. Los índices comienzan en 0, por lo que el primer carácter tiene índice 0, el segundo carácter tiene índice 1, y así sucesivamente.
    - `greeting[index]` accede al carácter en la posición `index` del string `greeting`.
    - `greeting[0]` devuelve el primer carácter del string, que es 'H'.
```Python
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
```

>[!TIP]
> Recuerda: Puedes detener la ejecución de un bucle en cualquier momento usando la instrucción `break`. Esto es útil si quieres salir del bucle antes de que termine todas las iteraciones.

- while loop con segmentación
    - `greeting[index:index+1]` devuelve una subcadena del string `greeting`, que contiene solo el carácter en la posición `index`. Esto es útil si quieres trabajar con subcadenas en lugar de caracteres individuales.
    - Ejemplo: `greeting[0:0+1]`: devuelve 'H', que es el primer carácter del string.
```Python
greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1
```
- Comprensión de listas
    - La comprensión de listas es una forma concisa de crear listas en Python. Permite generar una nueva lista aplicando una expresión a cada elemento de una secuencia existente.
    - Se itera sobre cada elemento de la variable `numbers`, cada iteración se asigna a la variable `x`, y se calcula el cuadrado de `x` usando la expresión `x ** 2`. El resultado se agrega a la nueva lista `squared_numbers`.
```Python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
# [1, 4, 9, 16, 25]
```
- Funciones avanzadas:
    - `map`: Puedes encontrar más información [aquí](https://www.tutorialsteacher.com/python/python-map-function)
    - `zip`: Puedes encontrar más información [aquí](https://pythonprogramming.net/zip-intermediate-python-tutorial/)

---

## Slice y Join strings
- `Slice`: Es una técnica que permite extraer una parte de un string. Se puede usar para obtener subcadenas, caracteres específicos o incluso invertir un string.
- `Join`: Es un método que permite unir una lista de strings en un solo string, utilizando un separador especificado. Esto es útil para combinar palabras, frases o cualquier conjunto de strings en una sola cadena de texto.
- Cómo hacer un `slice` de un string:
    - Tenemos que usar la sintaxis `string[start:end]`, donde `start` es el índice del primer carácter que queremos incluir en el slice, y `end` es el índice del primer carácter que NO queremos incluir en el slice.
```Python
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
```
- Tambien podemos usar índices negativos para hacer un slice desde el final del string:
    - Recuerda considerar que el índice -1 representa el último carácter del string, -2 representa el penúltimo carácter, y así sucesivamente.
```Python
# Prints “Earthlings” again
print(string1[-10:])
```
- Los `slice` tambien permiten usar algo llamado `stride` o `step`, que es un valor que indica cuántos caracteres saltar entre cada carácter incluido en el slice. Esto se hace agregando un tercer parámetro a la sintaxis del slice: `string[start:end:step]`.
    - `0::2` significa que queremos empezar desde el índice 0, ir hasta el final del string, y tomar cada segundo carácter.
    - `::-1` invierte el string, ya que el `step` es -1, lo que significa que se recorre el string de derecha a izquierda.
    - Al no indicar el valor de `start` o `end`, se asume que queremos empezar desde el principio o ir hasta el final del string, respectivamente.
```Python
string1 = "Greetings, Earthlings"
# Prints “Getns atlns”
print(string1[0::2])

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1])
```
- Join strings: 
- Podemos hacer un `join` de string utilizando el operado `+`, que concatena dos o más strings en uno solo. Esto es útil para combinar palabras, frases o cualquier conjunto de strings en una sola cadena de texto.
- El método `join()` se utiliza para unir una lista de strings en un solo string, utilizando un separador especificado.
    - La sintaxis es: `separator.join(iterable)`, donde `separator` es el string que se utilizará como separador entre los elementos de la lista, y `iterable` es la lista de strings que queremos unir.
```Python
# Prints “Hello world”
print("Hello" + " " + "world")

greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"
```
- Combinar `slice` y `join` strings:
    - utilizemos un ejemplo de formatear el número de teléfono `2025551212` para usar el formato de U.S.
```Python
phonenum = '2025551212'

# The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"
# The next 3 digits are called the “exchange”:
exchange = phonenum[3:6]
# The last 4 digits are the line number:
line = phonenum[-4:]
# Put the pieces back together into a nicely formatted string:
area_code + " " + exchange + "-" + line
```
- Hagamos lo mismo en una función
```Python
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')
# Prints “(202) 555-1212”
```

---

## Reseña: Errores comunes en bucles for
- Los siguientes bloques de código se usarán en el próximo video:

```Python
for x in 25:
    print(x)

#this will produce an error
```

```Python
for x in range(25):
    print(x)

#this will make the error go away
```

```Python
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])
```

```Python
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")
```

