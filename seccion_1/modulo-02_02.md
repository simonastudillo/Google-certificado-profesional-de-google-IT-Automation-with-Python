# Funciones

## Reseña: Definir funciones
- Eston son algunas funciones que se usarán en el siguiente video
```Python
def greeting(name):
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron")
```

```Python
def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")
```

---

## Definir funciones
- las funciones son el componente crucial
- Hemos visto funciones como `print()` y `str()`.
- En este ejemplo definimos la función `greeting()` que toma un argumento `name` y lo imprime en la consola.
```Python
def greeting(name):
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron")
```
- Usamos la palabra clave `def` para definir una función, seguida del nombre de la función y los paréntesis que contienen cualquier argumento que la función pueda tomar.
- Es importante la sangría, ya que indica qué código pertenece a la función.

---

## Funciones integradas
- Son funcionesque existen en Python y se pueden llamar directamente (como `print()` y `str()`).
- print()
    - Imprime un mensaje en la consola.
    - La función toma argumentos separados por comas y los imprime en la consola.
```Python
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)
```
- type()
    - Devuelve el tipo de un objeto.
```Python
print(type("This is a string"))
```
- str()
    - Util para convertir cualquier tip de dato en un string.
```Python
number = 12
string_representation = str(number)
print(string_representation)
```
- sorted()
    - Ordena los elementos de una lista en orden ascendente por defecto.
    - Tambien puede ordenar strings y tuplas.
```Python
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)
```
- max() y min()
    - Devuelve el valor máximo y mínimo de una lista.
```Python
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))
```

---

## Reseña: Retornar valores
- Las siguientes funciones se usarán de ejemplo en el siguiente video.
```Python
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)
```

---

## Retornar valores
- El trabajo que realizan las funciones puede producir nuevos resultados.
- Usamos la palabra clave return para decirle a ​Python que este es el valor devuelto por una función
- Cuando llamamos a la función, ​almacenamos ese valor en una variable. 
- Nos permite combinar llamadas a ​funciones y operaciones más complejas, ​lo que hace que el código sea más reutilizable
- Las sentencias de retorno en Python son aún más ​interesantes porque podemos ​usarlas para devolver más de un valor (return valor1, valor2, valor3)
- Una función puede devolver `None` si no se especifica un valor de retorno. Esto es útil para funciones que realizan una acción pero no necesitan devolver un valor.
- `None`: Es un tipo especial de dato en Python usado para indicar que no hay valor.

---

## Reseña: Los principios de la reutilización de código
- Las siguientes funciones se usarán de ejemplo en el siguiente video.
```Python
name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))
```

```Python
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")
```

---

## Los principios de la reutilización de código
- Las funciones son potentes porque puedes crear las tuyas propias
- Puedes usarlas para organizar el código de tus scripts en bloques lógicos, ​lo que hace que el código que escribas sea más fácil de usar y reutilizar

---

## Reseña: Estilo de código
- Las siguientes funciones se usarán de ejemplo en el siguiente video.
```Python
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)
#Output is 78.5
```

```Python
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)
#Output is 78.5
```

---

## Estilo de código
- Tener un estilo bueno o malo al escribir código no hace ​mucha diferencia entre que un script tenga éxito o se bloquee
- pero puede marcar una gran diferencia para las personas que lo usan y contribuyen a é
- Un ​estilo de programación deficiente puede dificultar la vida de los especialistas en TI o ​los administradores de sistemas
- Un mal estilo puede incluso causar dolor de cabeza al autor del guion si ha pasado un tiempo ​desde que lo escribió
- Un buen estilo facilita la vida a las personas que tienen que mantener el código y ​les ayuda a entender qué hace y cómo lo hace
- También puede reducir los errores, ya que hace que la actualización del código sea ​más fácil y directa
- Código auto documentado: Escribir de una forma que sea legible y no oculte su intención.
    - Nombre de variables
    - Expresiones
    - Funciones
    - etc.
- En la jerga de programación, cuando reescribimos el código para que sea más autodocumentado, ​llamamos refactorización a este proceso
- Puedes añadir comentarios en caso de que el fragmento de código se más complejo y no se pueda refactorizar para que sea más legible
- En Python los comentarios se escriben con el símbolo #. Todo lo que esté a la derecha de este símbolo se ignora al ejecutar el código.

---

## Guía de estudio: Funciones
- Términos
    - return value (retorno de valor): El valor que una función devuelve a la persona que la llama.
    - parameter (parámetro): Una variable que se pasa a una función para que la use.
    - refactoring code (refactorización de código): Reescribir el código para que sea más legible y no oculte su intención.
- Conocimientos
    - El proposito de `def` es definir una nueva función.
    - Mejores prácticas para escribir código
        - Crea una función reusable: Si un bloque de código se repite, considera convertirlo en una función.
        - Refactoriza tu código: Si un bloque de código es difícil de leer, considera reescribirlo para que sea más legible.
        - Agrega comentarios: Agregar comentarios es parte de un código auto documentado. Usar comentarios permite dejar notas para ti o para otros desarrolladores que puedan leer tu código en el futuro.
- Habilidades de codificación
    - Usa una función que acepte múltiples parámetros.
    - Retorna un valor
```Python
# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))
```
    - Utilice una función para devolver el resultado de una conversión de medida.
    - Usa operadores matemáticos dentro de una función para realizar cálculos.
    - Combina texto con el llamado a un función en print() para mostrar un mensaje en la consola.
    - Convierte el valor retornado a string
    - Llama a la función y realiza un cálculo sobre el valor de retorno dentro de una instrucción print().
```Python
# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in milliliters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in milliliters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in milliliters is " + str(convert_volume(4)))
```