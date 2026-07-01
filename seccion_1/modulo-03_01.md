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

---

## Guía de estudio: while loops
- Aprendimos la importancia de inicializar variables
- Como resolver un loop infinito con la keyword `break`
- Un While loop es un bucle que se ejecuta mientras una condición sea verdadera
- Errores comunes
    - Falla al inicializar variables
    - Loop infinito no intencional
- Terminos
    - while loop (Bucle while): Indica al ordenador que ejecute un conjunto de instrucciones mientras una condición específica sea verdadera. En otras palabras, los bucles while siguen ejecutando el mismo grupo de instrucciones hasta que la condición se vuelve falsa.
    - Infinite loop (Bucle infinito): Falta un método para salir del bucle, lo que provoca que este se ejecute indefinidamente.
    - break: La instrucción break en Python permite salir de un bucle antes de que su condición sea falsa. Una vez que se encuentra una instrucción break, el flujo de control del programa sale del bucle y continúa ejecutando el código posterior.
    - pass: La instrucción pass en Python es una instrucción de marcador de posición que se utiliza cuando la sintaxis requiere una instrucción, pero no se desea ejecutar ningún código o comando.
- Conceptos matemáticos 
    - Números primos: Números enteros que tienen solo dos factores, que son el número mismo multiplicado por 1. Los primeros diez números primos son 2, 3, 5, 7, 11, 13, 17, 19, 23 y 29. Cada uno de estos números primos solo es divisible por sí mismo y por 1.
    - Factores primos: Números primos que son factores de un número entero. Por ejemplo, los números primos 2 y 5 son los factores primos del número 10 (2 x 5 = 10). Los factores primos de un número entero no producen resto al dividirlo.
    - Divisor: Número (denominador) que se utiliza para dividir a otro número (numerador). Por ejemplo, si el número 10 se divide entre 5, el divisor es 5.
    - Suma de todos los divisores de un número: El resultado de sumar todos los divisores de un número.
    - Tabla de multiplicar: Un número entero multiplicado por una serie de números y sus resultados presentados en forma de tabla o lista. Por ejemplo: 4x1=4, 4x2=8, 4x3=12, 4x4=16, 4x5=20
- Habilidades de códificación
    - Inicializar variables
    - Usar while loop para ejecutar un bloque de código mientras una condición sea verdadera
    - Asegurarte de que el while loop no se ejecute indefinidamente
    - Incrementar un valor dentro de un while loop
```Python
# This function counts the number of integer factors for a 
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 
def count_factors(given_number):

    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded). 
    factor = 1
    count = 1

    # This "if" block will run if the "given_number" equals 0.
    if given_number == 0:
        # If True, the return value will be 0 factors. 
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1
        # When exiting the if block, increment the "factor" variable by 1
        # to divide the "given_number" variable by a new "factor" value
        # inside the while loop.
        factor += 1

    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count


print(count_factors(0)) # Count value should be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8, and 4x6). 
```
    - Inicializar variables dentro de un while loop
    - Usa el keyword break para salir de un while loop
```Python
# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.

# The function accepts a "given_number" variable through its
# parameters.
def addition_table(given_number):

	# The "iterated_number" and "my_sum" variables are initialized with
	# the value of 1. Although the "my_sum" variable does not need any
	# specific initial value, it still must be assigned a data type
	# before being used in the while loop. By initializing "my_sum"
	# with any integer, the data type will be set to int.
	iterated_number = 1
	my_sum = 1

	# The while loop will run while it is True that the
	# "iterated_number" is less than or equal to 5.
	while iterated_number <= 5:

		# The "my_sum" variable is assigned the value of the
		# "given_number" plus the "iterated_number" variables.
		my_sum = given_number + iterated_number

		# Test to see if the "my_sum" variable is greater than 20.
		if my_sum > 20:
			# If True, then use the break keyword to exit the loop.
			break

		# If False, the Python interpreter will move to the next line
		# in the while loop after the if-statement has ended.

		# The print function will output the "given_number" plus
		# the "iterated_number" equals "my_sum".
		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

		# Increment the "iterated_number" before the while loop starts
		# over again to print a new "my_sum" value.
		iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None
```

---

## Test your knowledge: While loops
1. In Python, what do while loops do?
> while loops tell the computer to repeatedly execute a set of instructions while a condition is true.

2. Which techniques can prevent an infinite while loop? Select all that apply.
> Change the value of a variable used in the while condition
> Use the break keyword

3. The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. To solve the problem, you will need to:
- Find the error in the code
- Fix the while loop so there is an exit condition

Hint: Try running your function with the number 0 as the input and observe the result.

Note that Coursera’s code blocks will time out after 5 seconds of running an infinite loop. If you get this timeout error message, it means the infinite loop has not been fixed. 
```Python
def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number!= 0 and number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
```

4. Write a function that takes an argument n and returns the sum of integers from 1 to n. For example, if n=5, your function should add up 1+2+3+4+5 and return 15. If n is less than 1, just return 0. Use a while loop to calculate this sum. 
```Python
def sum_of_integers(n):
  if n < 1:
    return 0


  i = 1
  sum = 0
  while i <= n:
    sum = sum + i
    i = i + 1


  return sum


print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15
```

5. Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:
- Initialize the “multiplier" variable with the starting value
- Complete the while loop condition
- Add an exit point for the loop
- Increment the “multiplier" variable inside the while loop
```Python
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1


    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier 
        if  result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1




multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15


multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25


multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24
```