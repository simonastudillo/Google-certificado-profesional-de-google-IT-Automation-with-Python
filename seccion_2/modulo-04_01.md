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