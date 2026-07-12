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

---

## Pipes y pipelines
- Mediante pipes, puede conectar varios scripts, comandos ​u otros programas ​en una canalización de procesamiento de datos
- `Pipes`: Conectan la salida de ​un programa a la entrada de otro
- Esto significa que podemos pasar datos entre programas, ​tomando la salida de uno y ​convirtiéndolo en la entrada del siguiente
- `Pipe` esta representado por el símbolo de barra vertical (|) y se coloca entre los comandos que queremos conectar
- Podemos conectar el comando `ls -l` con el comando `less` usando un pipe, lo que nos permite ver la salida de `ls -l` página por página
- Esto nos muestra los resultados de `ls -l` en un formato más legible, permitiéndonos desplazarnos por la lista de archivos y directorios usando las teclas de dirección o la barra espaciadora, para salir podemos presionar la tecla `q`
- Podemos usar pipes para procesar datos de manera más compleja, ejemplo `cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head` 
    - `cat spider.txt`: muestra el contenido del archivo `spider.txt`
    - `tr ' ' '\n'`: reemplaza los espacios por saltos de línea, lo que convierte cada palabra en una línea separada
    - `sort`: ordena las palabras alfabéticamente
    - `uniq -c`: cuenta las ocurrencias de cada palabra única
    - `sort -nr`: ordena las palabras por frecuencia de aparición en orden descendente
    - `head`: muestra las primeras 10 palabras más frecuentes
- Podemos unir comandos de Linux/unix con scripts de Python, ejemplo `cat haiku.txt | ./capitalize.py` o `./capitalize.py < haiku.txt`
- En el primer ejemplo, la salida del comando `cat haiku.txt` se pasa como entrada al script `capitalize.py`, que capitaliza la primera letra de cada línea y muestra el resultado en la salida estándar.
- En el segundo ejemplo, el script `capitalize.py` lee directamente desde el archivo `haiku.txt` utilizando la redirección de entrada, logrando el mismo resultado.

---

## Revisión: Procesos de señalización
- Los siguientes bloques de código se usarán en el próximo video:
```bash
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
```
- Presiona ctrl + c para detener el proceso de ping y ver el resumen de estadísticas de la conexión.
```bash
--- www.example.com ping statistics ---

9 packets transmitted, 9 received, 0% packet loss, time 8013ms

rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms
```
```bash
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
```
- Presiona ctrl + z para detener el proceso de ping y enviarlo a segundo plano.
```bash
fg
#ping www.example.com
#64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=5 ttl=51 time=93.6 ms
```
```bash
--- www.example.com ping statistics ---

9 packets transmitted, 9 received, 0% packet loss, time 8013ms

rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms
```

---

## Procesos de señalización
- `Signals`: son tokens entregados a procesos en ejecución para indicar una acción deseada, podemos decirle a un programa que queremos que se detenga o termine
- `ping`: es un comando que envía paquetes de datos a un host remoto y espera una respuesta, lo que nos permite medir la latencia y la conectividad de la red
- El comando ping se ejecuta en un bucle infinito hasta que se le indique que se detenga, por lo que podemos usar señales para controlar su ejecución
    - `ctrl + c`: envía la señal SIGINT al proceso de ping, lo que provoca que se detenga y muestre un resumen de estadísticas de la conexión
    - `ctrl + z`: envía la señal SIGTSTP al proceso de ping, lo que provoca que se detenga temporalmente y se envíe a segundo plano. Podemos reanudar su ejecución con el comando `fg`, que trae el proceso de vuelta al primer plano.
    - `fg`: trae un proceso detenido o en segundo plano al primer plano, permitiéndonos interactuar con él nuevamente.
    - `kill`: es un comando que la señal SIGTERM a un proceso en ejecución, lo que provoca que se detenga de manera ordenada. 
    -  Para usar el comando kill, necesitamos conocer el ID del proceso (PID) que queremos terminar. 
