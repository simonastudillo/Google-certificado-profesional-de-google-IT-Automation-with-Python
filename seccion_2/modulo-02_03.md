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