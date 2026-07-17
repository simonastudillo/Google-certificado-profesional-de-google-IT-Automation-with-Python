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