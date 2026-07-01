# While loops

## Introducción a loops (bucles)
- Aprenderemos cómo ​hacer que las computadoras realicen tareas repetitivas, ​que es otra piedra angular de la programación.
- La capacidad de realizar tareas repetitivas con precisión y ​no cansarse nunca es la razón por la ​que los ordenadores son tan buenos para la automatización.
- En los próximos vídeos, exploraremos ​tres técnicas para automatizar las tareas repetitivas
    - While loops
    - For loops
    - Recursion

---

## Reseña: Que es un While loop?
- Los siguientes bloques de código se usarán en el próximo video:
```Python
x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))
```

---

## Que es un While loop?
- Los bucles while ordenan a tu ordenador que ​ejecute continuamente tu código ​basándose en el valor de una condición
- El cuerpo del bloque se puede ​ejecutar varias veces en lugar de sólo una
- Initializing (inicialización): Es dar un valor inicial a un variable.

---

## Anatomía de un While loop
- Un while loop se ejecuta constantemente mientras la condición sea verdadera.
- Comienza con el `keyword` `while`, seguido de una condición a evaluar, por último un `:` para indicar que el bloque de código que sigue es parte del bucle.
- El bloque de código que sigue al `while` debe estar indentado (sangrado) para indicar que es parte del bucle.
- Este bloque de código se ejecutará una y otra vez mientras la condición sea verdadera.
- Una vez sea falsa la condición, el bucle se detendrá y el programa continuará con la siguiente línea de código después del bucle.

---

## Reseña: Más ejemplos de While loops
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)
```

```Python
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)
```

```Python
username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
#This code will give an error because get_username is not defined
```

---

## Más ejemplos de While loops
- Los ejemplos son de bucles while dentro de una función
- Estamos utilizando una expresión ligeramente diferente a la anterior ​x + = 1 es una versión abreviada de x es igual a x +1. 
- Lo importante a recordar es que la condición usada por el bucle while ​necesita evaluarse a verdadero o falso
- No importa si esto se hace utilizando operadores de comparación o ​llamando a funciones adicionales. 

---

## Reseña: Por qué inicializar variables importa?
- Los siguientes bloques de código se usarán en el próximo video:
```Python
while my_variable < 10:
    print("Hello")
    my_variable += 1
#This code will give a NameError
#Variable is not defined 
```

```Python
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1
```

```Python
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1
```

---

## Por qué inicializar variables importa?
- Uno de los errores más comunes es olvidar ​inicializar las variables con el valor correcto.
- Qué ocurre cuando no inicializamos una variables
    - El primer resultado posible y el más fácil de ​detectar es que Python podría generar un error ​que nos diga que estamos usando una variable que no hemos definido.
        - Posiblemente genere un error de tipo NameError, que nos dice que la variable no está definida.
    - si reutilizamos ​una variable sin establecer el valor correcto desde el principio, ​seguirá teniendo el valor de antes
        - Esto puede causar que el bucle while nunca se ejecute, o que se ejecute más veces de lo esperado.
        - En este caso, puede ser más difícil ​detectar el problema porque Python no genera ningún error.
        - Si tienes un bucle que no funciona correctamente y no se comporta como se esperaba, ​es una buena idea comprobar si todas las variables están inicializadas correctamente.

---

## Reseña: Loops infinitos y como romperlos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
while x % 2 == 0:
    x = x / 2
#No output
```

```Python
if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output
```

```Python
while x != 0 and x % 2 == 0:
    x = x / 2
#No output
```

```Python
while True:
    do_something_cool()
    if user_requested_to_stop():
        break
#This code will give an error because do_something_cool is not defined
```

---

## Loops infinitos y como romperlos
- El cuerpo del bucle while debe ​asegurarse de que la condición que se está comprobando cambiará
- Si no cambia, es posible que el `loop` nunca termine, ​y obtenemos lo que se llama un `loop` infinito, ​un ciclo que sigue ejecutándose y ​nunca se detiene.
- Podemos usar un condicional `if` previo al bucle para asegurarnos de que la condición se cumpla antes de entrar en el bucle.
- También podemos anidar la condición dentro del bucle con un operador `and` para asegurarnos de que la condición se cumpla antes de entrar en el bucle.
- A veces queremos que un bucle sea infinito, por ejemplo al hacer un `ping` a un servidor, normalmente se puede romper con las teclas `Ctrl + C` o `Cmd + C` en la terminal.
- En Python podemos usar la `keyword` `break` para romper un bucle infinito, normalmente dentro de un condicional `if`.