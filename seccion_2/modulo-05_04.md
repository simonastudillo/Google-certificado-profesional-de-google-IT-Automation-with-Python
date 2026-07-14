# Errores y excepciones

## Revisión: El concepto de Try-except
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#!/usr/bin/env python3

def character_frequency(filename):
  """Counts the frequency of each character in the given file."""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    return None

  # Now process the file
  characters = {}
  for line in f:
    for char in line:
      characters[char] = characters.get(char, 0) + 1
  f.close() 
  return characters
```

---

## El concepto de Try-except
- Hasta ahora, cada vez que el intérprete lanzaba uno de ​estos errores, cambiamos nuestro código para evitar el error.
- Ese es un enfoque común, ya que cada vez que el intérprete ​plantea uno de estos errores el programa se detiene, ​y no queremos que nuestros scripts lleguen a su ​fin antes de que terminen su trabajo
- Otras veces hay tantas cosas que podrían salir ​mal que comprobar todas ellas se convierte en un reto. 
- Digamos que tenía una función que abrió ​un archivo e hizo algún procesamiento en él. ​¿ Qué pasa si el archivo no existe? ​¿ Qué sucede si el usuario no tiene ​permisos para leer el archivo? ​¿ O qué pasa si el archivo está bloqueado por un ​proceso diferente y no se puede abrir en este momento?
- Podríamos verificar todas ​estas condiciones, pero ¿qué pasa si hay ​otra cosa que podría causar que ​la función abierta genere un error
- un mejor enfoque es usar la construcción try-except.
- En este ejemplo, hemos puesto la llamada a ​la función open dentro de un bloque try-except
- Lo que esto hace es primero intentar hacer la operación que ​queremos que en este caso es abrir el archivo. ​Si hay un error, entonces entra en la parte de aceptación ​del bloque que coincide con ​el error y hace cualquier limpieza que sea necesaria
- El código en el bloque except se ejecutará solo si una de las instrucciones en el bloque try genera un error.

---

## Revisión: Generación de errores
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#!/usr/bin/env python3

def validate_user(username, minlen):
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True

from validations import validate_user
validate_user("", -1)

from validations import validate_user
validate_user("", 1)
validate_user("myuser", 1)

from validations import validate_user
validate_user(88, 1)

from validations import validate_user
validate_user([], 1)

from validations import validate_user
validate_user(["name"], 1)

#!/usr/bin/env python3

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True

from validations import validate_user
validate_user([3], 1)
```

---

## Errores de generación
- En el ejemplo anterior, hemos agregado una verificación de tipo para asegurarnos de que el nombre de usuario es una cadena.
- Si no lo es, generamos un error de aserción con un mensaje que explica el problema.
- Para generar un error personalizado, debemos usar la palabra clave `raise` seguida del tipo de error que queremos generar y un mensaje opcional que explique el error.
- En este caso se usa `ValueError` para indicar que el valor de `minlen` es inválido.
- `assert`: Esta palabra clave intenta verificar que ​una expresión condicional es verdadera, ​y si es falsa, genera ​un error de aserción con el mensaje indicado.
- Las aserciones son útiles para verificar que los valores de entrada a una función son válidos, y si no lo son, generan un error que puede ser capturado por un bloque try-except.
- Las aserciones pueden estar en cualquier lugar de nuestro código, sirven además para validar que los valores a lo largo de nuestro código son válidos.
- Como regla general, ​deberíamos usar `raise` ​para verificar las condiciones que esperamos que ocurran ​durante la ejecución normal de nuestro código y `assert` para ​verificar situaciones que no ​se esperan, pero que podrían causar que nuestro código se comporte mal.

---

## Revisión: Testing para errores esperados
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#!/usr/bin/env python3

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)


