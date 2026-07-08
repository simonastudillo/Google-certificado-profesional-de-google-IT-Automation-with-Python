# Expresiones regulares avanzadas

## Reseña: Capturando grupos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])
"""
<_sre.SRE_Match object; span=(0, 13), match='Lovelace, Ada'>
('Lovelace', 'Ada')
Lovelace, Ada
Lovelace
Ada
Ada Lovelace
"""

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")
# Ada Lovelace

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")
# Dennis Ritchie

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")
# Grace M. Hopper
```

---

## Capturando grupos
- Por ejemplo, es posible que deseemos extraer el nombre de host o ​un ID de proceso de una línea de registro y usar ese valor para otra operación. ​Para eso necesitamos usar un concepto de expresiones regulares llamadas ​grupos de captura.
- `Capturing groups` nos permiten extraer partes de una cadena que coinciden con un patrón de expresión regular. Se definen usando paréntesis `()` alrededor del patrón que queremos capturar.
- Podemos usar `result.groups()` para obtener una tupla de todos los grupos capturados, o podemos acceder a cada grupo individualmente usando índices, como `result[1]`, `result[2]`, etc.

---

## Reseña: Más información sobre los calificadores de repetición
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# <_sre.SRE_Match object; span=(2, 7), match='ghost'>

import re
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# <_sre.SRE_Match object; span=(2, 7), match='scary'

import re
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# ['scary', 'ghost', 'appea']

import re
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")
# ['scary', 'ghost']

import re
print(re.findall(r"\w{5,10}", "I really like strawberries"))
# ['really', 'strawberri']

import re
print(re.findall(r"\w{5,}", "I really like strawberries"))
# ['really', 'strawberries']

import re
print(re.search(r"s\w{,20}", "I really like strawberries"))
# <_sre.SRE_Match object; span=(14, 26), match='strawberries'>