# Flujos de datos

## Introducción módulo 4: Gestión de datos y procesos
- En este módulo, analizaremos los conceptos que nos ayudan a interactuar con el ​sistema operativo ​en ejecución y veremos cómo podemos aprovechar al máximo las herramientas disponible
- Empezaremos hablando de cómo leer los datos de los usuarios de forma interactiva
- Exploraremos los flujos de datos de entrada y salida estándar que proporciona ​el sistema operativo y veremos cómo podemos interactuar con ellos, ​tanto desde los programas de Python como desde los programas del sistema
- cómo podemos ejecutar comandos del sistema desde Python. ​Esto permite que nuestros scripts aprovechen la potencia del resto del sistema operativo

---

## Reseña: Lectura interactiva de datos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
cat hello.py
#!/usr/bin/env python3

name = input("Please enter your name: ")
print("Hello, " + name)

./hello.py 
Please enter your name: Roger
#Output will be Hello, Roger

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")

./seconds.py 
Welcome to this time converter
Enter the number of hours: 1
Enter the number of minutes: 2
Enter the number of seconds: 3

Do you want to do another conversion? [y to continue] y
Enter the number of hours: 3
Enter the number of minutes: 2
Enter the number of seconds: 1

Do you want to do another conversion? [y to continue] n
```

---

## Lectura interactiva de datos
- Función `input()`: Permite leer datos de forma interactiva desde la entrada estándar (teclado). Esta función detiene la ejecución del programa hasta que el usuario ingresa un valor y presiona Enter.
- Recuerda que si esperas un número, debes convertir la entrada a un tipo numérico usando `int()` o `float()`, ya que `input()` siempre devuelve una cadena de texto.

---

## Reseña: Flujos estándar
- Los siguientes bloques de código se usarán en el próximo video:
```bash
cat streams.py
```
```Python
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
```
```bash
./streams.py 
# This will come from STDIN: Python Rocks!
# Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
# Well hello there, STDOUT

cat greeting.txt 
# Well hello there, STDOUT

ls -z
```

---

# Flujos estándar
- `I/O streams.` son flujos de datos que permiten la comunicación entre un programa y su entorno, como el sistema operativo o el usuario. Los flujos estándar más comunes son:
  - **STDIN (Standard Input)**: Flujo de entrada estándar, generalmente asociado al teclado.
  - **STDOUT (Standard Output)**: Flujo de salida estándar, generalmente asociado a la pantalla.
  - **STDERR (Standard Error)**: Flujo de error estándar, utilizado para mostrar mensajes de error.

---

## Reseña: Variables de entorno
- Los siguientes bloques de código se usarán en el próximo video:
```bash
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
# #!/usr/bin/env python3
# import os
# print("HOME: " + os.environ.get("HOME", ""))
# print("SHELL: " + os.environ.get("SHELL", ""))
# print("FRUIT: " + os.environ.get("FRUIT", ""))
./variables.py 
export FRUIT=Pineapple
./variables.py 
```

---

## Variables de entorno
- `shell` es un programa que proporciona una interfaz de línea de comandos para interactuar con el sistema operativo. Los shells suelen tener variables de entorno que almacenan información sobre el entorno del usuario y del sistema.
- El más utilizado en linux se llama `bash` (Bourne Again Shell). Otras opciones populares son `zsh`, `fish`, `csh`, entre otros.
- Para ver las variables de entorno de la terminal ejecuta el comando `env`
- la variable de entorno `PATH` es una lista de directorios separados por dos puntos (:) que el sistema operativo utiliza para buscar ejecutables cuando se ingresa un comando en la terminal. 
- Para ver el valor de la variable `PATH`, puedes ejecutar el comando `echo $PATH` en la terminal.
- Para obtener las variables de entorno desde un programa de Python, puedes usar el módulo `os` y acceder al diccionario `os.environ`. Por ejemplo:
```Python
import os
print("HOME: " + os.environ.get("HOME", ""))
```
- Se recomienda poner un segundo parámetro en caso de que la variable de entorno no exista, para evitar errores.
- Podemos añadir variables de entorno temporalmente en la terminal usando el comando `export`. Por ejemplo:
```bash
export FRUIT=Pineapple
```
>[!NOTE]
> Las variables de entorno establecidas con `export` solo duran mientras la terminal esté abierta. Una vez que cierres la terminal, las variables se perderán.

---

## Reseña: Argumentos de la línea de comandos y estado de salida
- Los siguientes bloques de código se usarán en el próximo video:
```bash
cat parameters.py 
# #!/usr/bin/env python3
# import sys
# print(sys.argv)

./parameters.py
# ['./parameters.py'] 

./parameters.py one two three
# ['./parameters.py', 'one', 'two', 'three']


wc variables.py
7 19 174 variables.py 	
echo $?
0

wc notpresent.sh
wc: notpresent.sh: No such file or directory
echo $?
1

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

./create_file.py example
echo $?
0

cat example 
New file created
./create_file.py example
Error, the file example already exists!
echo $?
1
```

---

## Argumentos de la línea de comandos y estado de salida
- `Command-line arguments` son los parámetros que se pasan a un programa cuando se ejecuta desde la línea de comandos.
- En Python, los argumentos de la línea de comandos se pueden acceder a través del módulo `sys` y la lista `sys.argv`. 
- El primer elemento de `sys.argv` es siempre el nombre del script, y los elementos siguientes son los argumentos proporcionados por el usuario.
- `exit status` es un valor numérico que un programa devuelve al sistema operativo al finalizar su ejecución.
- Un valor de salida de `0` generalmente indica que el programa se ejecutó correctamente, mientras que un valor distinto de `0` indica que ocurrió un error.
- Para ver el estado de salida del último comando ejecutado en la terminal, puedes usar el comando `echo $?`.
- En Python podemos establecer el estado de salida de un programa usando la función `sys.exit()`. Por ejemplo, `sys.exit(0)` indica una ejecución exitosa, mientras que `sys.exit(1)` indica un error.

---

## Más información sobre las funciones de entrada
- `input()` y `raw_input()` funcionan diferente en Python 2 y Python 3. 
- En Python 2, `input()` evalúa la entrada del usuario como código Python, mientras que `raw_input()` devuelve la entrada como una cadena de texto. 
- En Python 3, `raw_input()` fue eliminado y `input()` se comporta como `raw_input()` en Python 2, es decir, siempre devuelve una cadena de texto.
- `eval()` es una función que evalúa una cadena de texto como código Python.
- Ejemplo: `eval("2 + 2")` devolverá `4`. Sin embargo, usar `eval()` con entradas de usuario puede ser peligroso, ya que permite la ejecución de código arbitrario. Por lo tanto, se recomienda evitar su uso con datos no confiables.