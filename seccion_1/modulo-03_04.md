# Repaso de módulo

## Los bucles terminan
- En este módulo, hemos analizado las formas que podemos ​usar para decirle a una computadora que realice una acción de forma repetitiva
- Python nos ofrece tres formas diferentes de ​realizar tareas repetitivas: `for`, `while` y `recursión`.
- Usamos bucles while cuando queremos realizar una operación mientras ​una determinada condición es ​verdadera o, alternativamente, hasta que se convierte en falsa
- Usamos bucles for cuando queremos iterar ​sobre los elementos de una secuencia o un rango de números. 
- Usamos la recursión cuando el problema se resuelve mejor en ​pasos más pequeños y luego ​combinamos esos pasos para lograr una solución mayor.

---

## En palabras de Marga: Cómo me inicié en la programación
- Empecé a programar y a jugar con el ordenador, ​y me emocioné mucho
- Me enseñé a programar en mi tiempo libre.
- Así que siempre seguí ampliando mis horizontes porque me ​apasiona mucho la programación en general.
- Cuando miro hacia atrás en mi carrera, no diría que realmente me enfrenté a ​grandes obstáculos. ​En su mayoría diría que tuve oportunidades de crecimiento.

---

## Glosario de términos de la sección 1, módulo 3
- Break (Break): Una forma de salir de un bucle antes de que su condición sea falsa.
- Control statements (Declaraciones de control): Estructuras de programación que dirigen el flujo de ejecución de un programa, permitiendo tomar decisiones, repetir acciones o elegir entre diferentes rutas de código según condiciones específicas.
- For loop (Bucle for): Ejecuta un bloque de código un número determinado de veces o sobre una colección de elementos.
- Infinite loop (Bucle infinito): Una secuencia que carece de un método para salir del bucle, lo que provoca que este se ejecute indefinidamente.
- Iterators (Iteradores): Variables que permiten recorrer una colección elemento por elemento.
- Loop (Bucle): Una secuencia que hace que la computadora realice tareas repetitivas.
- Programming (Programación): El proceso de escribir un programa para que se comporte de diferentes maneras.
- Pass (Pass): Una instrucción de marcador de posición que se utiliza cuando la sintaxis requiere una instrucción, pero no se desea ejecutar ningún código o comando.
- Recursion (Recursión): La aplicación repetida del mismo procedimiento a un problema más pequeño.
- While loop (Bucle while): Se utiliza cuando un segmento de código necesita ejecutarse repetidamente mientras una condición sea verdadera.

---

## Guía de estudio: Módulo 3 Cuestionario calificado
- Términos clave:
    - variables (variables): Conocer como inicializar o incrementar una variable. Tambien es necesario reconocer un error de codificación en el que se intenta usar una variable antes de inicializarla.
    - inifinite loop (bucle infinito): Saber reconocer un bucle infinito y soluciones comunes para evitarlo. Por ejemplo: revisar condiciones de bucle, rangos, iteradores, declaraciones de control, etc.
    - iterators (iteradores): Conocer la variedad de opciones para iterar sobre una variable. Tambien necesitas nalizar donde la iteración debería ocurrir, una mala iteración puede causar un bucle infinito.
    - control statements (declaraciones de control): Saber como y cuando usar declaraciones de control como break y continue para prevenir bucles infinitos.
- Funciones
    - range(): Saber los roles de los parámetros de la función range() y como se comporta en diferentes escenarios.
        - x: El valor inicial de la secuencia. Si no se proporciona, el valor predeterminado es 0.
        - y: El valor final de la secuencia. La secuencia se detiene antes de este valor.
        - z: El valor de incremento de la secuencia. Si no se proporciona, el valor predeterminado es 1.
    - print(): Sabe que la función inserta una nueva línea al final de la salida, y como usar el parámetro end para cambiar este comportamiento.
        - end: Un parámetro opcional que especifica qué se debe imprimir al final de la salida. El valor predeterminado es una nueva línea ('\n'), pero se puede cambiar a cualquier cadena, como un espacio (' ') o una cadena vacía ('').
