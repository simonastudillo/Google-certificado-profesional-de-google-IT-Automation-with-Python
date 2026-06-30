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