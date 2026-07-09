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

---

## Revisión: Gestión avanzada de subprocesos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
```

---

## Gestión avanzada de subprocesos
- `os.environ.copy()` devuelve una copia del diccionario de variables de entorno del proceso actual. Esto permite modificar el entorno para un subproceso sin afectar al proceso principal.
- `os.pathsep` es un carácter que se utiliza para separar rutas en la variable de entorno `PATH`. En sistemas Unix, es `:` y en Windows, es `;`.
- El parámetro `env` de `subprocess.run()` permite especificar un conjunto de variables de entorno para el subproceso.
- Al modificar la variable `PATH` en el entorno del subproceso, se puede controlar qué directorios se buscan para encontrar ejecutables. Esto es útil cuando se desea ejecutar un programa que no está en los directorios estándar del sistema.
- Si estamos automatizando una tarea única y bien definida, ​estamos desarrollando una solución ​rápidamente es el mayor requisito, ​entonces el uso de comandos y ​subprocesos del sistema puede ayudar mucho
- Pero si estamos haciendo algo ​más complejo o de larga duración, ​generalmente es una buena idea usar el cebo ​en o módulos externos que Python proporciona

---

## Guía de estudio: Subprocesos de Python
- En Python, existen muchas maneras diferentes de realizar una misma tarea.
- Algunas son más fáciles de escribir, otras se adaptan mejor a una tarea específica y otras requieren menos recursos computacionales.
- Los subprocesos permiten llamar y ejecutar otras aplicaciones desde Python, incluyendo otros scripts.
- En Python, el módulo `subprocess` puede ejecutar código y aplicaciones nuevos mediante la creación de nuevos procesos desde el programa.
- Gracias a esta capacidad, `subprocess` es una forma muy útil de ejecutar varios procesos en paralelo en lugar de secuencialmente.
- Los subprocesos de Python pueden iniciar procesos para:
    - Abrir varios archivos de datos en una carpeta simultáneamente.
    - Ejecutar programas externos.
    - Conectarse a `input`, `output` y `error`, y obtener códigos de retorno.
- Comparación entre subprocess, OS y Pathlib
    - Una vez más, Python ofrece múltiples maneras de realizar la mayoría de las tareas; subprocess es extremadamente potente, ya que permite hacer todo lo que se haría desde Python en la consola y obtener información de vuelta a Python.
    - Pero el hecho de poder usar subprocess no siempre significa que sea lo más conveniente.
    - Comparemos subprocess con dos de sus alternativas: 
        - OS, que ya se ha tratado en otras lecturas, y Pathlib.
        - Para tareas como obtener el directorio de trabajo actual o crear un directorio, OS y Pathlib son más directas (o "pythónicas", es decir, utilizan el lenguaje tal como fue concebido).
        - Usar subprocess para estas tareas es como usar una palanca para abrir una tuerca.
        - Es más complejo y puede resultar excesivo para operaciones sencillas.
- Ejemplo: obtener el directorio de trabajo actual
- Sub proceso
`cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()`
- OS:
`cwd_os = os.getcwd()`
- Pathlib:
`cwd_pathlib = Path.cwd()`
- Ejemplo: Crear un directorio
- Sub proceso
`subprocess.run(['mkdir', 'new_directory'])`
- OS:
`os.mkdir('new_directory')`
- Pathlib:
`test_dir_pathlib2 = Path('test_dir_pathlib2')`
`test_dir_pathlib2.mkdir(exist_ok=True) #Ensures the directory is created only if it doesn't already exist`
- Donde Subprocess brilla
    - Las formas básicas de usar Subprocess son los métodos `.run()` y `.Popen()`.
    - Existen métodos adicionales: `.call()`, `.check_output()` y `.check_call()`.
    - Normalmente, bastará con usar `.run()` o uno de los dos métodos de verificación cuando sea apropiado.
    - Sin embargo, al crear procesos paralelos o comunicarse entre subprocesos, ¡`.Popen()` ofrece mucha más potencia!
    - `.run()` es la forma más sencilla de ejecutar un comando (su nombre lo indica) y `.Popen()` es la forma más completa de llamar a comandos externos.
    - Todos los métodos `.run()`, `.call()`, `.check_output()` y `.check_call()` son envoltorios de la clase `.Popen()`.
- `.run()`
    - El comando `.run()` es el método recomendado para invocar subprocesos.
    - Ejecuta el comando, espera a que finalice y luego devuelve una instancia de `CompletedProcess` que contiene información sobre el proceso.
    - Ejecutar el comando `echo` usando `.run()`:
        - `result_run = subprocess.run(['echo', '¡Hola, mundo!'], capture_output=True, text=True)`
        - `result_run.stdout.strip()` # Extrae la salida estándar y elimina los espacios en blanco adicionales.
        - Salida: `'¡Hola, mundo!'`
- `.call()`
    - El comando `call()` ejecuta una instrucción, espera a que finalice y luego devuelve el código de retorno.
    - `call` es un comando antiguo y ahora se recomienda usar `.run()`, pero es útil ver cómo funciona.
    - Ejecutando el comando `echo` con `call()`:
    - `return_code_call = subprocess.call(['echo', '¡Hola desde call!'])`
    - `return_code_call`
    - Salida: `0` El valor devuelto 0 indica que el comando se ejecutó correctamente.
- `.check_call()` y `.check_output()`
    - Utilice `check_call()` para obtener solo el estado de un comando.
    - Utilice `check_output()` para obtener también la salida.
    - Estas opciones son útiles en situaciones como la entrada/salida de archivos, donde un archivo podría no existir o la operación podría fallar.
    - El comando `check_call()` es similar a `call()`, pero genera una excepción `CalledProcessError` si devuelve un código de salida distinto de cero.
    - Ejemplo para ejecutar el comando `echo` con `check_call()`:
    - `return_code_check_call = subprocess.check_call(['echo', '¡Hola desde check_call!'])`
    - `return_code_check_call`
    - Salida: `0` El valor devuelto (0) indica que el comando se ejecutó correctamente.
    - Usando `check_output()` para ejecutar el comando `echo`:
    - `output_check_output = subprocess.check_output(['echo', '¡Hola desde check_output!'], text=True)`
    - `output_check_output.strip()` # Extrayendo la salida estándar y eliminando los espacios en blanco adicionales.
    - Salida: `'¡Hola desde check_output!'`
- `.Popen()`
    - La función `Popen()` ofrece características más avanzadas que las funciones mencionadas anteriormente. Permite crear un nuevo proceso, conectarse a sus canales de entrada/salida/error y obtener su código de retorno.
    - Ejemplo para ejecutar el comando `echo` con `Popen`:
    - `process_popen = subprocess.Popen(['echo', '¡Hola desde popen!'], stdout=subprocess.PIPE, text=True)`
    - `output_popen, _ = process_popen.communicate()`
    - `output_popen.strip()` (Extrae la salida estándar y elimina los espacios en blanco adicionales)
    - Salida: `¡Hola desde popen!`