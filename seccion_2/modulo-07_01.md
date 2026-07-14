# Prepararse para el proyecto final

## Introducción a su proyecto final
- Hemos aprendido acerca de administrar archivos y directorios, ​leer y escribir archivos de texto y archivos ​CSV usando expresiones regulares, ​entender cómo interactúa el sistema con nuestros programas, ​ejecutar comandos del sistema ​y escribir pruebas automatizadas por nombrar algunos
- Tambien hemos aprendido a usar bash

---

## Escribir un script desde cero
- El primer paso para manejar ​cualquier proyecto de codificación es ​comprender completamente la declaración del problema
- Esto incluye; deletrear lo que hay ​que hacer e identificar cuáles ​son las entradas dadas y las salidas deseadas para ese programa que necesitamos escribir
- Luego se recomienda hacer algunas investigaciones
- Esto significa descrubir cómo podemos abordar el problemas con las herramientas proporcionadas por la biblioteca estándar de Python y otras bibliotecas de terceros
- Queremos evitar reinventar la rueda
- La investigación incluye buscar la documentación de módulos, clases y funciones que necesitamos usar y crear, ver ejemplos de la documentación.
- En tercer lugar, debemos planificar
- Esto significa pensar en qué ​tipos de datos son útiles para nuestra solución, ​el orden de operaciones que necesitamos realizar ​y cómo todas las piezas se han ​unido para formar nuestra solución
- Por último, debemos escribir el código y probarlo
- Este paso incluye escribir el código, hacer pruebas manuales y automatizadas, depurar el código y refactorizarlo para mejorar la legibilidad y la eficiencia
- Dentro de lo posible, debemos tambien agregar documentación y comentarios para que otros puedan entender nuestro código

---

## Planteamiento del problema del proyecto
- uno de ​los servidores utilizados por su empresa ​ejecuta un servicio llamado ticky
- Este servicio es un sistema interno de ticketing utilizado por ​muchos equipos diferentes de ​la empresa para gestionar su trabajo
- El servicio registra un montón de eventos en syslog, ​tanto cuando se ejecuta correctamente como ​cuando encuentra errores
- Los desarrolladores del servicio están pidiendo ​su ayuda para obtener ​información de esos registros, ​para comprender mejor cómo se está ​utilizando el software y cómo mejorarlo
- Las líneas de registro siguen un patrón similar a esto
```bash
May 27 11:45:40 ubutu.local ticky: INFO: Created ticket [#1234] (username)
Jun 1 11:06:48 ubutu.local ticky: ERROR: Connection to DB failed (username)
```
- Cuando el servicio se ejecuta correctamente, ​registra un mensaje de información en syslog, ​indicando lo que ha hecho, ​el nombre de usuario y el número de ticket relacionado con el evento
- Si el servicio encuentra un problema, ​inicia sesión en el mensaje de error en el syslog, ​indicando qué estaba mal y el ​nombre de usuario que desencadenó la acción ​que causó el problema.
- Se necesitan 2 reportes:

1. una clasificación ​de errores generados por el sistema: una lista de todos los mensajes de error registrados ​y cuántas veces se encontró cada uno de ellos, ​sin tener en cuenta los usuarios involucrados, deben ordenarse por el error más común ​al error menos común
2. una estadística de uso para el servicio: Esto significa, una lista de todos los usuarios que han utilizado el sistema ​, incluyendo cuántos mensajes de información y ​cuántos mensajes de error han generado, este informe debe ordenarse por nombre de usuario.

- Para visualizar los datos de estos informes, ​desea generar un par de páginas web que ​serán servidas por un servidor web que se ejecute en el equipo. ​Para hacer esto, puede hacer uso de un script que ​ya está en el sistema llamado csv_ to_html.py
- Este script convierte los datos de un archivo CSV ​en un archivo HTML que contiene una tabla con los datos
- A continuación, coloque los archivos en el directorio ​que utiliza el servidor web para mostrar las páginas web
- El objetivo es tener un script que pueda ​hacer todo el trabajo necesario de forma automática, ​todos los días sin ninguna interacción del usuario
- recomendamos dividir la tarea para ​que cada pieza pueda escribirse y probarse por separado

---