- Habilidades de codificación:
    - Usar for loops con la función range()
    - Hacer que el valor final final de un rango sea inclusivo o exclusivo según sea necesario.
```Python
# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
def count_by_10(end):
    # Initialize the "count" variable as a string.
    count = ""

    # The range function parameters instruct Python to start the count  
    # at 0 and stop at the variable given as the upper end of the range. 
    # Since the value of the high end of a range is excluded by default,  
    # you can make Python include the "end" value by adding +1 to it. 
    # The third parameter tells Python to increment the count by 10.
    for number in range(0,end+1,10):

        # Although the variable "count" will hold a count of integers,  
        # this example will be converted to a string using "str(number)" 
        # in order to display the incremental count from 0 to the "end" 
        # value on the same line with a space " " separating each 
        # number.  
        count += str(number) + " "
        
    # The .strip() method will trim the final space " " from the end of 
    # the string "count"  
    return count.strip()


# Call the function with 1 integer parameter.
print(count_by_10(100))
# Should print 0 10 20 30 40 50 60 70 80 90 100
```
    - Usar for loops anidados con un rango para crear una matriz de 2 dimensiones.
    - Incluir el rango superior en la función rang() usando end+1.
```Python
# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names. 
    n1 = initial_number 
    n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the rows.
    for row in range(n1, n2):

        # The nested for loop will create the columns.
        for column in range(n1, n2):

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the 
            # end of the row. You can override the default behavior of the 
            # print() function (which inserts a new line character after 
            # the print command runs) by using the "end=" "" parameter 
            # inside the print() function.  
              print(column * row, end=" ")

        # The row ends when the inner loop (the columns) is finished.
        # The outer (row) for loop should insert a new line
        # to create the next row. Use the print() function new line default 
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters. 
matrix(1, 4)
# Should print:
# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16 
```
    - Predecir el valor final de un bucle for anidado con un rango.
```Python
# For this example, the outer for loop uses an end of range index of 
# 10. The value of index 10 will be 10-1, or 9.  
for outer_loop in range(10):

    # Using the "outer_loop" variable as the end of range for the  
    # inner loop, means the end of range index will be 9. The value 
    # of index 9 will be 9-1, or 8.
    for inner_loop in range(outer_loop):

        # The printed result is the value of "inner_loop". Since  
        # there aren’t any calculations in this loop, there is a 
        # simple shortcut for solving what the final value printed 
        # by the "inner_loop" will be. The solution is to simply use 
        # the value of the "inner_loop" index, which is 8.
        print(inner_loop)
```
    - Encontrar y corregir un error in un for loop con range()
```Python
# This function should count down by -2 from 11 to 1, so that it only
# prints odd numbers. 

# This range(11, -2) tells the for loop to start at 11 and end at index
# position -2 (which corresponds to the numeric value of -1). Since the
# third incremental or decremental value is missing, the loop will 
# increment by the default of +1 instead of the intended -2 decrement.
# Starting at index position 11 and incrementing by +1 will end the loop 
# automatically, because the index is not counting down towards -2 as 
# the end of the range. 

# To fix this problem, the range() needs three parameters:
# First parameter should be the starting index position of 11.
# Second parameter should be the ending index position of 0 (value 1).
# Third parameter should be decrementing by -2.
# So, the range should be configured as range(11, 0, -2).

# Fix this loop with the corrected range parameters and click Run.
for n in range(11, -2):
    if n % 2 != 0:
        print(n, end=" ")

# Should print: 11, 9, 7, 5, 3, 1 once the problem is fixed.
```
    - Usa un while loop para imprimir una secuencia de números
```Python
# For this example, the while loop will count down by threes starting 
# from 18 and ending at 0.
starting_number = 18

# The while loop will continue to loop until it reaches 0.
while starting_number >= 0:

    # To make the sequence of numbers easier to read, include a space
    # between each number in the sequence. You can override the default 
    # behavior of the print() function by using the "end=" parameter with
    # the print() function. The syntax for adding a space is: end=" " 
    print(starting_number, end=" ")
    
    # Decrement the "starting_number" variable by -3.
    starting_number -= 3

# Should print 18 15 12 9 6 3 0 
```
    - Usa un while loop para contar la cantidad de dígitos de un valor numérico
