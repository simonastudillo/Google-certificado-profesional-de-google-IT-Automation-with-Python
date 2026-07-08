# Expresiones regulares básicas

## Reseña: Emparejamiento simple en Python
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
result = re.search(r"aza", "plaza")
print(result)
# <_sre.SRE_Match object; span=(2, 5), match='aza'>

import re
result = re.search(r"aza", "bazaar")
print(result)
# <_sre.SRE_Match object; span=(1, 4), match='aza'>

import re
result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))
# None
# <_sre.SRE_Match object; span=(0, 1), match='x'>

import re
print(re.search(r"p.ng", "penguin"))
# <_sre.SRE_Match object; span=(0, 4), match='peng'>

import re
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
# <_sre.SRE_Match object; span=(4, 8), match='ping'>
# <_sre.SRE_Match object; span=(1, 5), match='pong'>

import re
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# <_sre.SRE_Match object; span=(0, 4), match='Pang'>
```

---

## Emparejamiento simple en Python
- La función `re.search()` busca un patrón en una cadena de texto y devuelve un objeto de coincidencia si encuentra el patrón, o `None` si no lo encuentra.
- La `r` al principio del patrón ​indica que se trata de una cadena sin procesar
- Esto significa que el intérprete de Python no debería ​intentar interpretar ningún carácter especial, ​y en su lugar, simplemente debería pasar ​la cadena a la función tal como está
- La `r` solo omite el procesamiento de `\` y no afecta a otros caracteres especiales como `.` o `^`.

---

## Reseña: Comodines y clases de personajes
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
print(re.search(r"[Pp]ython", "Python"))
# <_sre.SRE_Match object; span=(0, 6), match='Python'>

import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
# <_sre.SRE_Match object; span=(18, 22), match='hway'>
# None
# <_sre.SRE_Match object; span=(0, 6), match='cloudy'>
# <_sre.SRE_Match object; span=(0, 6), match='cloud9'>

import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))
# <_sre.SRE_Match object; span=(4, 5), match=' '>
# <_sre.SRE_Match object; span=(30, 31), match='.'>
# <_sre.SRE_Match object; span=(7, 10), match='cat'>
# <_sre.SRE_Match object; span=(7, 10), match='dog'>
# <_sre.SRE_Match object; span=(12, 15), match='dog'>
# <_sre.SRE_Match object; span=(7, 10), match='cat'>
# <_sre.SRE_Match object; span=(7, 10), match='dog'>
# <_sre.SRE_Match object; span=(12, 15), match='dog'>
# ['dog', 'cat']
```

---

## Comodines y clases de personajes
- Usar un punto es el comodín más amplio posible porque coincide absolutamente con ​cualquier carácter
- Las clases de caracteres se escriben entre corchetes y ​vamos a enumerar los caracteres que queremos que coincidan dentro de esos corchetes. 
- Ejemplo: Buscar todas las palabras con `p` y `P` usamos: `[pP]ython`
- Ejemplo: Buscamos `[a-z]way` para encontrar palabras que terminen con `way` y tengan una letra minúscula antes de `way`.
- Ejemplo: Buscamos `cloud[a-zA-Z0-9]` para encontrar palabras que comiencen con `cloud` y tengan una letra o un número después de `cloud`.
- Ejemplo: Si quieres excluir debemos agregar un spacio al final de los corchetes y anteponer un `^` al inicio de la clase de caracteres. Por ejemplo, `[^a-zA-Z ]` busca cualquier carácter que no sea una letra mayúscula o minúscula.
- Ejemplo: Usamos `|` para buscar coincidencias de varias palabras. Por ejemplo, `cat|dog` busca la palabra `cat` o la palabra `dog`.
- Podemos usar la función `re.findall()` para encontrar todas las coincidencias de un patrón en una cadena de texto y devolverlas como una lista. Por ejemplo, `re.findall(r"cat|dog", "I like both dogs and cats.")` devuelve `['dog', 'cat']`.

---

## Reseña: Calificadores de repetición
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))
"""
<_sre.SRE_Match object; span=(0, 9), match='Pygmalion'>
<_sre.SRE_Match object; span=(0, 17), match='Python Programmin'>
<_sre.SRE_Match object; span=(0, 6), match='Python'>
<_sre.SRE_Match object; span=(0, 3), match='Pyn'>
"""

