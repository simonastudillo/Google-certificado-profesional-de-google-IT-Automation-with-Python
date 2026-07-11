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