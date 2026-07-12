# Revisión de módulo

## Recapitulación del módulo 5: Pruebas en Python
- Hemos aprendido a configurar Python en su entorno local ​y aprender a administrar archivos, ​procesar textos, iniciar procesos del sistema, ​usar expresiones regulares y archivos de registro de procesos
- Aprendimos sobre los diferentes tipos de pruebas ​y cómo escribir nuestras propias pruebas unitarias en Python

---

## Glosario de términos del curso 2, Módulo 5
- `automated testing` (Prueba automática): Proceso en el que el software se autocomprueba para detectar errores y confirmar que funciona correctamente
- `black box testing` (Pruebas de caja negra): Pruebas en las que se sabe qué debe hacer el programa, pero no cómo lo hace
- `edge cases` (Casos extremos): Entradas de código que producen resultados inesperados y se encuentran en los extremos de los rangos de entrada
- `Pytest` (pytest): Una potente herramienta de pruebas de Python que ayuda a los programadores a escribir programas más eficaces y estables
- `software testing` (Pruebas de software): Proceso de evaluación de un código informático para determinar si hace o no lo que se espera de él
- `test case` (Caso de prueba): Es la unidad individual de prueba que busca una respuesta específica a un conjunto de entradas
- `test fixture` (Dispositivo de prueba): Preparado para realizar una o varias pruebas
- `test suite` (Conjunto de pruebas): Se utiliza para compilar pruebas que deben ejecutarse conjuntamente
- `test runner` (Ejecutor de pruebas): Este ejecuta la prueba y proporciona a los desarrolladores los datos del resultado
- `unittest` (unittest): Un conjunto de herramientas de Python para construir y ejecutar pruebas unitarias
- `unit tests` (Pruebas unitarias): Prueba para verificar que pequeñas partes aisladas de un programa funcionan correctamente
- `white box testing` (Prueba de caja blanca): Una prueba en la que el creador de la prueba sabe cómo funciona el código y puede escribir casos de prueba que utilizan la comprensión para asegurarse de que se realiza como se esperaba

---

## Evaluación de Qwiklabs: Implementación de pruebas unitarias
Introducción
Imagina que uno de tus compañeros informáticos se acaba de jubilar y te ha dejado una carpeta de scripts para que los utilices. Uno de los scripts, llamado emails.py, empareja a los usuarios con una dirección de correo electrónico y nos permite buscarlos fácilmente En la mayoría de los casos, el script funciona muy bien: se introduce el nombre de un empleado y su dirección de correo electrónico se imprime en la pantalla. Pero, en el caso de algunos empleados, el resultado no es del todo correcto. Tu trabajo es añadir una prueba para reproducir el error, hacer las correcciones necesarias y verificar que todas las pruebas pasan para asegurarte de que el script funciona Mucha suerte

Lo que tienes que hacer: 
    - Escribir una prueba simple para comprobar la funcionalidad básica
    - Escribir una prueba para comprobar los casos extremos
    - Corregir el código con una sentencia try/except

Tenga en cuenta que después de este laboratorio hay un cuestionario con calificación. Debe completar el laboratorio antes de realizar el cuestionario. El cuestionario evaluará su comprensión de los conceptos y procedimientos clave tratados en el laboratorio.

Esto es lo que puedes hacer para prepararte:
    - Preste mucha atención a las instrucciones y explicaciones que se dan durante la sesión de laboratorio.
    - Participa activamente en las actividades del laboratorio y toma notas.
    - Repasa tus apuntes antes de realizar la prueba.
```Python
#!/usr/bin/env python3

import unittest
from emails import find_email

class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()
```
```Python
#!/usr/bin/env python3


import sys
import csv

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/student/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()
```

----

## Ejemplo: Aplicación de pruebas unitarias
```bash
python3 emails.py Blossom Gill
# blossom@abc.edu
```
- Generamos las pruebas para el script emails.py
```Python
#!/usr/bin/env python3
import unittest
from emails import find_email
class EmailsTest(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()
```
- damos permisos `chmod +x emails_test.py` y ejecutamos `./emails_test.py`
```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
- Caso de prueba 1: Falta de parámetros
```bash
python3 emails.py Kirk
Traceback (most recent call last):
  File "emails.py", line 30, in <module>
    main()
  File "emails.py", line 27, in main
    print(find_email(sys.argv))
  File "emails.py", line 20, in find_email
    fullname = str(argv[1] + " " + argv[2])
