# Interactuando con la linea de comandos de Bash

## Introducción al módulo 6: bash scripting
- ampliaremos ​nuestra exposición a lo que el ​sistema operativo Linux tiene para ofrecer
- Haremos un resumen de los ​comandos más comunes de Linux y veremos cómo podemos ​conectar los flujos de entrada y salida a ​archivos o incluso a otros programas
- Ser capaz de script y bash puede ser un ​complemento muy útil para nuestros scripts de Python
-  ​Al final de este módulo, ​debería sentirse mucho más cómodo ​interactuando con muchos comandos del sistema ​disponibles en Linux y creando sus propios scripts en ​Bash y sabiendo cuándo elegir ​Python o Bash para sus scripts

---

## Revisión: Comandos básicos de linux
- Los siguientes bloques de código se usarán en el próximo video:
```bash
mkdir mynewdir
cd mynewdir/
/mynewdir$ pwd
/mynewdir$ cp ../spider.txt .
/mynewdir$ touch myfile.txt
/mynewdir$ ls -l 
#Output:
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 myfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
/mynewdir$ ls -la
#Output:
#total 12
#drwxr-xr-x  2 user user  4096 Mai 22 14:17 .
#drwxr-xr-x 56 user user 12288 Mai 22 14:17 ..
#-rw-rw-r--  1 user user     0 Mai 22 14:22 myfile.txt
#-rw-rw-r--  1 user user   192 Mai 22 14:18 spider.txt
/mynewdir$ mv myfile.txt emptyfile.txt
/mynewdir$ cp spider.txt yetanotherfile.txt
/mynewdir$ ls -l
#Output:
#total 8
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 emptyfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:23 yetanotherfile.txt
/mynewdir$ rm *
/mynewdir$ ls -l
#total 0
/mynewdir$ cd ..
rmdir mynewdir/
ls mynewdir
#ls: cannot access 'mynewdir': No such file or directory
```

---

## Comandos básicos de linux
- Muchos comandos en linux no imprimen nada en la salida estándar, solo lo hacen cuando fallan.
- `echo`: imprime texto en la salida estándar
- `cat`: imprime el contenido de un archivo en la salida estándar
- `ls`: lista los archivos y directorios en el directorio actual
- `chmod`: cambia los permisos de un archivo o directorio
- `mkdir`: crea un nuevo directorio
- `cd`: cambia el directorio actual
- `pwd`: imprime el directorio de trabajo actual
- `cp`: copia un archivo o directorio
- `..`: Hace referencia al directorio padre del directorio actual
- `.`: Hace referencia al directorio actual
- `touch`: crea un archivo vacío
- `ls -l`: lista los archivos y directorios en el directorio actual con información detallada (permisos, nodos, usuario y grupo, tamaño, fecha de modificación y nombre)
- `ls -la`: lista los archivos y directorios en el directorio actual con información detallada, incluyendo archivos ocultos (aquellos que comienzan con un punto, tambien se muestra el directorio actual y el directorio padre)
- `mv`: mueve un archivo o directorio a otro lugar
- `rm`: elimina un archivo o directorio (para eliminar todos los archivos de un directorio, se puede usar `rm *`)
- `rmdir`: elimina un directorio vacío

---

## Revisión: Redirección de flujos
- Los siguientes bloques de código se usarán en el próximo video:
```bash
cat stdout_example.py 
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")
./stdout_example.py 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py > new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py >> new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
 #Don't mind me, just a bit of text here...
cat streams_err.py 
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
./streams_err.py < new_file.txt 2> error_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
cat error_file.txt 
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt 
#These are the contents of the file
```

---

## Redirección de flujos
- Por defecto, la entrada es proporcionada por el teclado en el terminal de texto y ​la salida y el error se muestran en la pantalla
- Podemos cambiar este valor predeterminado utilizando el proceso llamado redirección
- La ​redirección es un proceso de envío de una secuencia a un destino diferente
- Este proceso es proporcionado por el sistema operativo y ​puede ser realmente útil cuando desea almacenar la salida de un comando en un archivo, en ​lugar de simplemente mirarlo en una pantalla. 
- Si usamos un carácter mayor que (>) para redirigir la salida, en su lugar se creará un archivo con el contenido de la salida.
- al igual que vimos antes con el modo de archivo w utilizado por la función abierta ​cada vez que realizamos de redirección de STD hacia fuera, el destino se sobrescribe
- Para hacer un `append` a un archivo existente, podemos usar el doble carácter mayor que (>>) para redirigir la salida. Esto agregará la salida al final del archivo en lugar de sobrescribirlo.
- ​En lugar de utilizar el teclado para enviar datos a un programa, ​podemos usar el símbolo menor que (<) para leer el contenido de un archivo
- `2>` se utiliza para redirigir la salida de error a un archivo. Esto es útil cuando queremos capturar los errores generados por un programa en un archivo separado para su posterior análisis.
- Ejemplo: `./streams_err.py < new_file.txt 2> error_file.txt` redirige la entrada desde `new_file.txt` y redirige la salida de error a `error_file.txt`.
- Crear un archivo con echo: 
```bash
echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt
#Output: These are the contents of the file
```

---

## Revisión: Pipes y pipelines
- Los siguientes bloques de código se usarán en el próximo video:
```bash
ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
     # 7 the
     # 3 up
     # 3 spider
     # 3 and
     # 2 rain
     # 2 itsy
     # 2 climbed
     # 2 came
     # 2 bitsy
     # 1 waterspout.
```
```bash
cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())
```
```bash
cat haiku.txt 
#advance your career,
#automating with Python,
#it's so fun to learn.

```
```bash
cat haiku.txt | ./capitalize.py 
#Advance your career,
#Automating with python,
#It's so fun to learn.

```
```bash
./capitalize.py < haiku.txt
#Advance your career,
#Automating with python,
#It's so fun to learn.

```