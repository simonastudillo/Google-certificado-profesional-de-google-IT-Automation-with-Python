# Deshacer cosas

## Revisión: Cómo deshacer los cambios antes del commit
- Los sigiuentes códigos se encuentran en el vídeo de la lección:
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