## Ayuda para la investigación y la planificación
- Se recomienda usar expresiones regulares para extraer la información de los registros, ya que los registros siguen un patrón específico.
- Podemos usar la web [gregx101.com](https://regex101.com/) para probar nuestras expresiones regulares y asegurarnos de que funcionan correctamente.
- para contar y ordenar la información podemos usar diccionarios y listas en Python, y luego usar la función `sorted()` para ordenar los resultados.
- Podemos tener 2 diccionarios: uno para los errores y otro para los usuarios, donde las claves serán los mensajes de error o los nombres de usuario, y los valores serán el número de ocurrencias.
- Una vez que tengamos los datos contados y ordenados, podemos escribirlos en archivos CSV usando el módulo `csv` de Python.
- Luego tenemos que pasar esos archivos CSV al script `csv_to_html.py` para generar los archivos HTML.
- Se recomienda hacer esta tarea con bash, ya que tiene una sintaxis simple y es muy útil para automatizar tareas en Linux como mover archivos.

---

## Evaluación de Qwiklabs: Análisis de registros mediante expresiones regulares
- Imagine que su empresa utiliza un servidor que ejecuta un servicio llamadoticky, un sistema interno de tickets. El servicio registra eventos en syslog, tanto cuando se ejecuta correctamente como cuando encuentra errores.

- Los desarrolladores del servicio necesitan su ayuda para obtener información de esos registros, de modo que puedan comprender mejor cómo se utiliza su software y cómo mejorarlo. Por lo tanto, para este laboratorio, usted escribirá algunos scripts de automatización que procesarán el registro del sistema y generarán informes basados en la información extraída de los archivos de registro.

- Lo que harás
    - Utilizar regex para analizar un Archivo de registro
    - Añadir y modificar valores en un diccionario
    - Escribir a un archivo en formato CSV
    - Mover archivos al directorio apropiado para su uso con el conversor CSV->HTML

```bash
cat syslog.log
# Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)
# Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)
# Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)
# Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)
```

1. Crear script de Python para analizar el archivo de registro y generar un informe de errores y cantidad de ocurrencias de cada error, ordenado de mayor a menor.
```python
#!/usr/bin/env python3
import re
import csv
import sys

error_dict = {}
errorRegex = "ticky: ERROR ([\w ]*) "
fileSyslog = sys.argv[1]

def find_error(line, error_dict):
    errorMatch = re.search(errorRegex, line)
    if errorMatch:
        errorMessage = errorMatch.group(1)
        if errorMessage in error_dict:
            error_dict[errorMessage] += 1
        else:
            error_dict[errorMessage] = 1
    return error_dict

def write_csv(list, head, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(head)
        csvwriter.writerows(list)

with open(fileSyslog, 'r') as f:
    for line in f:
        error_dict = find_error(line, error_dict)
error_list = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
write_csv(error_list, ['Error', 'Count'], 'error_message.csv')
```
2. una estadística de uso para el servicio: Esto significa, una lista de todos los usuarios que han utilizado el sistema ​, incluyendo cuántos mensajes de información y ​cuántos mensajes de error han generado, este informe debe ordenarse por nombre de usuario.
```python
#!/usr/bin/env python3
import re
import csv
import sys

error_dict = {}
user_dict = {}
fileSyslog = sys.argv[1]

def find_error(line, error_dict):
    errorMatch = re.search("ticky: ERROR ([\w ]*) ", line)
    if errorMatch:
        errorMessage = errorMatch.group(1)
        if errorMessage in error_dict:
            error_dict[errorMessage] += 1
        else:
            error_dict[errorMessage] = 1
    return error_dict

def find_user(line, user_dict):
    userMatch = re.search("ticky: (INFO|ERROR) .* \(([\w\.]+)\)", line)
    if userMatch:
        messageType = userMatch.group(1)
        username = userMatch.group(2)
        if username not in user_dict:
            user_dict[username] = {'INFO': 0, 'ERROR': 0}
        user_dict[username][messageType] += 1
    return user_dict

def write_csv(list, head, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(head)
        csvwriter.writerows(list)

with open(fileSyslog, 'r') as f:
    for line in f:
        error_dict = find_error(line, error_dict)
        user_dict = find_user(line, user_dict)

user_list = sorted(user_dict.items())  # Ordenar por nombre de usuario
user_list = [(user, stats['INFO'], stats['ERROR']) for user, stats in user_list]
error_list = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
write_csv(error_list, ['Error', 'Count'], 'error_message.csv')
write_csv(user_list, ['Username', 'INFO', 'ERROR'], 'user_statistics.csv')
```
3. Crear archivo bash que ejecute el script de Python para generar los csv, luego ejecute el script csv_to_html.py para generar los archivos html
```bash
#!/bin/bash

logFile=$1
./ticky_check.py $logFile

./csv_to_html.py /home/student/error_message.csv /home/student/error_message.html
./csv_to_html.py /home/student/user_statistics.csv /home/student/user_statistics.html

mv /home/student/error_message.html /var/www/html/
mv /home/student/user_statistics.html /var/www/html/
```

---

## Ejemplo: Análisis de registros mediante expresiones regulares
- Para el ejercicio anterior es importante verificar los permisos: Tanto de los archivos script como de la carpeta /var/www/html/ para que el script pueda escribir los archivos html en esa carpeta.
```bash
sudo chmod o+w /var/www/html
sudo chmod +x csv_to_html.py
sudo chmod +x ticky_check.py
```
- Se hace un prueba del script csv_to_html.py con datos de usuarios y emails
- El script propuesto es:
```python
#!/usr/bin/env python3
import sys
import re
import operator
import csv

# Dict: Count number of entries for each user
per_user = {}  # Splitting between INFO and ERROR
# Dict: Number of different error messages
errors = {}

# * Read file and create dictionaries
with open('syslog.log') as file:
    # read each line
    for line in file.readlines():
        # regex search
        # * Sample Line of log file
        # "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        # Populates error dict with ERROR messages from log file
        if code == 'ERROR':
            if error_msg not in errors.keys():
                errors[error_msg] = 1
            else:
                errors[error_msg] += 1
        # Populates per_user dict with users and default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        # Populates per_user dict with users logs entry
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]["INFO"] += 1
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['ERROR'] += 1


# Sorted by VALUE (Most common to least common)
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

# Sorted by USERNAME
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()
# Insert at the beginning of the list
errors_list.insert(0, ('Error', 'Count'))

# * Create CSV file user_statistics
with open('user_statistics.csv', 'w', newline='') as user_csv:
    user_csv.write("Username,INFO,ERROR\n")
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' +
                       str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

# * Create CSV error_message
with open('error_message.csv', 'w', newline='') as error_csv:
    for key, value in errors_list:
        error_csv.write(str(key) + ',' + str(value)+'\n')
```

---

## Module 7 challenge: Log Analysis Using Regular Expressions
1. Which task can you accomplish by using regular expressions in log analysis?
> Parsing log entries to extract specific fields

1. What is the primary purpose of using regular expressions in log analysis? 
> To extract specific patterns and information from unstructured log data

2. What will the following command return? `grep "ERROR" syslog.log`
> All the ERROR logs in syslog

3. FIll in the blank. The command python3 opens a Python shell, also known as _____.
> Python interactive shell

3. Complete the sentence for the following Python regular expression: To match a string stored in a line variable, we use the search() method by defining a_____.
> pattern

4. When sorting this dictionary: `fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}` What will the following line of code return? `sorted(fruit.items(), key=operator.itemgetter(1))`
> [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

5. What is the primary advantage of using regular expressions when writing automation scripts to process a system log and generate reports from log files? 
> Flexible pattern matching for extracting specific data from log entries

5. Why do you need to know how to write automation scripts that process a system log and generate reports from the log files? 
> To eliminate the need for manual log analysis, saving time, and improving efficiency

6. Which of the following is true about using regular expressions? 
> They can simplify complex string processing tasks

6. Why are regular expressions useful? 
> They allow us to search and manipulate text based on patterns

7. What syntax would you use to enlist all the ERROR messages of a specific kind?
> grep ERROR [message] [file-name]

8. What is the Python module used to perform similar tasks to the Unix command grep for filtering log data?
> re (Regular Expression) module

8. In Python, regular expressions are typically handled using which module? 
> re

9. How does the sorted() function sort items in a Python dictionary? 
> Sorts dictionary items based on their keys in ascending order and returns a list of items #bad
> Sorts dictionary items based on their values in ascending order and returns a list of items ?

9. Evaluate the following problem statement: “I want to create a script to sort files.” What's missing?
> The problem statement does not specify what files to sort.

10. If there is no csv file named user_emails.csv, what will the command nano user_emails.csv return? 
> A new csv file named user_emails.csv

10. If there is no python script named ticky_check.py, what will the command nano ticky_check.py return?
> A new python script named ticky_check.py