- `ps`: es un comando que muestra información sobre los procesos en ejecución en el sistema, incluyendo su PID, estado, usuario y comando.
- `ps ax`: muestra todos los procesos en ejecución en el sistema, incluyendo los de otros usuarios y los procesos del sistema.
- `grep`: es un comando que busca un patrón en la entrada estándar o en un archivo, y muestra las líneas que coinciden con ese patrón.
- `ps ax | grep ping`: combina los comandos ps y grep para buscar el proceso de ping en la lista de procesos en ejecución, mostrando su PID y otra información relevante.

---

## Guía de estudio: Comandos básicos de Linux
- Gestión de archivos y directorios
    - `mv` se utiliza para mover uno o más archivos a un directorio diferente, renombrar un archivo, o ambas cosas a la vez.
        - `mv myfile.txt dir1/` Este comando mueve un archivo al directorio.
        - `mv file1.txt file2.txt file3.txt dir1/` Este comando mueve múltiples archivos.
    - `cp` se utiliza para copiar uno o más archivos.
        - `cp myfile.txt dir1/` Este comando copia un archivo al directorio.
        - `cp file1.txt file2.txt file3.txt dir1/` Este comando copia múltiples archivos.
    - `chmod`/`chown`/`chgrp` se utilizan para hacer que un archivo sea legible para todos en el sistema antes de moverlo a un directorio público.
        - `chmod +r file.html && mv file.html /var/www/html/index.html`: Este comando hace que el archivo sea legible para todos y luego lo mueve a un directorio público.
- Operar con el contenido de los archivos
    - `cut` es un comando que extrae campos de un archivo de datos
        - `cut -f1 -d"," addressbook.csv` Este comando extrae el primer campo de un archivo .csv.
        - `cut -c1-3,5-7,9-12 phones.txt` Este comando extrae los caracteres 1-3, 5-7 y 9-12 de un archivo .txt.
    - `sort` es un comando que ordena el contenido de un archivo
        - `sort names.txt` Este comando ordena las entradas alfabéticamente.
        - `sort -r names.txt` Este comando ordena las entradas en orden alfabético inverso, empezando por la letra z.
        - `sort -n numbers.txt` Este comando trata las entradas como números y luego las ordena numéricamente.
        - `ls -l | cut -w -f5,9 | sort -rn | head -10` Este comando muestra los 10 archivos más grandes del directorio actual.
        - `cut -f1-2 -d"," addressbook.csv | sort` Este comando extrae los nombres y apellidos de un archivo .csv y los ordena.
- Comandos adicionales
    - `id` es un comando que imprime información sobre el usuario actual. Este comando es útil si recibe un error de permisos denegados y cree que se le debería conceder acceso a un archivo.
    - `free` es un comando que imprime información sobre la memoria en el sistema actual.
    - `free -h` es un comando que imprime información sobre la memoria en el sistema actual en un formato legible para humanos.
        

>[!NOTE]
> Linux distingue entre mayúsculas y minúsculas, por lo que mv también puede utilizarse para cambiar las mayúsculas de un nombre de archivo.

---

## Redirecciones, tuberías y señales
- Gestión de flujos
    - `comando > archivo`: redirige la salida estándar, sobrescribe el archivo
    - `comando >> archivo`: redirige la salida estándar, anexa al archivo
    - `comando < archivo`: redirige la entrada estándar desde archivo
    - `comando 2> archivo`: redirige el error estándar a archivo
    - `comando1 | comando2`: conecta la salida del comando1 a la entrada del comando2
- Operando con procesos
    - `ps`: lista los procesos que se están ejecutando en el terminal actual para el usuario actual
    - `ps ax`: lista todos los procesos que se están ejecutando actualmente para todos los usuarios  
    - `ps e`: muestra el entorno de los procesos listados  
    - `kill PID`: envía la señal SIGTERM al proceso identificado por PID
    - `fg`: hace que un trabajo que estaba detenido o en segundo plano vuelva al primer plano
    - `bg`: hace que un trabajo que estaba detenido pase a segundo plano
    - `jobs`: enumera los trabajos actualmente en ejecución o parados
    - `top`: muestra los procesos que actualmente utilizan más tiempo de CPU (pulse "q" para salir)  