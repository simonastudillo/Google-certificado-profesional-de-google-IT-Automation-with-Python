# Subprocesos de Python

## Revisión: Ejecución de comandos del sistema en Python
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import subprocess
subprocess.run(["date"])

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)
```

---

## Ejecución de comandos del sistema en Python
- Módulo `subprocess` de Python permite ejecutar comandos del sistema operativo desde un script de Python.
- La función `subprocess.run()` se utiliza para ejecutar un comando y esperar a que termine.
- Para ejecutar el comando externo se crea un entorno secundario para ​el proceso o subproceso secundario en el que se ejecuta el comando. ​Mientras que el proceso principal, que es nuestro script, ​está esperando que el subproceso termine, está bloqueado, lo ​que significa que el padre no puede hacer ningún trabajo hasta que el hijo termine.
- Para enviar argumentos al comando, se pasan como una lista de cadenas de texto. Por ejemplo, para ejecutar `ls -l`, se usaría `subprocess.run(["ls", "-l"])`.
- El comando `subprocess.run()` devuelve un objeto `CompletedProcess` que contiene información sobre la ejecución del comando.
- Incluye un atributo `returncode` que indica el estado de salida del comando ejecutado. Un valor de `0` generalmente indica éxito, mientras que un valor distinto de `0` indica un error.

---

## Revisión: Obtención del resultado de un comando del sistema
- Los siguientes bloques de código se usarán en el próximo video:
```Python
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)


import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
```

---

## Obtención del resultado de un comando del sistema
- El comando `who` se utiliza para mostrar información sobre los usuarios que están actualmente conectados al sistema.
- Para capturar la salida de un comando, se puede usar el parámetro `capture_output=True` en la función `subprocess.run()`. Esto permite acceder a la salida estándar y al error estándar del comando ejecutado.
- El comando `host` se utiliza para realizar consultas de DNS y obtener información sobre nombres de dominio y direcciones IP.
- El resultado de la ejecución de un comando se puede acceder a través de los atributos `stdout` y `stderr` del objeto `CompletedProcess`. Estos atributos contienen la salida estándar y el error estándar del comando, respectivamente.
- La respuesta de `stdout` y `stderr` se devuelve como bytes, por eso tiene un `b` al inicio. Para convertirlo a una cadena de texto legible, se puede usar el método `decode()`.
- Los datos de los equipos se almacenan y transmiten en ​bytes y cada uno puede representar hasta 256 caracteres
- Pero hay miles de caracteres posibles por ​ahí solían escribir en varios idiomas.
- El chino, por ejemplo, ​requiere más de 10.000 caracteres diferentes
- Para poder escribir en esos idiomas, se ​han creado varias especificaciones llamadas codificaciones a lo largo del ​tiempo para indicar qué secuencias ​de bytes representan qué caracteres
- Hoy en día, la mayoría de las personas usan codificación UTF-8, ​que es parte del estándar Unicode que ​enumera todos los caracteres posibles ​que se pueden representar. 

>[!NOTE]
> El parámatro `capture_output=True` esta disponible a partir de Python 3.7. 