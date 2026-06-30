# Condicionales

## Reseña: Comparando cosas
- Estos son los ejemplos usados en el siguiente video:
```Python
print(10>1)
#True
print("cat" == "dog")
#False
print (1 != 2)
#True

print(1 < "1")
#Will return a type error

print(1 == "1")
#False

print("Yellow" > "Cyan" and "Brown" > "Magenta")
#False

print(25 > 50 or 1 != 2)
#True

print(not 42 == "Answer")
#True
```

---

## Comparando cosas
- Python puede comparar cosas
    - Si algo es pequeño o grande que otra cosa
- Booleanos: True o False
- Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
    - `==` es igual a
    - `!=` es diferente a
    - `<` es menor que
    - `>` es mayor que
    - `<=` es menor o igual que
    - `>=` es mayor o igual que
- En Python podemos comparar números, strings y booleanos
- Operadores lógicos: `and`, `or`, `not`
    - `and` devuelve True si ambos son True
    - `or` devuelve True si al menos uno es True
    - `not` devuelve True si el valor es False y viceversa

---

## Operadores de comparación con ecuaciones
- Los comparadores retornan un valor booleano (True o False)
- Operador `==` y `!=` 
```Python

print(32 == 30+2)   # The == operator checks if the 2 values are 
True                # equal to each other. If they are equal, 
                    # Python returns a True result.


print(5+10 == 6+7)  # If the two values are not equal, as in the
False               # expression 5+10 == 6+7 (or 15 == 13), Python          
                    # returns a False result.


print(10-4 != 10+4) # The != operator checks if the 2 values are
True                # NOT equal to each other. If true, Python              
                    # returns a True result. 


print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
False               # is false. So, Python returns a False value.
```
- El operador `==` vs el operador `=`
    - El operador `=` es un operador de asignación, no de comparación
    - El operador `==` es un operador de comparación, no de asignación
```Python

# The = equals assignment operator is used to assign a value to a 
# variable.

my_variable = 3*5           # Assigns a value to my_variable      
print(my_variable)          # Printing the variable returns the 
15                          # value assigned to the variable.


                              
# The == equality comparison operator checks if the values of the two
# expressions on either side of the == operator are equivalent to one 
# another.
      
print(my_variable == 3*5)   # Printing the variable returns a Boolean 
True                        # True or False result. 
```
- Mayor que y menor que
```Python

print(11 > 3*3)         # The > operator checks if the left value is
True                    # greater than the right value. If true, it
                        # returns a True result.


print(4/2 > 8-4)        # If the > operator finds that the left value
False                   # is NOT greater than the right value, the
                        # comparison will return a False result.


print(4/2 < 8-4)        # The < operator checks  if the left value is
True                    # less than the right side. If true, the
                        # comparison returns a True result.


print(11 < 3*3)         # If the < operator finds that the left side is False                   
                        # NOT less than the right value, Python returns
False                   # a False result.
```
- Mayor o igual que y menor o igual que
```Python

print(12*2 >= 24)   # The >= operator checks if the left value is
True                # greater than or equal to the right value. 
                    # If one of these conditions is true,  
                    # Python returns a True result. In this case  
                    # the two values are equal. So, the comparison
                    # returns a True result.


print(18/2 >= 15)   # If the >= comparison determines that the left
False               # value is NOT greater than or equal to the
                    # right, it returns a False result.

print(12*2 <= 30)   # The <= operator checks if the left value is
True                # less than or equal to the right value. In 
                    # this case, the left value is less than the
                    # right value. Again, if one of the two 
                    # conditions is true, Python returns a True
                    # result.


print(15 <= 18/2)   # If the <= comparison determines that the left 
False               # value is NOT less than or equal to the right
                    # value, the comparison returns a False result. 
```

---

## Operadores de comparación con strings
- Si utiliza los operadores == (igualdad) y != (distinto de) con cadenas de texto, podrá comprobar si dos cadenas contienen el mismo texto. También puede ordenar alfabéticamente las cadenas utilizando los operadores de comparación > (mayor que), < (menor que), >= (mayor o igual que) y <= (menor o igual que). Al igual que con los tipos de datos numéricos, los operadores de comparación utilizados con cadenas de texto devolverán resultados booleanos (Verdadero o Falso).
- Operador `==` y `!=`
```Python
# The == operator can check if two strings are equal to each other. 
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
True


# In this example, the equality == comparison is between "4 + 5" and
# 4 + 5. Since the left data type is a string and the right data type
# is an integer, the two values cannot be equal. So, the comparison
# returns a False result.
print("4 + 5" == 4 + 5)
False


# The != operator can check if the two strings are NOT equal to each
# other. If they are indeed not equal, then Python returns a True result.
print("rabbit" != "frog")
True


# In this example, the variable event_city has been assigned the string 
# value "Shanghai". This variable is compared to a static string, 
# "Shanghai", using the != operator. As, the strings "Shanghai" and 
# "Shanghai" are the same, the comparison of "Shanghai" != "Shanghai" 
# is false. Accordingly, Python will return a False result.
event_city = "Shanghai"
print(event_city != "Shanghai")
False

# This last example illustrates the result of trying to compare two
# items of different data types using the equality == operator. The
# two items are not equal, so the comparison returns False.
print("three" == 3)
False
```
- Mayor que y menor que
    - En Python, los operadores de comparación mayor que > y menor que < permiten ordenar palabras alfabéticamente. Las letras del alfabeto tienen códigos numéricos en Unicode (también conocidos como valores ASCII).
    - Las letras mayúsculas de la A a la Z se representan con los valores Unicode del 65 al 90. Las letras minúsculas de la a a la z se representan con los valores Unicode del 97 al 122.
