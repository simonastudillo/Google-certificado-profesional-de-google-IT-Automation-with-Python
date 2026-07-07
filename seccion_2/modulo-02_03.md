# Gestión de archivos y directorios

## Reseña: Trabajando con archivos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
 import os
 os.remove("novel.txt")

import os
os.remove("novel.txt")
os.remove("novel.txt")

os.rename("first_draft.txt", "finished_masterpiece.txt")

 os.path.exists("finished_masterpiece.txt")
 os.path.exists("userlist.txt")
```

---

## Trabajando con archivos
- El módulo `os` de Python proporciona funciones para interactuar con el sistema de archivos, sin importar el sistema operativo que estés utilizando.
- Para eliminar un archivo, se puede usar la función `os.remove()`, pasando como argumento la ruta del archivo que se desea eliminar.
- Si tratamos de eliminar un archivo que no existe, Python generará un error `FileNotFoundError`.
- Para renombrar un archivo, se puede usar la función `os.rename()`, pasando como argumentos la ruta del archivo que se desea renombrar y el nuevo nombre que se le quiere dar.
- Si tratamos de renombrar un archivo que no existe, Python generará un error `FileNotFoundError`.
- Para evitar estos errores usamos la función `os.path.exists()`, que devuelve `True` si el archivo existe y `False` si no existe.

---

## Reseña: Más información de archivos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
os.path.getsize("spider.txt")
#This code will provide the file size

os.path.getmtime("spider.txt")
#This code will provide a unix timestamp for the file

import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an 
#easy-to-understand format

os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path
```

---

## Más información de archivos
- Para obtener información adicional sobre un archivo, se pueden usar las funciones del módulo `os.path`.
- La función `os.path.getsize()` devuelve el tamaño del archivo en bytes.
- La función `os.path.getmtime()` devuelve la fecha y hora de la última modificación del archivo en formato de timestamp.
- Para convertir el timestamp a un formato de fecha y hora legible, se puede usar la función `datetime.datetime.fromtimestamp()`.
- La función `os.path.abspath()` devuelve la ruta absoluta del archivo.

---

## Reseña: Directorios
- Los siguientes bloques de código se usarán en el próximo video:
```Python
print(os.getcwd())
#This code snippet returns the current working directory.

os.mkdir("new_dir")
#The os.mkdir("new_dir") function creates a new directory called new_dir

os.chdir("new_dir")
os.getcwd()
#This code snippet changes the current working directory to new_dir. 
#The second line prints the current working directory.

os.mkdir("newer_dir")
os.rmdir("newer_dir")
#This code snippet creates a new directory called newer_dir. 
#The second line deletes the newer_dir directory.

import os
os.listdir("website")
#This code snippet returns a list of all the files and 
#sub-directories in the website directory.

 dir = "website"
 for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))
```

---

## Directorios
- El módulo `os` de Python también proporciona funciones para interactuar con directorios en el sistema de archivos.
- La función `os.getcwd()` devuelve la ruta del directorio de trabajo actual.
- La función `os.mkdir()` crea un nuevo directorio con el nombre especificado.
- La función `os.chdir()` cambia el directorio de trabajo actual al directorio especificado.
- La función `os.rmdir()` elimina un directorio vacío con el nombre especificado.
- La función `os.listdir()` devuelve una lista de todos los archivos y subdirectorios en el directorio especificado.
- La función `os.isdir()` devuelve `True` si la ruta especificada es un directorio y `False` si no lo es.