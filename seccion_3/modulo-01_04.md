# Usando Git

## Reseña: Primeros passo con Git
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
git config --global user.email "me@example.com"
git config --global user.name "My name"

mkdir checks
cd checks
git init

ls -la

ls -l

ls -l .git/

cp ../disk_usage.py .
ls -l

git add disk_usage.py 
git status

git commit
```

---

## Primeros pasos con Git
- Lo primero es indicar a Git quienes somos, para ello usamos los siguientes comandos:
```bash
git config --global user.email "me@example.com"
git config --global user.name "My name"
```
- Luego podemos crear un nuevo directorio para nuestro proyecto y entrar en él
- una vez dentro del directorio, podemos inicializar un nuevo repositorio Git con el comando `git init`
- Usamos el comando `ls -la` para listar todos los archivos y carpetas, incluyendo los ocultos, y podemos ver que se ha creado un nuevo directorio llamado `.git`, que contiene toda la información del repositorio
- Podemos usar el comando `ls -l .git/` para ver los archivos y carpetas dentro del directorio `.git`, y podemos ver que contiene varios archivos y carpetas que Git utiliza para rastrear los cambios en nuestro proyecto
- `Working tree` o `árbol de trabajo` es el directorio donde trabajamos con nuestros archivos y carpetas, y es donde hacemos cambios en nuestro proyecto
- `Staging area` o `área de preparación` es donde preparamos los cambios que queremos confirmar en nuestro repositorio, y es donde usamos el comando `git add` para agregar archivos a la zona de preparación
- `git status` nos permite ver el estado de nuestro repositorio, incluyendo los archivos que han sido modificados, los archivos que están en la zona de preparación y los archivos que no están siendo rastreados por Git
- `git commit` nos permite confirmar los cambios que hemos preparado en la zona de preparación, y nos pedirá que ingresemos un mensaje de confirmación que describa los cambios realizados

---

## Reseña: Tracking files
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
cd checks
ls -l

git status

atom disk_usage.py 
git status

git commit -m 'Add periods to the end of sentences.'

git status
```

---

## Tracking files
- `track file` significa que Git comenzará a rastrear los cambios en un archivo específico, cada vez que hagamos una modificación en ese archivo, Git lo registrará como un cambio en nuestro proyecto
- `untracked file` significa que Git no está rastreando los cambios en un archivo específico, y cualquier modificación que hagamos en ese archivo no será registrada por Git
- Los archivos tienen 3 estados en Git:
    - Si un archivo está en el estado modificado, ​significa que hemos realizado cambios en él que aún no hemos cometido. ​Los cambios podrían ser agregar, modificar o eliminar el contenido del archivo. ​Git nota cada vez que modificamos nuestros archivos. ​Pero no almacenará ningún cambio hasta que los añadamos al `staging area`.
    - Un archivo en el estado `staged` significa que los cambios en esos archivos están listos para ser comprometidos con el proyecto. ​Todos los archivos que se ponen en escena formarán parte de la próxima instantánea que tomemos
    - `committed` significa que los cambios en esos archivos se han guardado en el repositorio de Git. ​Cada vez que confirmamos un cambio, Git toma una instantánea de todos los archivos en el área de preparación y almacena una referencia a esa instantánea en el historial del proyecto

---

## Reseña: El workflow básico de Git
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
mkdir scripts
cd scripts
git init

git config -l
```
```Python
#!/usr/bin/env python3

def main():
    pass

main()
```
```bash
chmod +x all_checks.py
git status
git add all_checks.py
git commit -m 'Create an empty all_checks.'
```
```Python
#!/usr/bin/env python3

import os

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")	

def main():
    pass

main()
```
```bash
git status
git add all_checks.py 
git status
git commit -m 'Add a check_reboot function'
```