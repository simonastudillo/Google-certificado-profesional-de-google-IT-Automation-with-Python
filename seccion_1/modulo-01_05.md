# Revisión del módulo

## Resumen de los Primeros Pasos
- Haz descubierto que son las secuencias de comandos
- En que consisten la sintaxis y la semántica
- Como se relacionan con la automatización de tareas
- Aprendido pequeños bloques de código y su ejecución
- Como Python funciona las operaciones básicas matematicas y lógicas

---

## Conoce a Marga, la desarrolladora de currículos
- Es muy importante que ​todos puedan aprender a decirle al ordenador lo que tiene que hacer
>  ​Si hubiera sido solo yo, ​no habría sido posible
- Es muy importante incorporar ​muchos puntos de vista diferentes

---

## Términos del glosario de la sección 1, módulo 1
- Automation (Automatización): Proceso de sustitución de un paso manual por otro que se realiza automáticamente
- Client-side scripting language (Lenguaje de scripting del lado del cliente): Principalmente para programación web; los scripts se transfieren desde un servidor web al navegador del usuario final y luego se ejecutan en el navegador
- Code editors (Editores de código): Herramientas que proporcionan funciones, incluyendo resaltado de sintaxis, sangría automática, verificación de errores y autocompletado
- Computer program (Programa informático): Una lista de instrucciones paso a paso que una computadora sigue para alcanzar un objetivo previsto
- Functions (Funciones): Un bloque de código reutilizable que realiza una tarea específica
- IDE (Entorno de desarrollo integrado): Una aplicación de software que proporciona instalaciones completas para el desarrollo de software
- Interpreter (Intérprete): El programa que lee y ejecuta el código
- Input (Entrada): Información que se proporciona a un programa por el usuario final
- Logic errors (Errores lógicos): Errores en el código que impiden que se ejecute correctamente
- Machine language (Lenguaje de máquina): Lenguaje de computadora de nivel más bajo. Se comunica directamente con las máquinas informáticas en código binario (unos y ceros)
- Object-oriented programming language (Lenguaje de programación orientado a objetos): La mayoría de los elementos de codificación se consideran objetos con propiedades configurables
- Output (Salida): El resultado final de una tarea realizada por una función o programa informático
- Platform-specific scripting language (Lenguaje de scripting específico de la plataforma): Lenguaje utilizado por los administradores del sistema en esas plataformas específicas
- Programming (Programación): El proceso de escribir un programa para que se comporte de diferentes maneras
- Programming code (Código de programación): Conjunto de instrucciones informáticas escritas, guiadas por reglas, que utilizan un lenguaje de programación informática
- Programming languages (Lenguajes de programación): Lenguaje con sintaxis y semántica para escribir programas informáticos
- Python (Python): Un lenguaje de programación de propósito general
- Python interpreter (Intérprete de Python): Programa que lee y ejecuta código Python traduciendo el código Python en instrucciones informáticas
- Script (Script): A menudo se utiliza para automatizar tareas específicas
- Semantics (Semántica): Significado o efecto que se pretende dar a las frases o conjuntos de palabras, tanto en el lenguaje humano como en el informático
- Syntax (Sintaxis): Las reglas que rigen la construcción de los enunciados, tanto en el lenguaje humano como en el informático
- Variables (Variables): Se utilizan para almacenar temporalmente valores cambiantes en el código de programación

---

## Guía de estudio: Quiz calificado del Módulo 1
- Conocimientos
    - Beneficios del lenguaje de programción Python
    - Cómo es Python comparado con otros lenguajes de programación
    - Cómo el conocimiento de un lenguaje de programación puede ayudar a aprender otros lenguajes
    - Cómo los scripts pueden ayudar a automatizar tareas
    - Sintaxis correcta para operaciones aritméticas y lógicas en Python
    - Funciones y Keywords de Python usados para mostrar información en la pantalla
    - Por qué la precisión es importante en la programación
- Terminos
    - Programas informáticos
    - Lenguajes de programación
    - Sintaxis
    - Semántica
    - Errores lógicos
    - Script
    - Automatización
    - Funciones
- Habilidades de codificación
    - Usa la función `print()`para mostrar un `string`
```Python
# Syntax for printing a string of text
print("I love Python!")

# Syntax for printing numeric values
print(360)
print(32*45)

# Syntax for printing the value of a variable
value = 8*6
print(value)
```
    - Usa operadores aritméticos, enfocado en exponentes
```Python
# Multiplication, division, addition, and subtraction
print(3*8/2+5-1)
 
# Exponents
print(4**6) # Syntax means 4 to the power of 6
print(4**2) # To square a number
print(4**3) # To cube a number
print(4**0.5) # To find the square root of a number

# To calculate how many different possible combinations can be
# formed using a set of "x" characters with each character in "x"
# having "y" number of possible values, you will need to use an 
# exponent for the calculation:
x = 4
y = 26
print(y**x)
``` 
    - Uso de variables con valores asignados y operaciones aritméticas
```Python
# Assignment of values to the variables:
years = 10
weeks_in_a_year = 52
# This variable is assigned an arithmetic calculation:
weeks_in_a_decade = years * weeks_in_a_year
# Prints the calculation stored in the "weeks_in_a_decade" variable:
print(weeks_in_a_decade)
``` 