# Run the tests
unittest.main()
```
```bash
./validations_test.py 
```

---

## Testing para errores esperados
- En el ejemplo anterior, hemos agregado un caso de prueba para verificar que la función `validate_user` genera un error de `ValueError` cuando se le pasa un valor de `minlen` inválido.
- Para hacer esto, usamos el método `assertRaises` de la clase `unittest.TestCase`, que verifica que se genera un error del tipo especificado cuando se llama a la función con los argumentos proporcionados.
- Esto nos permite asegurarnos de que nuestra función maneja correctamente los casos de error y genera los errores esperados cuando se le pasan valores inválidos.

---

## Guía de estudio: Manejando errores
- En algunos casos, es mejor generar un error por nosotros mismos, y cómo comprobar que se genera el error correcto cuando eso es lo que esperas.
- También aprendimos a probar el código para verificar que hace lo que debe.
- Manejo de excepciones
    - Cuando se realiza el manejo de excepciones, es importante predecir qué excepciones pueden ocurrir.
    - A veces, para averiguar qué excepciones necesitas tener en cuenta, tienes que dejar que tu programa falle.
    - La forma más simple de manejar excepciones en Python es usando las cláusulas `try` y `except`.
    - En la cláusula `try`, Python ejecuta todas las sentencias hasta que encuentra una excepción. Usas la cláusula `except` para atrapar y manejar la(s) excepción(es) que Python encuentra en la cláusula `try`.
- Este es el proceso de cómo funciona:
1. Python ejecuta la cláusula try, por ejemplo, la(s) sentencia(s) entre las palabras clave try y except.
2. Si no se produce ningún error, Python se salta la cláusula except y finaliza la ejecución de la sentencia try.
3. Si se produce un error durante la ejecución de la cláusula try, Python se salta el resto de la cláusula try y transfiere el control al bloque except correspondiente. Si el tipo de error coincide con lo que se indica después de la palabra clave except, Python ejecuta la cláusula except. La ejecución continúa después del bloque try/except.
4. Si se produce una excepción pero no coincide con lo que aparece en la cláusula except, se pasa a las sentencias try fuera de ese bloque try/except. Sin embargo, si no se puede encontrar un manejador para esa excepción, la excepción se convierte en una excepción no manejada, la ejecución se detiene, y Python muestra un mensaje de error designado.

- A veces, una sentencia try puede tener más de una cláusula except para que el código pueda especificar manejadores para diferentes excepciones.
- Esto puede ayudar a reducir el número de excepciones no manejadas.
- Podemos usar excepciones para atrapar casi todo. Es una buena práctica como desarrollador o programador ser tan específico como sea posible con los tipos de excepciones que intentas manejar, especialmente si estás creando tus propias excepciones.

- Lanzar excepciones
- Como desarrollador o programador, es posible que quieras lanzar un error tú mismo. Normalmente, esto ocurre cuando algunas de las condiciones necesarias para que una función haga su trabajo correctamente no se cumplen y devolver ninguno o algún otro valor base no es suficiente.
- Puedes lanzar un error o lanzar una excepción, que fuerza a que se produzca una excepción en particular, y te notifica que algo en tu código va mal o que se ha producido un error.
- Algunos casos en los que lanzar una excepción es una herramienta útil:
    - Un archivo no existe
    - Falla una conexión de red o de base de datos
    - Su código recibe una entrada no válida
- En el ejemplo siguiente, el código lanza dos excepciones incorporadas en Python: raise ValueError y raise ZeroDivisionError.
```Python
# File reading function with exception handling
def read_file(filename):
	try:
		with open(filename, 'r') as f:
			return f.read()
	except FileNotFoundError:
		return "File not found!"
	finally:
		print("Finished reading file.")
```
- Imagine que tiene una función que lee datos de un fichero y luego divide dos números proporcionados dentro de ese fichero.
- Hay algunos fallos en ella que puedes atrapar con excepciones.
```Python
def faulty_read_and_divide(filename):
	with open(filename, 'r') as file:
		data = file.readlines()
		num1 = int(data[0])
		num2 = int(data[1])
		return num1 / num2
```
- Hay varios problemas potenciales aquí:
    - El archivo podría no existir, causando un FileNotFoundError.
    - El fichero podría no tener suficientes líneas de datos, provocando un IndexError.
    - Los datos del fichero podrían no ser convertibles a números enteros, lo que provocaría un ValueError.
    - El segundo número podría ser cero, lo que provocaría un ZeroDivisionError.
```Python
def enhanced_read_and_divide(filename):
	try:
		with open(filename, 'r') as file:
			data = file.readlines()
       	 
        # Ensure there are at least two lines in the file
        if len(data) < 2:
            raise ValueError("Not enough data in the file.")
       	 
        num1 = int(data[0])
        num2 = int(data[1])
       	 
        # Check if second number is zero
        if num2 == 0:
            raise ZeroDivisionError("The denominator is zero.")
       	 
        return num1 / num2


	except FileNotFoundError:
    	     return "Error: The file was not found."
	except ValueError as ve:
    	     return f"Value error: {ve}"
	except ZeroDivisionError as zde:
    	     return f"Division error: {zde}"
```
- Ahora, la función enhanced_read_and_divide está equipada para gestionar las posibles excepciones con elegancia, proporcionando mensajes de error informativos a la persona que llama.
- De esta forma, el código explicará cuándo falla, ya que ha identificado zonas de fallo potenciales, como cuando se trata de entradas impredecibles o contenido de archivos.

- assert sentencias
- assert las sentencias te ayudan a verificar si se cumple una determinada condición y lanzar una excepción en caso contrario
- Como su nombre indica, su propósito es "afirmar" que ciertas condiciones son verdaderas en puntos específicos de su programa.
- La sentencia assert existe en casi todos los lenguajes de programación y tiene dos usos principales:
    - Ayudar a detectar problemas antes en el desarrollo, en lugar de más tarde, cuando falla alguna otra operación, los problemas que no se abordan hasta más tarde en el proceso de desarrollo pueden resultar más largos y costosos de solucionar.
    - Proporcionar una forma de documentación para otros desarrolladores que lean el código.

--- 

## Errores y excepciones: Jupyter Notebook
- Below we have a function that removes an item from an input list. Run it to see what it does.
```Python
my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

