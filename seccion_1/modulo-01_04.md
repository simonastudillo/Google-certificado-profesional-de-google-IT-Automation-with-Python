# Hello World

## Revisión: Hello World!
- Bloques de código para imprimir un "Hello, World!" en Python y en C
```Python
# Python
print("Hello, World!")
```
```C
// C
main () {
    printf("Hello, World!");
}
```

---

## Hello, World!
- Ejemplos
```Python
print("Hello, World!")
```
- print: Es una función que muestra en pantalla lo que le indicamos entre paréntesis.
- Funciones: Son fragmentos de código que realizan una unidad de trabajo.
- Keyworkd (palabra clave): Son palabras reservadas que se utilizan para crear instrucciones
    - if, while, for
- String: Es un tipo de dato que representa texto. Se define entre comillas simples o dobles.

---

## Revisión: Obtener información del usuario
- El siguiente bloque de código muestra como usar variables e mostrarlas en pantalla
```Python
name = "Brook"
print("Hello " + name)
#Hello Brook

name = "Alex"
print("Hello " + name)
#Hello Alex
```

---

## Obtener información del usuario
- En general para que un programa se útil, necesita obtener información del usuario.
- Formas de obtener información
    - Campos de textos
    - Clic en botones
    - Solicitar datos en la terminal
    - Uso de parámetros o variables

---

## Revisión: Python puede ser una calculadora
- Ejemplos de operaciones matemáticas en Python
```Python
print(4+5)
#9
print(9*7)
#63
print(-1/4)
#-0.25
print(1/3)
#0.3333333333333333
print(((2050/5)-32)/9)
#42.0
print(2**10)
#1024
```

---

## Python puede ser una calculadora
- Recuerda usar paréntesis, tal como lo hacemos en matemáticas, para indicar el orden de las operaciones.
- Pyhton se puede usar para obtener cuadrados, cubos o cualquier potencia de un número usando el operador `**`.
- Experimenta para familiarizarte con las operaciones matemáticas en Python.

---

## Guía de estudio: Primeros conceptos de programación
- Functions: Son fragmentos de código que realizan una unidad de trabajo.
    - print(): Muestra en pantalla lo que le indicamos entre paréntesis.
- Keywords: Son palabras reservadas que se utilizan para crear instrucciones
    - Values: True, False, None
    - Conditions: if, elif, else
    - Logical operators: and, or, not
    - Loops: for, in, while, break, continue
    - Functions: def, return  
- Operaciones aritméticas:
    - Suma: `+`
    - Resta: `-`
    - Multiplicación: `*`
    - División: `/`
    - Potenciación: `**`
    - Potenciación con fracciones: `**(1/n)` donde n es el índice de la raíz.
    - División entera: `//`
    - Módulo: `%` (devuelve el residuo de la división)
- Orden de operaciones:
    - Paréntesis: `()`, `{}`, `[]`
    - Exponentes: `**`
    - Multiplicación y división: `*`, `/`, `//`, `%`
    - Suma y resta: `+`, `-`
