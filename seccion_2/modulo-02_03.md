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

---

## Guía de estudio: Archivos y directorios
- El módulo `os` de Python proporciona funciones para interactuar con el sistema de archivos, sin importar el sistema operativo que estés utilizando.
- Los nombres de archivo pueden considerarse como dos nombres separados por un punto.
- Por ejemplo, helloworld.txt es el nombre del archivo y la extensión define el tipo de archivo.
- El sistema operativo proporciona funciones para crear, leer, actualizar y eliminar archivos. Algunas de las funciones básicas incluyen:
    - Abrir y cerrar archivos
    - Leer y escribir archivos
    - Agregar a archivos
- Directorios: El módulo `os` de Python también proporciona funciones para interactuar con directorios en el sistema de archivos. Algunas de las funciones básicas incluyen:
    - Crear y eliminar directorios
    - Cambiar el directorio de trabajo actual
    - Listar archivos y subdirectorios en un directorio
- Permisos: El módulo `os` de Python también proporciona funciones para interactuar con los permisos de archivos y directorios en el sistema de archivos. Algunas de las funciones básicas incluyen:
    - Cambiar los permisos de un archivo o directorio
    - Verificar los permisos de un archivo o directorio

---

## Test your knowledge: Managing files and directories

1. The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".
```Python
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
```

2. The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 
```Python
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))
```

3.Which of the following methods from the os module will create a new directory?
> os.mkdir()

4. The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
```Python
import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date_time = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion 
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return ("{:%Y-%m-%d}".format(date_time))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
```

5. The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
```Python
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..')

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())
```