>[!NOTE]
> Recuerda: El uso correcto de la sintaxis es critico.

- Incluso un pequeño error tipográfico puede causar un error de sintaxis y el corrector automático de cuestionarios codificado en Python marcará tu código como incorrecto
- Problemas de codificación causados por sintaxis incorrecta son normales mientras aprendes a programar.
- Por eso es importante comenzar el habito de ser preciso y exacto con la sintaxis desde el principio.
- Errores comunes de sintaxis
    - Identación incorrecta
    - Olvidar o usar un caracter incorrecto en una palabra clave
        - Llaves `{}`, paréntesis `()`, corchetes `[]`, comillas `'` o `"`
        - Caracteres de introdocción a un bloque de código como `:` o `;`
    - Difertes tipos de datos
    - Olvidar, usar incorrecto o mal usar palabras reservadas
    - Usar el `case`incorrecto, Python es case-sensitive, lo que significa que `Variable` y `variable` son diferentes.

---

## Module 1 challenge: Hello Python!
- Why is it important to be very precise about what a computer program is supposed to do?
    - Computers do exactly what they are told.
- Which of the following are true about programming languages? Select all that apply.
    - Some common programming languages include Python, Java, C, C++, C#, and R.
    - Programming languages are used to write computer programs and scripts.
    - Similar to human language, programming languages use syntax and semantics.
- What are some tasks that might be a good fit for full automation? Select all that apply.
    - Detecting and removing duplicate data
    - Updating specific files on multiple computers
- What is the term for the set of rules for how statements are constructed in a programming language?
    - Syntax
- What is a property of Python that makes it easier to understand than some other programming languages?
    - Code is similar to the English language.
- Write a Python script that outputs "Automating with Python is fun!" to the screen. Remember that syntax precision is important in programming languages. A missing capital letter, spelling error, or punctuation mark can produce errors.
```Python
print("Automating with Python is fun!")
```
- What should be the output of the expression below? 
    - 8
- Assuming there are 60 minutes in an hour, write a program that calculates the number of minutes in a 24 hour day. Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.
```Python
# Enter code here:
hours:int = 24
minutes_per_hour:int = 60
print(hours*minutes_per_hour)
# Should print 1440
```
- The market is six miles away from your home. The school is two miles away from your home. Use Python to calculate how much further the market is from your home than the school (in miles). Note: Your result should be in the format of a number, not a sentence.
```Python
# Should print 4
market_distance:int = 6
school_distance:int = 2
print(market_distance-school_distance)
```
- Fill in the blank to calculate how many sectors a given 16 GB (gigabyte) hard disk drive has. The given hard drive is divided into sectors of 512 bytes each. Divide the total bytes on the drive by the number of bytes in a sector to calculate how many sectors this drive has.  Your result should be a number. Note: To calculate the total bytes on the disk drive, multiply by multiples of 1024. In the code below,  you can calculate the "disk_size" of 16 GB by multiplying 16 by 1024 three times to go from bytes, to kilobytes, to megabytes, and finally to gigabytes.
```Python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount) # Should print 33554432.0
```
- Once you have learned the basics of a programming language, how does this affect your ability to learn and use a second programming language?"
    - It’s easier to learn and use a second language.
- What is automation?
    - The process of replacing a manual step with an automated step
- Which of the following are characteristics of the Python language? Select all that apply.
    - Python is cross-platform compatible
    - Python is used in a wide variety of applications
- Complete the code so that the string "I am writing Python code!" will print to the screen. Remember that syntax precision is important in programming languages. A missing capital letter, spelling error, or punctuation mark can produce errors.
```Python
# Replace the blanks with the correct code and syntax:
print("I am writing Python code!")

# Should print: I am writing Python code!
```
- What should be the output of the expression below? 
```Python
print((9-3)/(2*(1+2)))
# 1.0
```
- Keeping in mind there are 60 seconds per minute , write a program that calculates how many seconds there are in an hour .Print the result to the screen. Note: Your result should be in the format of just a number, not a sentence.
```Python
# Enter code here:
seconds_per_minute:int = 60
minutes_per_hour:int = 60
print(seconds_per_minute*minutes_per_hour)
# Should print 3600
```
- What is the program that reads and executes Python code by translating it to computer instructions called?
    - Interpreter
- In one year, if there are 365 days, with 24 hours in a day, , write a program to calculate the number of hours in a year. Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.
```Python
# Enter code here:
days_per_year:int = 365
hours_per_day:int = 24
print(days_per_year*hours_per_day)
# Should print 8760
```
- Consider this scenario about using Python to make calculations:
In a managed computing environment, there are 200 remote computers that must download 200 MB (megabytes) of updates each month. There are 1024 KB (kilobytes) in each MB.
Fill in the blank in the code below to compute the number of total kilobytes downloaded by all computers from the remote update server each month. Multiply the total number of computers by the download size in KB to calculate. 
```Python
download_size_kb = 200*1024
total_computers = 200
total_kbs = download_size_kb * total_computers

print(total_kbs) # Should print 40960000.0
```