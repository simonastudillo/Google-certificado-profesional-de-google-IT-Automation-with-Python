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