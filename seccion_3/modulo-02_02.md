# Deshacer cosas

## Revisión: Cómo deshacer los cambios antes del commit
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd scripts
atom all_checks.py
```
```Python
#!/usr/bin/env python3
  
import os
import sys

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
```
```bash
git status
git checkout all_checks.py
git status

./all_checks.py > output.txt
git add *
git status
git reset HEAD output.txt
git status
git commit -m "it should be os.path.exists"
```

---

## Cómo deshacer los cambios antes del commit
- `git checkout <file>`: Deshace los cambios en un archivo específico antes de hacer commit.
- `git checkout -p <file>`: Permite deshacer cambios de manera interactiva, seleccionando qué cambios específicos se quieren deshacer.
- `git reset HEAD <file>`: Deshace los cambios en el área de preparación (staging area) para un archivo específico, pero mantiene los cambios en el directorio de trabajo.

---

## Revisión: Modificar commits
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd scripts/
touch auto-update.py
touch gather-information.sh
ls -l

git add auto-update.py
git commit -m 'Add two new scripts'

git add gather-information.sh
git commit --amend
```

---

## Modificar commits
- `git commit --amend`: Permite modificar el último commit, ya sea para cambiar el mensaje del commit o para agregar cambios adicionales al mismo. Si quieres agregar más archivos al último commit, primero debes agregarlos al área de preparación (staging area) con `git add` y luego ejecutar `git commit --amend`.

>[!WARNING]
> Evita tanto como sea posible modificar commits que ya han sido compartidos con otros colaboradores, ya que esto puede causar conflictos y confusión en el historial del proyecto.

---

## Revisión: Rollback
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd scripts
atom all_checks.py
```
```Python
#!/usr/bin/env python3
  
import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

    if disk_full():
        print("Disk Full.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
```
```bash
./all_checks.py 

git revert HEAD
git revert HEAD

git log -p -2
```

---

## Rollback
- `git revert <commit>`: Git revert no solo significa deshacer. ​En su lugar, crea un commit que contiene el inverso de ​todos los cambios realizados en ​la confirmación incorrecta para cancelarlos.
- Por ejemplo, ​si se agregó una línea en particular en el commit incorrecto, ​entonces en el commit revertido, ​se eliminará la misma línea. 
- De esta manera obtienes el efecto de haber deshecho los cambios, ​pero el historial de los commits en el proyecto sigue siendo ​consistente dejando un registro de exactamente lo que sucedió
- `git revert HEAD`: Revertir el último commit. Esto crea un nuevo commit que deshace los cambios del commit más reciente.

---

## Revisión: Identificar un commit
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd checks
git log -1

git log -2
git show 30e70712882267ca2dd749acfa02ea3aacfd0b24

git show 30

git show 30e7

git revert 30e7

git revert 7d71

git show 7d1de19
```

---

## Identificar un commit
- Git usa un hash SHA-1 de 40 caracteres para identificar de manera única cada commit. Sin embargo, no es necesario escribir el hash completo para referirse a un commit específico. Git permite usar los primeros caracteres del hash siempre que sean suficientes para identificar de manera única el commit deseado.
- `git log -1`: Muestra el último commit realizado en la rama actual.
- `git log -2`: Muestra los dos últimos commits realizados en la rama actual.
- `git show <commit>`: Muestra los detalles de un commit específico, incluyendo el mensaje del commit y los cambios realizados en los archivos, puedes pasar el hash completo o los primeros caracteres del hash para identificar el commit.
- En caso de que pasos una cantidad de caracteres insuficiente para identificar un commit de forma única, Git te mostrará un mensaje de error indicando que el commit no se puede encontrar. 

---

## Guía de estudio: Git Revert
- `git checkout`: Deshace los cambios en un archivo específico antes de hacer commit.
- `git reset`: Deshace los cambios en el área de preparación (staging area) para un archivo específico, pero mantiene los cambios en el directorio de trabajo.
- `git commit --amend`: Permite modificar el último commit, ya sea para cambiar el mensaje del commit o para agregar cambios adicionales al mismo.
- `git revert`: Crea un commit que contiene el inverso de todos los cambios realizados en la confirmación incorrecta para cancelarlos, manteniendo el historial de commits consistente.
- [documentación oficial de Git](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things)
- [SHA1 Collision detection in Git](https://github.blog/news-insights/company-news/sha-1-collision-detection-on-github-com/)

---

## Test your knowledge: Undoing things
1. Let's say we've made a mistake in our latest commit to a public branch. Which of the following commands is the best option for fixing our mistake?
> git revert

2. If we want to rollback a commit on a public branch that wasn't the most recent one using the revert command, what must we do?
> use the commit ID at the end of the git revert command

3. What does Git use cryptographic hash keys for?
> To guarantee the consistency of our repository

4. What does the command git commit --amend do?
> Overwrite the previous commit

5. How can we easily view the log message and diff output the last commit if we don't know the commit ID?
> git log #bad
> git show