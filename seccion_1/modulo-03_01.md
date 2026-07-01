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