![Unicode-Character](image.png)
```Python
# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.
print("Wednesday" > "Friday")
True
 
 
# The less than < operator checks if the left string has a lower 
# Unicode value than the right string. If you reference the Unicode 
# chart above, you can see that all lowercase letters have higher 
# Unicode values than uppercase letters. We can see that B has a 
# Unicode value of 66 and b has a Unicode value of 98. This 
# comparison is the same as 66 < 98, which is true. So, Python will 
# return a True result.
print("Brown" < "brown")
True


# If the strings have the same first few letters, the comparison will 
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values. In this example, 
# both strings share the initial substring "sun", but then have 
# different letters with different Unicode values in the fourth place 
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan")
False


# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")
False


# This last example illustrates the result of trying to compare two
# items of different data types using the less than < operator. The 
# greater than > and less than operators < cannot be used to compare
# two different data types. 
print("Five" < 6)
'''
Error on line 1:
    print("Five" < 6)
TypeError: '<' not supported between instances of 'str' and 'int'
```
- Mayor o igual que y menor o igual que
    - Los operadores mayor o igual que (>=) y menor o igual que (<=) también se pueden usar con cadenas de texto. Al igual que los demás operadores de comparación, devuelven un resultado booleano (verdadero o falso) cuando se comparan dos cadenas.
    - Para comprobar si una cadena tiene un valor Unicode mayor o igual que la(s) primera(s) letra(s) de otra cadena, utilice el operador mayor o igual que: >=
    - Para comprobar si una cadena tiene un valor Unicode menor o igual que la(s) primera(s) letra(s) de otra cadena, utilice el operador menor o igual que: <=
```Python
# Use the Unicode chart in Part 2 to determine if the Unicode values of 
# the first letters of each string are higher, lower, or equal to one
# another. 


var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
 
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)
```

---

## Operadores lógicos
- Los operadores lógicos  son usados para expresiones más complejas.
- Puedes hacer más compleja una comparación uniendo varias comparaciones con los operadores lógicos `and`, `or` y `not`.
    - `and` devuelve True si toda la operación es True
    - `or` devuelve True si al menos una de las operaciones es True
    - `not` devuelve True si la operación es False y viceversa
- Ejemplos:
1. `and`:
```Python
# Example 1

print((6*3 >= 18) and (9+9 <= 36/2))

# Example 2 - Python resuelve los valores de las expresiones antes de compararlos
(6*3 >= 18) and (9+9 <= 36/2)
# becomes
(18 >= 18) and (18 <= 18)

# Example 3

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")
```
2. `or`:
```Python
# Expression1 or Expression2
# Define country and city variables
country = "United States"
city = "New York City"

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))  # True or True = True

# False or True returns True
print(country == "New York City" or city == "New York City")  # False or True = True

# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)  # True or False = True

# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name") # False or False = False
```
3. `not`:
```Python
# Si la expresión condicional es True, el operador not cambiará el resultado a False.
# Si la expresión condicional es False, el operador not cambiará el resultado a True.
# not expression
# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)

# What happens when you negate a False statement? 
# Click Run when you are ready to check your answer.


today = "Monday"
print(not today == "Tuesday") 


# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True. In other words, this expression asks if it is
# false that today is not Tuesday. More succinctly, "not False" means 
# True."

```

---