IndexError: list index out of range
```
- Modificamos el test para que falle y agregamos un caso de prueba para la falta de parámetros
```Python
#!/usr/bin/env python3
import unittest
from emails import find_email
class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)
  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()
```
- Guardamos y ejecutamos nuevamente `./emails_test.py`
```bash
.E
======================================================================
ERROR: test_one_name (__main__.TestFile)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./emails_test.py", line 15, in test_one_name
    self.assertEqual(find_email(testcase), expected)
  File "/home/student/scripts/emails.py", line 20, in find_email
    fullname = str(argv[1] + " " + argv[2])
IndexError: list index out of range

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (errors=1)
```
- Debemos modificar el script emails.py para que maneje la excepción y devuelva un mensaje de error en lugar de fallar
- Se agrega un bloque try/except para manejar la excepción IndexError y devolver un mensaje de error en lugar de fallar
```Python
#!/usr/bin/env python3
import sys
import csv
def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict
def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"
def main():
  print(find_email(sys.argv))
if __name__ == "__main__":
  main()
```
- Guardamos y ejecutamos nuevamente `./emails_test.py`
```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
- Caso de prueba 2: Dirección de correo electrónico aleatoria
Busquemos otros Casos extremos. Buscaremos un empleado que no existe. ¿Puede esperar la salida que daría el script? La salida esperada en tal caso debería ser "No se ha encontrado ninguna dirección de correo electrónico". Veamos cómo reacciona el script ante este caso añadiendo un caso de prueba en el fichero emails_test.py justo después del segundo caso de prueba.
```Python
#!/usr/bin/env python3
import unittest
from emails import find_email
class EmailsTest(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)
  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)
  def test_two_name(self):
    testcase = [None, "Roy","Cooper"]
    expected = "No email address found"
    self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()
```
- Guardamos y ejecutamos nuevamente `./emails_test.py`
```bash
..F
======================================================================
FAIL: test_two_name (__main__.EmailsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./emails_test.py", line 16, in test_two_name
    self.assertEqual(find_email(testcase), expected)
AssertionError: None != 'No email address found'

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
```
- Vamos a editar el script emails.py para que devuelva el mensaje "No se ha encontrado ninguna dirección de correo electrónico" cuando los usuarios buscados no existan.
```Python
#!/usr/bin/env python3
import csv
import sys
def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict
def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"
def main():
  print(find_email(sys.argv))
if __name__ == "__main__":
  main()
```
- Guardamos y ejecutamos nuevamente `./emails_test.py`
```bash
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```
- Ejecutamos el script emails.py con un empleado que no existe
```bash
python3 emails.py Roy Cooper
No email address found
```

---

## Module 5 challenge: Implementing Unit Testing

1. What is the cause of an IndexError?
> Attempting to access an index that's outside the bounds of a list.

2. The function find_emails(argv) searches a dictionary using the employee’s first and last name, and then returns the matching email address. How does the script accept the input of the employee’s name? 
> The script accepts the employee's first name and last name as command-line arguments.

3. When you began working with the existing emails.py script, what mode did you need to open it in? 
> Edit mode

4. If a try clause is executed and an exception occurs, but there is no match for the exception in any of the except clauses, what happens?
> It's an unhandled exception and the execution stops with an error message.

5. What is the purpose of software testing? 
> To prove that the software works correctly

6. When referring to unit testing, what are “classes”? 
> Classes are test cases that correct bugs.

7. The following code will either return an email address for an employee or an error message if there is no employee matching the name entered. What would the error message be?
```Python
if email_dict.get(fullname.lower()):
    return email_dict.get(fullname.lower())
else:
    return "No email"
```
> "No email"

8. Which of the following commands represent the correct sequence for catching an exception for a division by zero error in Python? 
> try: a/b except ZeroDivisionError: pass

9. The following portion of code will return an error message if a user fails to enter the full name of the employee for a search. What will the error message be?
```Python
def find_email(argv):
 """ Return an email address based on the username given."""
 # Create the username based on the command line input.
 try:
   fullname = str(argv[1] + " " + argv[2])
   # Preprocess the data
   email_dict = populate_dictionary('/home/<username>/data/user_emails.csv')
   # Find and print the email
   return email_dict.get(fullname.lower())
 except IndexError:
   return "Missing name"
```
> "Missing name"

10. When writing a try/except clause, how many except clauses can be included? 
> As many except clauses are needed to specify handlers for different exceptions. 