- Recursos:
    - [Funciones](https://docs.python.org/3/library/functions.html)
    - [Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)
    - [Operadores aritméticos](https://flexiple.com/python/arithmetic-operators-in-python/)

---

## Test your knowledge: Hello World
- What are functions in Python?
R: Functions are pieces of code that perform a unit of work
- What are keywords in Python?
R: Keywords are reserved words that are used to construct instructions.
- What does the print function do in Python?
R: The print function outputs messages to the screen
- Output a message that says "Programming in Python is fun!" to the screen.
```Python
print("Programming in Python is fun!")
```
- Replace the ___ placeholder to calculate the square root of 9. (Tip: to calculate the square root of a number x, you can use x**(1/2).)
```Python
ratio = 9**(1/2)
print(ratio)
```

---

## Editores de código y IDEs
- Las herramientas de codificación pueden ayudarte a desarrollar, escribir, depurar ​y visualizar tu código.
- Con un editor de código, ​puedes escribir, depurar y ejecutar programas en Python
- Los editores de código proporcionan características, incluyendo resaltado de sintaxis, ​indentación automática, comprobación de errores, ​y autocompletado
- Esto permite escribir código de forma más eficiente. ​También facilitan la comprensión de variables, ​comandos, funciones y bucles.
- Un IDE es una herramienta de software que simplifica el proceso ​de creación de una nueva aplicación de software
- Un IDE es una aplicación de software ​que proporciona completas facilidades ​para el desarrollo de software
- IDLE es un IDE que viene con Python automáticamente. ​Es un excelente IDE para principiantes ​porque es muy sencillo de usar

---

## Revisión: Uso de la línea de comandos
- Se usa para decirle a la computadora qué hacer
- Puedes acceder a servidores, mover archivos, cambiar directorios y escribir scripts.
- En MacOS usa `spotlight` para buscar la aplicación Terminal.
    - Escribe en la consola `python --version` o `python3 --version` para verificar la versión de Python.
- En Windows usa `cmd` para buscar la aplicación Command Prompt.
    - Escribe en la consola `python --version` para verificar la versión de Python.
- En Linux usa `Ctrl+Alt+T` para abrir la terminal.
    - Escribe en la consola `python3 --version` para verificar la versión de Python.
- Uso de IDLE: IDLE viene con Python y es un IDE que permite escribir código, depurarlo y ejecutarlo.
- En MacOS, Linux y Windows puedes abrir IDLE desde el menú de aplicaciones.

---

## Usa la línea de comandos
- Para instalar Python en linux usa: 
```bash
sudo apt install python3
```
- Idle es un Entorno de desarrollo integrado y aprendizaje ​para el lenguaje de programación Python.
- Python Idle es un intérprete interactivo, ​o editor de archivos, que le permite ​escribir fácilmente scripts y programas Python. ​Idle proporciona resaltado de sintaxis, completado de código, ​y sangría automática
- ​Para ejecutar el código Python en el archivo que has guardado, haz clic en ejecutar, ​ejecutar módulo desde el menú, o pulsa intro.

--- 

## Revisión: Usa JupyterLab y Jupyter Notebook
- JupyterLab es una interfaz web que permite el uso de Jupyter Notebook, un entorno interactivo para escribir y ejecutar código en Python.
- Jupyter Notebook es una aplicación web que permite crear y compartir documentos que contienen código en vivo, ecuaciones, visualizaciones y texto narrativo.
- Lo puedes descargar desde [JupyterLab](https://jupyter.org/install)
- Como usar Jupyter Notebook:
    - Abre la siguiente [URL](https://jupyter.org/try-jupyter/lab/?path=notebooks%2FIntro.ipynb) en tu navegador web
    - Esto creará un nuevo entorno de Jupyter Notebook en tu navegador web

---

## Usa JupyterLab y Jupyter Notebook
- Jupyter Lab y Jupyter Notebooks ​forman parte de un proyecto de código abierto llamado Project Jupyter ​y son de uso gratuito
- Jupyter Lab proporciona un entorno en línea ​que te permite ejecutar tu código en la nube
- Notebook de Jupyter se puede utilizar en la interfaz basada en web ​a través de Jupyter Lab o en tu máquina local.
- Notebook de Jupyter te permite crear documentos basados en texto ​que contienen bloques de código en vivo
- Puedes escribir programas y scripts de Python ​usando Notebooks de Jupyter ​y ver cómo se ejecutan todo en un mismo lugar
- Para ejecutar el código en en Notebook de Jupyter, haz clic en el bloque de código y presiona `Shift + Enter` o haz clic en el botón de ejecutar en la barra de herramientas.
- Para instalar Jupyter Notebook en tu máquina local, puedes usar el siguiente comando en la terminal:
```bash
pip install notebook
```
- Para instalar Jupyter Lab en tu máquina local, puedes usar el siguiente comando en la terminal:
```bash
pip install jupyterlab
```