## Reseña: Ramificación con sentencias if
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
```

---

## Ramificación con sentencias if
- Branching (ramificación): La habilidad de un programa para alternar la secuencia de ejecución de instrucciones dependiendo de una condición.
- Escribimos la palabra clave `if` seguida de ​la condición que queremos comprobar y, a continuación, seguida de dos puntos.
- Después viene el cuerpo del bloque if, ​que tiene una sangría más a la derecha
- El cuerpo del bloque if solo se ​ejecutará cuando la condición se evalúe como verdadera

---

## Reseña: Ramificación con sentencias else
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")
#This code will not have an output. 
```
- Este fragmento de código define una función llamada hint_username.
- La instrucción if len(username) < 3: comprueba la longitud de la cadena username.
- Si la longitud de la cadena es menor a 3 caracteres, se ejecuta el código dentro de la instrucción if.
- La instrucción print("Nombre de usuario no válido. Debe tener al menos 3 caracteres") imprime el mensaje "Nombre de usuario no válido.
- Debe tener al menos 3 caracteres".
- La instrucción else: se ejecuta si la longitud de la cadena username no es menor a 3 caracteres.
- En este caso, se ejecuta el código dentro de la instrucción else, que es la instrucción print("Nombre de usuario válido").
```Python
def is_even(number):
    if number % 2 == 0:
        return True
    return False
#This code has no output
```
- Este fragmento de código define una función llamada `is_even`.
- Esta función comprueba si un número es par.
- La parte del código que verifica si el número es par es `if number % 2 == 0:`.
- Si el número es impar, la función devuelve `False`.

---

## Ramificación con sentencias else
- Podemos extender la ramificación con la sentencia `else` para ejecutar un bloque de código alternativo si la condición del `if` no se cumple.
- Utiliza la palabra clave else seguida de dos puntos para indicar ​el comienzo del bloque else
- el cuerpo del bloque tiene una sangría adicional a la derecha
- recuerda que puedes elegir utilizar tantos o tan pocos espacios como quieras para ​la sangría, pero siempre necesitas sangrar, y ​siempre necesitas utilizar el mismo número de espacios
- Operador módulo: `%`
    - Este operador devuelve el resto de la división de un número por otro
    - Ejemplo: `5 % 2` devuelve `1` porque 5 dividido entre 2 es 2 con un resto de 1
    - Ejemplo: `4 % 2` devuelve `0` porque 4 dividido entre 2 es 2 con un resto de 0
- Recuerda que si haces un return dentro de un bloque if o else, el resto del código no se ejecutará. Por ejemplo, en la función `is_even`, si el número es par, se ejecutará el return True y el resto del código no se ejecutará.

---

## Sentencia else y el operador módulo
- La instrucción `else` sigue a un bloque `if` y se compone de la palabra clave `else` seguida de dos puntos.
- El cuerpo de la instrucción `else` se indenta a la derecha y se ejecutará si la instrucción `if` anterior no se ejecuta.

- operador módulo, representado por el signo de porcentaje: %.
- Este operador realiza la división entera, pero solo devuelve el resto de la operación
- Si dividimos 5 entre 2, el cociente es 2 y el resto es 1
- Dividir 10 entre 5 nos daría un cociente de 2 sin resto, ya que 5 cabe en 10 dos veces sin que sobre nada
- En este caso, 10%5 daría como resultado 0, puesto que no hay resto

---

## Reseña: Sentencia elif
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")
```
- Podemo refactorizar el código anterior utilizando `elif` para simplificar la estructura de control de flujo:
```Python
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")
```

---

## Sentencia elif
- La instrucción `elif` es una abreviatura de "else if" y permite comprobar múltiples condiciones en una estructura de control de flujo.
- ​Python nos proporciona la palabra clave `elif` que nos permite gestionar más de dos casos de comparación.
- ​La principal diferencia entre las sentencias `elif` y `if` ​es que solo podemos escribir un bloque `elif` ​como complemento de un bloque `if`.
- El uso de la bifurcación para determinar el flujo de su programa ​abre un nuevo abanico ​de posibilidades en sus scripts

---

## Ramificación compleja con sentencias elif
- La instrucción `elif` nos permite realizar aún más comparaciones para lograr ramificaciones más complejas
- comienza con la palabra clave `elif`, seguida de la comparación que se va a evaluar.
- A continuación, se colocan dos puntos y, en la siguiente línea, se introduce el bloque de código con sangría a la derecha
- Una instrucción `elif` debe ir después de una instrucción `if` y solo se evaluará si la instrucción `if` se evaluó como falsa

---

## Explore: If, elif, and else statements

---

## Guía de estudio: Condicionales
- Conocimiento
    - x == y: Si x es igual a y, devuelve True. De lo contrario, devuelve False.
    - x != y: Si x no es igual a y, devuelve True. De lo contrario, devuelve False.
    - x < y: Si x es menor que y, devuelve True. De lo contrario, devuelve False.
    - x > y: Si x es mayor que y, devuelve True. De lo contrario, devuelve False.
    - x <= y: Si x es menor o igual a y, devuelve True. De lo contrario, devuelve False.
    - x >= y: Si x es mayor o igual a y, devuelve True. De lo contrario, devuelve False.
- Comparadores en strings
    - "x" == "y": Si "x" es igual a "y", devuelve True. De lo contrario, devuelve False.
    - "x" != "y": Si "x" no es igual a "y", devuelve True. De lo contrario, devuelve False.
    - "x" < "y": Si "x" tiene un valor Unicode menor que la cadena "y", devuelve True. De lo contrario, devuelve False.
    - "x" > "y": Si "x" tiene un valor Unicode mayor que la cadena "y", devuelve True. De lo contrario, devuelve False.
    - "x" <= "y": Si "x" tiene un valor Unicode menor o igual que la cadena "y", devuelve True. De lo contrario, devuelve False.
    - "x" >= "y": Si "x" tiene un valor Unicode mayor o igual que la cadena "y", devuelve True. De lo contrario, devuelve False.
- Operadores lógicos
    - x and y: Si x e y son True, devuelve True. De lo contrario, devuelve False.
    - x or y: Si x o y es True, devuelve True. De lo contrario, devuelve False.
    - not x: Si x es False, devuelve True. De lo contrario, devuelve False.
- Sintaxis if-elif-else
```Python
if condition1: # si condition1 es True, se ejecuta el bloque de código correspondiente
    action1
