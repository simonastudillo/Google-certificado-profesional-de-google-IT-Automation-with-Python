# Reseña de módulo

## En palabras de Marga: Por qué me gusta Python
- Tenemos un script que mantiene el ordenador actualizado, ​que el software se actualiza todos los días y que está escrito en Python.
- También tenemos un script que comprueba que la computadora no tiene ningún ​problema específico y, si hay algún problema, lanza una alerta para ​que el usuario pueda tomar medidas
- Una de las cosas que más me gustan de Python es que el código es realmente ​legible. 
- Ningún lenguaje de programación es perfecto, cada lenguaje de programación tiene sus ventajas y ​desventajas
- Si escribes pruebas y luego la prueba puede probar todo el código, incluso si ​no se ejecuta todos los días

---

## Términos del glosario del curso 1, módulo 2
- Built-in functions (Funciones integradas): Funciones que existen en Python y que se pueden llamar directamente.
- Comments (Comentarios): Notas para uno mismo o para otros programadores que aclaran el propósito del código.
- Data types (Tipos de datos): Clases de datos (p. ej., cadena, entero, flotante, booleano, etc.), que incluyen las propiedades y el comportamiento de las instancias del tipo de dato (variables).
- Explicit conversion (Conversión explícita): Ocurre cuando se escribe código para convertir manualmente un tipo de dato a otro mediante una función de conversión de tipos de datos.
- Expression (Expresión): Una combinación de números, símbolos u otros valores que produce un resultado al evaluarse.
- Implicit conversion (Conversión implícita): Ocurre cuando el intérprete de Python convierte automáticamente un tipo de dato a otro.
- Logical operators (Operadores lógicos): Operadores que se utilizan para combinar o manipular valores booleanos (Verdadero o Falso) para crear condiciones complejas para la toma de decisiones.
- Parameter (argumento): Valor que se pasa a una función para su uso dentro de ella, controlando el comportamiento del lector y escritor de CSV.
- Refactoring (Refactorización): Proceso de actualización de código para que sea más autoexplicativo y aclare su propósito.
- Return value (Valor de retorno): Valor o variable que devuelve la función como resultado final.

---

## Guía de estudio: Cuestionario calificado del módulo 2
- Conocimientos:
    - Cómo asignar valores a variables y usarlas en el código
    - Cómo construir una función y usar sus parámetros
    - Cómo se pueden usar los operadores de comparación y lógicos
    - Cómo se comportan los operadores de comparación y lógicos con diferentes tipos de datos
    - Qué tipo de resultados producen las comparaciones simples y complejas
    - Cómo ordenar alfabéticamente las cadenas usando operadores de comparación
    - Qué debe aparecer después de las palabras clave `if` y `elif`
    - Qué hace la palabra clave `elif`
    - Cuándo se ejecuta una sentencia `if`, `elif` o `else`
    - Cómo usar los operadores de división entera (`/`) y módulo (`%`), y por qué
    - Cómo usar operadores lógicos con operadores de comparación para desarrollar sentencias condicionales complejas dentro de un bloque `if-elif-else`
    - Mejores prácticas de programación y sus beneficios
    - Qué significa "código autodocumentado"

>[!NOTE]
> Recuerda: Una sintaxis correcta es crítica.

- Utilizar una sintaxis precisa es fundamental al escribir código en cualquier lenguaje de programación.
- Incluso un pequeño error tipográfico puede provocar un error de sintaxis.
- Esto refleja los errores de programación reales, ya que un solo error de ortografía, mayúsculas/minúsculas, puntuación, etc., puede hacer que tu código falle.
- Los problemas de codificación causados ​​por una sintaxis imprecisa siempre serán un inconveniente, tanto si estás aprendiendo un lenguaje de programación como si utilizas tus habilidades de programación en el trabajo.

---

## Module 2 challenge: Basic Python Syntax Assessment
1. Complete the code to output the statement, “Marjery lives at her home address of 1234 Mockingbird Lane”. Remember that precise syntax must be used to receive credit.
```Python
name = "Marjery"
home_address = "1234 Mockingbird Lane"
print(name + " lives at her home address of " + home_address)
# Should print "Marjery lives at her home address of 1234 Mockingbird Lane"
```

2. What’s the value of this Python expression: 7 < "number"?
> TypeError

3. What is the elif keyword used for?
> To handle more than two comparison cases

4. Consider the following scenario about using if-elif-else statements:

The fall weather is unpredictable.  If the temperature is 32 degrees Fahrenheit or below, a heavy coat should be worn.  If it is above 32 degrees but not above 50 degrees, then a jacket should be sufficient.  If it is above 50 but not above 65 degrees, a sweatshirt is appropriate, and above 65 degrees a t-shirt can be worn.  

Fill in the blanks in the function below so it returns the proper clothing type for the temperature.
```Python
def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50:
        clothing = "Sweatshirt"
    elif temp > 32:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat
```

5. When using an if statement, the code inside the if block will only execute if the conditional statement returns what?
> True

6. Fill in the blanks to complete the function.  The character translator function receives a single lowercase letter, then prints the numeric location of the letter in the English alphabet.  For example, “a” would return 1 and “b” would return 2. Currently, this function only supports the letters “a”, “b”, “c”, and “d” It returns "unknown" for all other letters or if the letter is uppercase.
```Python
def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown
```

7. Can you calculate the output of this code?
```Python
def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))
```
> 15

8. What's the value of this Python expression?
```Python
x = 5*2
((10 != x) or (10 > x))
```
> False

9. Fill in the blanks to complete the function. The “return_nonnegative” function takes in two numbers and determines which number is larger.  Then, it subtracts the smaller number from the larger and returns the result. The result will always be greater than or equal to 0. Complete the body of the function so that it returns the correct result.
```Python
def return_nonnegative(first_num, second_num):
    if first_num > second_num:
        result = first_num - second_num
    else:
        result = second_num - first_num
    return result


print(return_nonnegative(5, 5)) # Should print 0
print(return_nonnegative(4, 5)) # Should print 1
print(return_nonnegative(5, 3)) # Should print 2
print(return_nonnegative(2, 5)) # Should print 3
print(return_nonnegative(5, 0)) # Should print 5
print(return_nonnegative(0, 5)) # Should print 5
```

10. Code that is written so that it is readable and doesn’t conceal its intent is called what?
> Self-documenting code

---

## Resumen de la sintaxis básica
- Diferentes tipos de datos: cadena, entero, flotante, booleano
- Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Operadores lógicos: `and`, `or`, `not`
- Sentencias condicionales: `if`, `elif`, `else`
