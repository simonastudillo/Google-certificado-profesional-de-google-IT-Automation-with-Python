# Revisión del módulo

## Resumen del Módulo 4: Gestión de datos y procesos
- hemos aprendido un montón de maneras diferentes en las que ​podemos proporcionar información a nuestros scripts, como leer desde la entrada estándar ​, las variables de entorno y los argumentos de la línea de comandos

---

## Glosario de terminos
- `Bash` (Bash): El intérprete de comandos más utilizado en Linux.
- `Command line arguments` (Argumentos de línea de comandos): Entradas que se proporcionan a un programa al ejecutarlo desde la línea de comandos.
- `Environment variables` (Variables de entorno): Configuraciones y datos almacenados fuera de un programa al que este puede acceder para modificar su comportamiento en un entorno determinado.
- `Input/Output (I/O)` (Entrada/Salida, E/S): Estos flujos son el mecanismo básico para realizar operaciones de entrada y salida en los programas.
- `Log files` (Archivos de registro): Los archivos de registro son registros o archivos de texto que almacenan un historial de eventos, acciones o errores generados por un sistema informático, software o aplicación con fines de diagnóstico, resolución de problemas o auditoría.
- `Standard input (STDIN)` (Flujo de entrada estándar): Un canal entre un programa y una fuente de entrada.
- `Standard output (STDOUT)` (Flujo de salida estándar): Una vía entre un programa y un destino de salida, como una pantalla.
- `Standard error (STDERR)` (Error estándar): Muestra la salida como la salida estándar, pero se utiliza específicamente como un canal para mostrar mensajes de error y diagnósticos del programa.
- `Command-line interpreter (Shell)` (Instrumento de línea de comandos): La aplicación que lee y ejecuta todos los comandos.
- `Subprocesses` (Subprocesos): Un proceso que llama y ejecuta otras aplicaciones desde Python, incluidos otros scripts de Python.

---

## Qwiklabs assessment: Work with log files
- Imagina que uno de tus compañeros tiene problemas con un programa que no deja de dar errores. Por desgracia, el código fuente es demasiado complejo como para encontrar el error fácilmente. ¡Pero la buena noticia es que el programa genera un archivo de registro que puedes leer! Vamos a escribir un script para buscar el error exacto en el archivo de registro y guardarlo en otro archivo para que puedas averiguar cuál es el problema.
```Python
#!/usr/bin/env python3


import sys
import os
import re

def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

    
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
```
```bash
sudo chmod +x find_error.py
./find_error.py ~/data/fishy.log
# CRON ERROR Failed to start
cat ~/data/errors_found.log
```

Find an error
In this lab, we'll search for the CRON error that failed to start. To do this, we'll use a python script to search log files for a particular type of ERROR log. In this case, we'll search for a CRON error within the fishy.log file that failed to start by narrowing our search to "CRON ERROR Failed to start".

To get started, let's create a python script named find_error.py within scripts directory using nano editor.

```bash
cd ~/scripts
```
```bash
nano find_error.py
```

Add the shebang line:

```python
#!/usr/bin/env python3
```
Import the necessary Python modules:

```python
import sys
import os
import re
```
The sys module provides information about the Python interpreter's constants, functions, and methods. The os module provides a portable way of using operating system dependent functionality with Python.

Regular Expression (RegEx) is a sequence of characters that defines a search pattern. We can use regular expressions using re module.

Now, write a function error_search that takes log_file as a parameter and returns returned_errors. Define the error_search function and pass the log file to it as a parameter.

```python
def error_search(log_file):
```
To allow us to search all log files for any type of logs, we'll be making our script consistent and dynamic.

Define an input function to receive the type of ERROR that the end-user would like to search and assign to a variable named error.

The input() function takes the input from the user and then evaluates the expression. This means Python automatically identifies whether the user entered a string, a number, or a list. If the input provided isn't correct then Python will raise either a syntax error or exception. The program flow will stop until the user has given an input.

Later in the script, we'll iterate over this user input and the log file to produce results. Following the input function, now initialize the list returned_errors. This will enlist all the ERROR logs as specified by the end-user through the input function.

```python
  error = input("What is the error? ")
  returned_errors = []
```
Use the Python file's handling methods to open the log file in reading mode and use 'UTF-8' encoding.

```python
  with open(log_file, mode='r',encoding='UTF-8') as file:
```
We'll now read each log separately from the fishy.log file using the readlines() method. As mentioned earlier, we'll iterate over user input to get the desired search results. For this, we'll create a list to store all the patterns (user input) that will be searched. This list is named error_patterns and, initially it has a pattern "error" to filter out all the ERROR logs only. You can change this to view other types of logs such as INFO and WARN. You can also empty initialize the list to fetch all types of logs, irrespective of their type.

We'll add the whole user input to this list error_patterns.

```python
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
```
Now, let's use the search() method (present in re module) to check whether the file fishy.log has the user defined pattern and, if it is available, append them to the list returned_errors.

```python
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
```
Next, close the file fishy.log and return the results stored in the list returned_errors.

```python
    file.close()
  return returned_errors
```
Great job! You've successfully defined a function to store all the logs defined as a CRON error that fails to start. In the next section, we'll generate a new file consisting of the logs based on your search within /data directory.

Create an output file
Let's define another function file_output that takes returned_errors, returned by a previous function, as a formal parameter.

```python
def file_output(returned_errors):
```
Using Python file handling methods, write returned_errors into the errors_found.log file by opening the file in writing mode. For defining the output file, we'll use the method os.path.expanduser ('~'), which returns the home directory of your system instance. Then, we'll concatenate this path (to the home directory) to the file errors_found.log in /data directory.

```python
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
```
Next, write all the logs to the output file by iterating over returned_errors.

```python
    for error in returned_errors:
      file.write(error)
```
And finally, close the file.

```python
    file.close()
```
Function call
Now, let's call the functions and run the script.

Define the main function and call both functions that we defined in the earlier sections.

The variable log_file takes in the path to the log file passed as a parameter. In our case, the file is fishy.log. Call the first function i.e., error_search() and pass the variable log_file to the function. This function will search and return a list of errors that would be stored in the variable returned_errors. Call the second function file_output and pass the variable returned_errors as a parameter.

sys.exit(0) is used to exit from Python, the optional argument passed can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered "successful termination" and any nonzero value is considered an "abnormal termination" by shells.
```