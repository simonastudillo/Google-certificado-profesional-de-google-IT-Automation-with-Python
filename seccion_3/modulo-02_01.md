# Interacción avanzado con Git

## Introducción a módulo 2: Usando Git localmente
- La capacidad de revertir los cambios anteriores es uno de ​los aspectos más útiles de los sistemas de control de versiones
- Podemos descartar los cambios realizados en un archivo, ​corregir una confirmación incorrecta ​e incluso revertir nuestro proyecto a una instantánea anterior
- Podemos usar ramas para trabajar en ​una función experimental sin ​afectar el código principal de nuestro proyecto, ​admitir versiones separadas de ​un programa que no se pueden combinar y mucho más

---

## Reseña: Saltandose el staging area
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