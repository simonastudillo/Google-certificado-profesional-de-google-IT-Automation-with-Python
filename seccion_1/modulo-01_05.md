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