import re
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
"""
<_sre.SRE_Match object; span=(1, 3), match='ol'>
<_sre.SRE_Match object; span=(1, 5), match='ooll'>
None
"""

import re
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
"""
<_sre.SRE_Match object; span=(3, 7), match='each'>
<_sre.SRE_Match object; span=(7, 12), match='peach'>
"""
```

---

## Calificadores de repetición
- El caracter `*` coincide con cero o más repeticiones del patrón anterior.
- Ejemplo: `Py.*n` coincide con cualquier cadena que comience con `Py` y termine con `n`, sin importar lo que haya en el medio.
- Esto búsca hasta la última coincidencia posible, por lo que puede coincidir con más de lo que esperas.
- Puedes usar `[a-z]*` para coincidir con cero o más letras minúsculas entre `Py` y `n`.
- El caracter `+` coincide con una o más repeticiones del patrón anterior.
- La diferencia con `*` es que `+` requiere al menos una coincidencia del patrón anterior.
- El caracter `?` coincide con cero o una repetición del patrón anterior.
- La diferencia con `*` es que `?` solo permite una coincidencia del patrón anterior, o ninguna.
```Python
"""
The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 
"""
import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
```

---

## Reseña: Personajes que escapan
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))
"""
<_sre.SRE_Match object; span=(2, 6), match='lcom'>
None
<_sre.SRE_Match object; span=(8, 12), match='.com'>
"""

import re
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
"""
<_sre.SRE_Match object; span=(0, 4), match='This'>
<_sre.SRE_Match object; span=(0, 19), match='And_this_is_another'>
"""
```

---

## Personajes que escapan
- El caracter `\` se usa para escapar caracteres especiales y darles un significado literal.
- Ejemplo: `\.com` busca la cadena literal `.com` en lugar de cualquier carácter seguido de `com`.
- Ejemplo: `\w*` coincide con cero o más caracteres alfanuméricos (letras, números y guiones bajos).
- Ejemplo: `\d` coincide con cualquier dígito (0-9).
- Ejemplo: `\s` coincide con cualquier espacio en blanco (espacios, tabulaciones, saltos de línea).
- Ejemplo: `\b` coincide con un límite de palabra, que es la posición entre un carácter de palabra y un carácter que no es de palabra.
```Python
"""
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
"""
import re
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
```

---

## Reseña: Expresiones regulares en acción
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))
"""
<_sre.SRE_Match object; span=(0, 9), match='Argentina'>
<_sre.SRE_Match object; span=(0, 9), match='Azerbaija'>
<_sre.SRE_Match object; span=(0, 9), match='Australia'>
"""

import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))
"""
<_sre.SRE_Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
None
<_sre.SRE_Match object; span=(0, 12), match='my_variable1'>
None
"""
```

---

## Expresiones regulares en acción
- Buscar países que contengan una `A` y hasta tener otra `a` usando `A.*a`.
- Buscar países que comienzan con `A` y terminan con `a` usando `^A.*a$`.
- Ejemplo: `^[a-zA-Z_][a-zA-Z0-9_]*$` busca nombres de variables válidos en Python.
    - `^` indica el inicio de la cadena.
    - `[a-zA-Z_]` indica que el primer carácter debe ser una letra o un guion bajo.
    - `[a-zA-Z0-9_]*` indica que los caracteres siguientes pueden ser letras, números o guiones bajos, y pueden repetirse cero o más veces.
    - `$` indica el final de la cadena.

---

## Guía de estudio: Expresiones regulares
- Una expresión regular (a veces llamada regex) es una cadena de caracteres que especifica un patrón para buscar coincidencias en un texto.
- Además de buscar coincidencias, permiten extraer partes específicas del texto, validar datos de entrada y son compatibles con editores de código y entornos de desarrollo integrados (IDE).
- Ejemplos:
    - `r"\d{3}-\d{3}-\d{4}"` busca un número de teléfono en el formato de USA: 123-456-7890.
    - `r"^-?\d*(\.\d+)?$"` busca un número decimal, que puede ser negativo y puede tener una parte fraccionaria.
    - `r"^/(.+)/([^/]+)/$"` busca una ruta de archivo en un sistema Unix o de una URL, donde el primer grupo captura el directorio y el segundo grupo captura el nombre del archivo.
- Puedes practicar en la página web [regex101.com](https://regex101.com/)