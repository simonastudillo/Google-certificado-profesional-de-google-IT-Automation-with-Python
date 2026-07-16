# Interacción avanzado con Git

## Introducción a módulo 2: Usando Git localmente
- La capacidad de revertir los cambios anteriores es uno de ​los aspectos más útiles de los sistemas de control de versiones
- Podemos descartar los cambios realizados en un archivo, ​corregir una confirmación incorrecta ​e incluso revertir nuestro proyecto a una instantánea anterior
- Podemos usar ramas para trabajar en ​una función experimental sin ​afectar el código principal de nuestro proyecto, ​admitir versiones separadas de ​un programa que no se pueden combinar y mucho más

---

## Reseña: Saltándose el staging area
- Esta lectura contiene el código utilizado en los vídeos siguientes:
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

main()
```
```bash
git commit -a -m "Call check_reboot from main, exit with 1 on error"
git log
```

---

## Saltándose el staging area
- Podemos usar el flag `-a` con el comando `git commit` para omitir la zona de preparación y confirmar directamente los cambios en los archivos rastreados
- Esta bandera automáticamente coloca ​cada archivo que se realiza un seguimiento y ​modificado antes de realizar la confirmación ​dejando que se salte el paso git add

>[!NOTE]
> El flag `-a` no agregará archivos nuevos al área de preparación, solo los archivos que ya están siendo rastreados por Git.

- Git usa el alias `HEAD` para representar el último commit en la rama actual, por lo que podemos usar `HEAD` para referirnos a la confirmación más reciente
- El `HEAD` puede ser ​un commit en una rama diferente del proyecto

---

## Reseña: Obtener más información del usuario
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
git log -p
commit 033f27a8196987d61c4fd42930f2148b23434a03 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 14:39:18 2019 +0200

    Call check_reboot from main, exit with 1 on error

diff --git a/all_checks.py b/all_checks.py

index 340f1f7..710266a 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -1,12 +1,15 @@

 #!/usr/bin/env python3

 

 import os

+import sys

 

 def check_reboot():

     """Returns True if the computer has a pending reboot."""

     return os.path.exists("/run/reboot-required")

(...)
```
```bash
git log
commit 033f27a8196987d61c4fd42930f2148b23434a03 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 14:39:18 2019 +0200

    Call check_reboot from main, exit with 1 on error

commit cc1acbf10fdea6cc07ebf827697666b6a35b0f36

Author: My name <me@example.com>

Date:   Thu Jul 11 17:19:32 2019 +0200

    Add a check_reboot function

(...)

user@ubuntu:~/scripts$ git show cc1acbf10fdea6cc07ebf827697666b6a35b0f36

commit cc1acbf10fdea6cc07ebf827697666b6a35b0f36

Author: My name <me@example.com>

Date:   Thu Jul 11 17:19:32 2019 +0200

    Add a check_reboot function

diff --git a/all_checks.py b/all_checks.py

index c0d03b3..340f1f7 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -1,5 +1,11 @@

 #!/usr/bin/env python3

 

+import os

+

+def check_reboot():

+    """Returns True if the computer has a pending reboot."""

+    return os.path.exists("/run/reboot-required")

+

 def main():

     Pass
```
```bash
git log --stat
commit 033f27a8196987d61c4fd42930f2148b23434a03 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 14:39:18 2019 +0200

    Call check_reboot from main, exit with 1 on error

 all_checks.py | 5 ++++-

 1 file changed, 4 insertions(+), 1 deletion(-)

(...)
```
```bash
atom  all_checks.py
git  add -p

git diff
git diff --staged
git commit -m 'Add a message when everything is ok'
```

---

## Obtener más información del usuario
- Podemos usar el flag `-p` con el comando `git log` para ver los cambios realizados en cada `commit`
- Para ver detalles de un `commit` específico, podemos usar el comando `git show <commit_id>` para ver los cambios realizados en ese `commit`
- El flag `--stat` con el comando `git log` nos permite ver un resumen de los cambios realizados en cada `commit`, incluyendo el número de archivos modificados, el número de líneas agregadas y eliminadas, y un resumen de los cambios realizados en cada archivo
- Podemo pasar el nombre de un archivo al comando `git diff` para ver los cambios realizados en ese archivo desde el último `commit`
- Podemos usar el flag `-p` con el comando `git add` para agregar cambios específicos a la zona de preparación, lo que nos permite seleccionar qué cambios queremos confirmar en nuestro próximo `commit`
- Podemos usar el comando `git diff --staged` para ver los cambios que hemos agregado a la zona de preparación antes de confirmar los cambios en nuestro próximo `commit`