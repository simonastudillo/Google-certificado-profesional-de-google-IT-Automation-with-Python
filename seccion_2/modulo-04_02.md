# Subprocesos de Python

## Revisión: Ejecución de comandos del sistema en Python
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import subprocess
subprocess.run(["date"])

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)
```