```Python
# This function accepts a CEO's salary as a variable. 
# It counts the number of digits in the salary and 
# returns the sentence like:
# "The CEO has a 6-figure salary."
def X_figure(salary):
    
    # Initializes the counter as an integer.
    tally = 0

    # The if-statement checks if the variable "salary" 
    # is equal to 0.
    if salary == 0:
        # If true, then it increments the counter to 
        # show there is 1 digit in 0.
        tally += 1

    # The while loop starts to run while the "salary"
    # is greater than or equal to 1 (the loop will 
    # not run if the "salary" is 0).
    while salary >= 1:

        # The body of the while loop counts the digits 
        # in "salary" by counting the number of times 
        # "salary" can be divided by 10 until "salary" 
        # is no longer >= 1.
        salary = salary/10

        # Add 1 to the counter to tally the number of 
        # times the loop runs.
        tally += 1

    # Return the results of the "tally" of the number
    # of digits in "salary".
    return tally
 
# Call the X_figure function with 1 parameter, converted to a string,
# inside a print function with additional strings.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")

# Should print"The CEO has a 7-figure salary."
```
    - Usar una función que acepte 2 variables de tipo integer
    - Usar un if-else anidado y un while loop para contar hacia arriba o hacia abajo desde la primera variable hasta la segunda variable.
```Python
# This function will accept two integer variables: the floor
# number that a passenger "enter"s an elevator and the floor
# number the passenger is going to "exit". Then, the function
# counts up or down from the two floor numbers.
def elevator_floor(enter, exit):
    # The "floor" variable will be used as a counter and to  
    # print the floor numbers. The "elevator_direction"
    # variable will hold the string "Going up: " or 
    # "Going down: " plus the count up or down of the 
    # "floor" numbers.
    floor = enter
    elevator_direction = ""

    # If the passenger enters the elevator on a floor that  
    # is higher than the destination floor:
    if enter > exit:
        
        # Then the "elevator_direction" string will be 
        # initialized with the string "Going down: ".
        elevator_direction = "Going down: "

        # While the "floor" number is greater than or  
        # equal to the exit floor number:
        while floor >= exit:
            # The "floor" number is converted to a string 
            # and is appended to the string variable 
            # "elevator_direction".
            elevator_direction += str(floor)

            # If the "floor" number is still greater than  
            # the exit floor number:
            if floor > exit:

                # A pipe | character is added between each  
                # floor number in the string variable  
                # "elevator_direction" to provide a visual  
                # divider between numbers. The if-statement 
                # above (if floor > exit) prevents the pipe 
                # character from appearing after the "floor" 
                # number is no longer greater than the "exit" 
                # variable. 
                elevator_direction += " | "
                
                # Decrement the "floor" number as the elevator 
                # goes down.
            floor -= 1

    # Else, it is implied that the passenger is entering the  
    # elevator on a floor that is lower than the destination 
    # floor.
    else:

        # The "elevator_direction" string will be initialized 
        # with the string "Going up: ".
        elevator_direction = "Going up: "
        
        # While the "floor" number is less than or equal to the 
        # "exit" floor number:
        while floor <= exit:

            # Convert the "floor" number to a string and append 
            # it to the string variable "elevator_direction".
            elevator_direction += str(floor)

            # If the entry floor number is still less than the exit 
            # floor number:
            if floor < exit:

                # The pipe | character is added between each  
                # floor number in the string variable  
                # "elevator_direction" to provide a visual  
                # divider between numbers. The if-statement 
                # above (if floor < exit) prevents the pipe 
                # character from appearing after the "floor" 
                # number is no longer less than the "exit" 
                # variable. 
                elevator_direction += " | "

            # Increments the "floor" number as the elevator goes up.
            floor += 1

    # Returns the string holding the elevator direction (Going down or 
    # Going up) along with the floor countdown or count up.
    return elevator_direction


# Call the function with 2 integer parameters. 
print(elevator_floor(1,4)) # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Should print Going down: 6 | 5 | 4 | 3 | 2
```

