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