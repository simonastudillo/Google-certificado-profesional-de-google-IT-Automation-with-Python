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
```Python
"""
We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets. We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440
"""

import re
def show_time_of_pid(line):
  pattern = r"^(\w+ \d+ \d+:\d+:\d+) .+\[(\d+)\]"
  result = re.search(pattern, line)
  return f"{result[1]} pid:{result[2]}"

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
```

---

## Revisión: Dar sentido a los datos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
"""
{'good_user': 1}
{'good_user': 2}
"""

#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)

    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)
```
```bash
./check_cron.py syslog
```

---

## Dar sentido a los datos
- Para mejorar nuestro resultado, sería una buena idea tener un recuento de cuántas veces ​aparece cada nombre de usuario en nuestro registro
- Almacenaremos el nombre de usuario como claves de un diccionario y usaremos el valor para ​contar el número de veces que cada nombre de usuario aparece en el archivo. 
- `usernames[name] = usernames.get(name, 0) + 1` Modificamos el diccionario para que el valor de la clave `name` sea el valor actual más 1. Si la clave no existe, se devuelve 0 y se le suma 1.
- Antes de agregar el nombre de usuario al diccionario, debemos asegurarnos de que la expresión regular haya encontrado un resultado.
- Esto lo hacemos con un if verificando si es un `None` y si es así, usamos `continue` para pasar a la siguiente línea. 