# [5, 9, 6, 8]
```
- We used the RemoveValue() function to remove the number, 27 from the given list. Great! The function seems to be working fine. However, there is a problem when we try to call the function on the number 27 again. Run the following cell to see what happens.
```Python
print(RemoveValue(27))
```
```bash
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-3f8c37f416f6> in <module>
----> 1 print(RemoveValue(27))

<ipython-input-1-597531fc6dcc> in RemoveValue(myVal)
      2 
      3 def RemoveValue(myVal):
----> 4     my_list.remove(myVal)
      5     return my_list
      6 

ValueError: list.remove(x): x not in list
```
From the above output we see that our function now raises a ValueError. This is because we are trying to remove a number from a list that is not in the list. When we removed 27 from the list the first time, it was no longer available in the list to be removed a second time. Python is letting us know that the number 27 no longer makes sense for our RemoveValue() function.

We'd like to take control of the error messaging here and pre-empt this error. Fill in the blanks below to raise a ValueError in the RemoveValue() function if a value is not in the list. You can have the error message say something obvious like "Value must be in the given list".
```Python
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))
```
```bash
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-fb2c6a4acd6e> in <module>
      6     return my_list
      7 
----> 8 print(RemoveValue(27))

<ipython-input-5-fb2c6a4acd6e> in RemoveValue(myVal)
      1 def RemoveValue(myVal):
      2     if myVal not in my_list:
----> 3         raise ValueError("Value must be in the given list")
      4     else:
      5         my_list.remove(myVal)

ValueError: Value must be in the given list
```
Did your error message print correctly? Was the output something like: ValueError: Value must be in the given list? If not, go back to the previous cell and make sure you filled in the blanks correctly. If your error message did print correctly, great! You are on your way to mastering the basics of handling errors and exceptions.

Now, let's look at a different function. Below we have a function that sorts an input list alphabetically. Run it to see what it does.
```Python
my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))
# ['after', 'east', 'inside', 'over', 'up']
```
We used the OrganizeList() function to sort a given list alphabetically. The function seems to be working fine. However, there is a problem when we try to call the function on a list containing number values. Run the following cell to see what happens.
```Python
my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))
```
```bash
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-459d95f39adf> in <module>
      1 my_new_list = [6, 3, 8, "12", 42]
----> 2 print(OrganizeList(my_new_list))

<ipython-input-6-252da45e411d> in OrganizeList(myList)
      2 
      3 def OrganizeList(myList):
----> 4     myList.sort()
      5     return myList
      6 

TypeError: '<' not supported between instances of 'str' and 'int'
```
From the above output we see that our function now raises a TypeError. This is because the OrganizeList() function makes sense for lists that are filled with only strings. Take control of the error messaging here and pre-empt this error by filling in the blanks below to add an assert type argument that verifies whether the input list is filled with only strings. You can have the error message say something like "Word list must be a list of strings".
```Python
def OrganizeList(myList):
    for item in myList:
        raise TypeError("Word list must be a list of strings")
    myList.sort()
    return myList

print(OrganizeList(my_new_list))
```
```bash
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-cb30be109874> in <module>
      5     return myList
      6 
----> 7 print(OrganizeList(my_new_list))

<ipython-input-8-cb30be109874> in OrganizeList(myList)
      1 def OrganizeList(myList):
      2     for item in myList:
----> 3         raise TypeError("Word list must be a list of strings")
      4     myList.sort()
      5     return myList

TypeError: Word list must be a list of strings
```
Did your error message print correctly? Was the output something like: AssertionError: Word list must be a list of strings? If not, go back to the previous cell and make sure you filled in the blanks correctly. If your error message did print correctly, excellent! You are another step closer to mastering the basics of handling errors and exceptions.

Let's look at one last code block. The Guess() function below takes a list of participants, assigns each a random number from 1 to 9, and stores this information in a dictionary with the participant name as the key. It then returns True if Larry was assigned the number 9 and False if this was not the case. Run it to see what it does.
```Python
import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))

# False
```
The code seems to be working fine. However, there are some things that could go wrong, so find the part that might throw an exception and wrap it in a try-except block to ensure that you get sensible behavior. Do this in the cell below. Code your function to return None if an exception occurs.
```Python
# Revised Guess() function
def Guess(participants):
    try:
        my_participant_dict = {}
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except Exception:
        return None
```
Call your revised Guess() function with the following participant list.
```Python
participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))
# None
```
Was the above output None? If not, go back to the code block containing your revised Guess() function and make edits so that the output is None for the previous code block. If the above output was indeed None, congratulations! You've mastered the basics of handling errors and exceptions in Python and you are all done with this notebook!