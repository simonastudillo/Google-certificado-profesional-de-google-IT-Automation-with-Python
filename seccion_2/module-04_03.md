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

---

## Filtrando archivos log con expresiones regulares
- La técnica habitual es llamar a ​la función `open()` que devuelve ​un objeto de archivo y luego iterar ​a través de cada una de sus líneas usando un for-loop.
- ​Recuerde que, por razones de rendimiento, ​cuando los archivos son grandes, ​generalmente es una buena práctica leerlos línea por ​línea en lugar de cargar todo el contenido en la memoria.
- Los trabajos de Cron se utilizan para ​programar scripts en sistemas operativos basados en UNIX
- En un for loop podemos usar la instrucción `continue` para omitir líneas que no nos interesan y centrarnos en las que sí nos interesan.
- Usamos expresiones regulares para obtener las lineas donde dice "USER" y extraer el nombre de usuario que se encuentra entre paréntesis.