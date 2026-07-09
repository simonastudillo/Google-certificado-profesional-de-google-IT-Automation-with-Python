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