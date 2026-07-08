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