>[!NOTE]
> Recuerda: La sintaxis correcta es crítica

---

## Modulo 3: Cuestionario calificado
1. Fill in the blanks to print the numbers 1 through 7.
```Python
number = 1 # Initialize the variable
while number < 8: # Complete the while loop condition
    print(number, end=" ")
    number = number + 1 # Increment the variable

# Should print 1 2 3 4 5 6 7 
```

1.2 Fill in the blanks to print the numbers from 15 to 5, counting down by fives.
```Python
number = 15 # Initialize the variable
while number > 0: # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Increment the variable

# Should print 15 10 5 
```

2. Find and correct the error in the for loop below.  The loop should print every even number from 2 to 12.
```Python
for number in range(2,13,2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12
```

2.2 Find and correct the error in the for loop.  The loop should print every number from 5 to 0 in descending order.
```Python
for number in range(5,-1, -1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1
# 0
```

3. Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many even numbers exist in a sequence from 0 to the given “n”number, where 0 counts as an even number.  For example, even_numbers(25) should return 13, and even_numbers(6) should return 4.
```Python
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n: # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1 # Increment the appropriate variable
        current_number = current_number + 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1
```

4. Fill in the blanks to complete the “sequence” function. This function should print a sequence of numbers in descending order, from the given "high" variable to the given "low" variable.  The range should make the loop run two times. Complete the range sequences in the nested loops so that the “sequence(1, 3)” function call prints the following:

3, 2, 1

3, 2, 1
```Python
def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low - 1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.
```

4.2 Fill in the blanks to complete the “rows_asterisks” function. This function should print rows of asterisks (*), where the number of rows is equal to the “rows” variable. The number of asterisks per row should correspond to the row number (row 1 should have 1 asterisk, row 2 should have 2 asterisks, etc.). Complete the code so that “row_asterisks(5)” will print:
*
* * 
* * *
* * * *
* * * * *
```Python
def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1, rows + 1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above
```

5. Fill in the blanks to complete the “countdown” function. This function should begin at the “start” variable, which is an integer that is passed to the function,  and count down to 0. Complete the code so that a function call like “countdown(2)” will return the numbers “2,1,0”.
```Python
def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1 # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)) # Should be "Cannot count down to 0"
```

6. Fill in the blanks to complete the “even_numbers” function. This function should return a space-separated string of all positive even numbers, excluding 0, up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “even_numbers(6)” will return the numbers “2 4 6”.  
```Python
def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for i in range(2, maximum + 1, 2): 

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string += str(i) + " "

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
```

7. What happens when the Python interpreter executes a loop where a variable used inside the loop is not initialized?
> Will produce a NameError stating the variable is not defined

7.2 The following code is supposed to add together all numbers from x to 10.  The code is returning an incorrect answer, what is the reason for this?
```Python
x = 1
sum = 5
while x <= 10:
    sum += x
    x += 1
print(sum)
# Should print 55
# The "sum" variable is initialized with the wrong value
```

8. How many numbers will this loop print?  Your answer should be only one number.
```Python
for sum in range(5):
    sum += sum
    print(sum)
# Should print 5 numbers
```

9. What is the final value of "y" at the end of the following nested loop code? Your answer should be only one number.
```Python
for x in range(10):
    for y in range(x):
        print(y)
# Should print 8
```

10. The following code causes an infinite loop. Can you figure out what is incorrect?
```Python
def test_code(num):
  x = num
  while x % 2 == 0:
    x = x / 2

test_code(0)
# When called with 0, it triggers an infinite loop
```

10.2 The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?
```Python
def count_numbers(first, last):
  # Loop through the numbers from first to last 
  x = first
  while x <= last:
    print(x)


count_numbers(2, 6) 
# Should print:
# 2
# 3
# 4 
# 5
# 6
```
> Variable x is not incremented