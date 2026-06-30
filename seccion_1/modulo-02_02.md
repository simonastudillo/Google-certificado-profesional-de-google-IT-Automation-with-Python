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