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