# Procesando archivos log

## Qué son los archivos log
- El tipo de datos que puede encontrar en ​un archivo Syslog o en un registro de solicitudes web
- Los diferentes eventos que ocurren en ​programas que se ejecutan en ​un sistema y no están conectados a la ​terminal suelen ser archivos de log
- ​Los archivos de log contienen mucha información útil, ​especialmente cuando intenta depurar ​un problema complicado que está sucediendo en un equipo
- Usaremos expresiones regulares para extraer información de los archivos log

---

## Revisión: Filtrando archivos log con expresiones regulares
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#!/bin/env/python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    print(line.strip())



#!/bin/env/python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    print(line.strip())



import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])



#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    print(result[1])


chmod +x check_cron.py 
./check_cron.py syslog 
```