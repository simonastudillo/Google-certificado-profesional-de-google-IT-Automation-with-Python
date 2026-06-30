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