elif condition2: # si condition1 es False y condition2 es True, se ejecuta el bloque de código correspondiente
    action2
else: # si condition1 y condition2 son False, se ejecuta el bloque de código correspondiente
    action3
```

- Habilidades de codificación
    - Usa un operador de comparación con números
    - Use un operador de comparación con cadenas de texto
```Python
# The value of 10*4 (40) is greater than 14+23 (37), therefore this 
# comparison expression will return the Boolean value of True.


print(10*4 > 14+23) # Should print True

# The letter "t" has a Unicode value of 116 and the letter "s" has a
# Unicode value of 115. Since 116 is not less than 115, the 
# comparison of "tall" < "short" (or 116 < 115) is False. 

print("tall" < "short")  # Should print False
```
    - Crea una función con el `keyword` `def`
    - Para un parámetro a la función
    - Usa una sentencia if-elif-else
    - Asigna strings a variables}
    - Usa operadores condicionales
    - Retorna un valor
```Python
# This function accepts one variable as a parameter
def translate_error_code(error_code):
 
# The if-elif-else block assesses the value of the variable
# passed to the function as a parameter. The if statement uses 
# the equality operator == to test the value of the variable.
# This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
# If the comparison above returns True, then the indented 
# line(s) inside the if-statement will run. In this case, the
# action is to assign a string to the translation variable.
# The remainder of the if-elif-else block will not run.
# The Python interpreter will skip to the next line outside of 
# the if-elif-else block. In this case, the next line is the 
# return value statement.  
        translation = "Server received an unauthenticated request"
 
# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
# If the first elif-statement returns a True result, then the
# indented line(s) inside the first elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Requested web page not found on server"
 
# If both the initial if-statement and the first elif-statement 
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
# If the second elif-statement returns a True result, then the
# indented line(s) inside the second elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Server request to close unused connection"
 
# If the conditional tests above do not produce a True result
# then the else-statement will run. 
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation

# The print() function allows us to display the output of the
# function. To call a function in a print statement, the syntax
# is print(name_of_function(parameter))
print(translate_error_code("404 Not Found"))

# Expected output:
# Requested web page not found on server
```
    - Usa una sentencia if-elif-else con
        - Operadores de comparación
        - Operadores lógicos
```Python
# Sets value of the "number" variable
number = 25

# The "number" variable will first be compared to 5. Since it is 
# False that "number" is not less than or equal to 5, the expression indented 
# under this line will be ignored. 
if number <= 5: 
   print("The number is 5 or smaller.")
 
# Next, the "number" variable will be compared to 33. Since it is 
# False that "number" is equal to 33, the expression indented under 
# this line will be ignored. 
elif number == 33:
   print("The number is 33.")
 
# Then, the "number" variable will be compared to 32 and 6. Since it 
# is True that 25 is less than 32 and greater than 6, the Python 
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder 
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))
 
# Expected output is: 
# The number is less than 32 and greater than 6.
```
    - Usa una sentencia if para retornar el calculo de un valor
    - Usa operadores condicionales
    - Utiliza operadores aritméticos `//` y `%`
```Python
# This function rounds a variable number up to the nearest 10x value
def round_up(number):
  x = 10
# The floor division operator will calculate the integer value of
# "number" divided by x: 35 // 10 will return the integer 3.
  whole_number = number // x
# The modulo operator will calculate the remainder value of "number"
# divided by x: 35 % 10 will return the remainder value 5.
  remainder = number % x
# If the remainder is greater than or equal to 5: 
  if remainder >= 5: 
# Return x multiplied by the (whole_number+1) to round up
    return x*(whole_number+1)
# Else, return x multiplied by the whole_number to round down
  return x*whole_number
 
# Calls the function with the parameter value of 35.
print(round_up(35)) # Should print 40
```