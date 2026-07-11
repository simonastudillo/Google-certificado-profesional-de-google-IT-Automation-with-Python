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

