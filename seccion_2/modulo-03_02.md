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