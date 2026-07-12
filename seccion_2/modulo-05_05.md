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