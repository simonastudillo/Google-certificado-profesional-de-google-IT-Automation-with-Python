# Uso de Python para interactuar con el sistema operativo

- Módulo 1: Poniendo en marcha tu Python
- Módulo 2: Manejando archivo con Python
- Módulo 3: Expresiones regulares
- Módulo 4: Gestión de datos y procesos
- Módulo 5: Testing en Python
- Módulo 6: Bash scripting
- Módulo 7: Proyecto final

## Skills
- File I/O
- bash scripting
- scripting
- Unit testing
- Test Driven Development (TDD)
- File Management
- Operating Systems
- OS Process Management
- Linux commands
- Shell script
- Test Script Development
- Linux
- Development Testing
- Unix commands
- Scripting languages
- Software testing
- Test automation
- Command-line interface (CLI)
- Unix Shell
- Development Environment

## Resumen de sección

Esta sección cubre **7 módulos** del curso *Google IT Automation with Python* (Curso 2). A continuación un desglose detallado de cada módulo con los puntos clave y lo más difícil de cada uno.

---

### Módulo 1: Poniendo en marcha tu Python (5 archivos)

**Temas:** Sistema operativo (Kernel vs User Space), diferencia entre Windows/macOS/Linux, instalación de Python, uso de `pip`, intérprete vs compilado, shebang (`#!/usr/bin/env python3`), módulos y paquetes (`__init__.py`), IDEs, entornos virtuales (`venv`), automatización, fórmula `time_to_automate < (time_to_perform * amount_of_times_done)`, Principio de Pareto (80/20), bit-rot, módulos `shutil` y `psutil`.

**Puntos importantes:**
- Un sistema operativo tiene dos partes: Kernel (comunicación directa con hardware) y User Space (programas con los que interactuamos).
- Python 3 es la versión moderna. La `r` en cadenas como `r"texto"` crea raw strings.
- Los entornos virtuales (`python -m venv myenv`) aíslan dependencias entre proyectos.
- La fórmula de automatización ayuda a decidir si vale la pena automatizar una tarea.
- `pip freeze > requirements.txt` documenta dependencias.

**Lo más difícil:**
- Aplicar la fórmula de automatización y entender el ROI blando.

---

### Módulo 2: Manejando archivos con Python (5 archivos)

**Temas:** File descriptors, modos de apertura (`r`, `w`, `a`, `r+`), `with` para manejo automático de cierre, `readline()`, `read()`, `readlines()`, `strip()`, rutas absolutas vs relativas, `os.getcwd()`, `os.listdir()`, `os.remove()`, `os.rename()`, `os.path.exists()`, `os.path.getsize()`, `os.path.getmtime()`, `os.mkdir()`, `os.chdir()`, `os.rmdir()`, `os.path.join()`, archivos CSV con `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()`, dialectos CSV.

**Puntos importantes:**
- Siempre usar `with open(...) as file:` para evitar archivos abiertos olvidados.
- Usar `/` en rutas incluso en Windows para compatibilidad multiplataforma.
- `os.path.join()` es la forma correcta de construir rutas.
- CSV tiene dialectos que definen delimitadores y reglas de parseo.
- `DictReader` y `DictWriter` facilitan trabajar con archivos CSV con cabeceras.

**Lo más difícil:**
- Manejar dialectos CSV personalizados (espacios iniciales, comillas).

---

### Módulo 3: Expresiones regulares (4 archivos)

**Temas:** `re.search()`, `re.findall()`, `re.split()`, `re.sub()`, raw strings (`r""`), clases de caracteres (`[a-z]`), rangos, exclusión (`[^...]`), operador OR (`|`), cuantificadores (`*`, `+`, `?`, `{n}`, `{n,m}`), caracteres de escape (`\.`, `\(`), metacaracteres (`\w`, `\d`, `\s`, `\b`), anclas (`^`, `$`), grupos de captura `()`, backreferences (`\1`, `\2`), lookahead (`(?=...)`), `grep` en terminal.

**Puntos importantes:**
- `re.search()` encuentra la primera coincidencia; `re.findall()` encuentra todas.
- Los grupos de captura `()` permiten extraer partes específicas del texto.
- `re.sub(r"patrón", r"\1 \2", texto)` permite reemplazar con backreferences.
- `\b` marca límites de palabra (útil para palabras completas).
- `grep` es la herramienta CLI para regex: `grep "patrón" archivo`.

**Lo más difícil (es el módulo más denso):**
- Los cuantificadores greedy (`*` y `+` toman lo máximo posible).
- Escape de caracteres especiales (`\.` para punto literal, `\(` para paréntesis).
- Construir patrones complejos como `r"^([\w .-]*), ([\w .-]*)$"` para nombres.
- Diferencia entre `re.match()` (solo al inicio) y `re.search()` (en toda la cadena).
- Lookahead `(?=...)` para coincidencias condicionales.

---

### Módulo 4: Gestión de datos y procesos (4 archivos)

**Temas:** `input()`, flujos STDIN/STDOUT/STDERR, variables de entorno (`os.environ`), `PATH`, `sys.argv`, exit status (`echo $?`), `sys.exit()`, módulo `subprocess` (`run()`, `capture_output=True`, `Popen()`), `CompletedProcess`, `stdout.decode()`, codificación UTF-8, procesamiento de logs con `open()` + regex, diccionarios para conteo (`dict.get(key, 0) + 1`).

**Puntos importantes:**
- STDIN (entrada), STDOUT (salida), STDERR (errores) son los 3 flujos estándar.
- `sys.argv[0]` es el nombre del script, `sys.argv[1]` en adelante son argumentos.
- `exit 0` = éxito, `exit != 0` = error.
- `subprocess.run(["comando", "arg"], capture_output=True)` ejecuta comandos del sistema.
- `os.environ.copy()` permite modificar entorno para un subproceso sin afectar el principal.
- Para logs grandes, iterar línea por línea (no `readlines()`).

**Lo más difícil:**
- Entender los flujos STDIN/STDOUT/STDERR y la redirección (`>`, `2>`).
- `subprocess.Popen()` vs `subprocess.run()` vs `subprocess.call()`.
- Decodificar bytes a string con `decode()` y entender codificaciones (UTF-8).
- Procesar archivos de log con regex + condicionales + diccionarios anidados.

---

### Módulo 5: Testing en Python (5 archivos)

**Temas:** Pruebas manuales vs automáticas, casos de prueba, `unittest` (`TestCase`, `assertEqual`, `assertTrue`, `assertRaises`, `setUp()`, `tearDown()`), `pytest`, TDD (Test Driven Development), caja blanca vs caja negra, tests de integración, regresión, smoke test, load test, manejo de errores con `try`/`except`, `raise`, `assert`.

**Puntos importantes:**
- `unittest.main()` ejecuta las pruebas desde CLI. En Jupyter usar `unittest.main(argv=['ignored'], exit=False)`.
- Las pruebas unitarias deben aislarse del entorno de producción.
- `assertRaises(TipoError, funcion, args)` verifica que se lance una excepción esperada.
- TDD: escribir la prueba **antes** del código.
- `setUp()` se ejecuta antes de cada prueba, `tearDown()` después.
- CI (Integración Continua) ejecuta pruebas automáticamente al subir código.

**Lo más difícil:**
- Escribir casos límite (edge cases): strings vacíos, `None`, tipos incorrectos.
- Diferencia entre `raise` (errores esperados en ejecución normal) y `assert` (errores que no deberían ocurrir).
- Usar `try`/`except` correctamente sin silenciar errores importantes.
- Entender el ciclo TDD: escribir prueba → verificar que falla → escribir código → verificar que pasa → refactorizar.

---

### Módulo 6: Bash scripting (4 archivos)

**Temas:** Comandos Linux (`ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, `rmdir`, `touch`, `cat`, `echo`, `chmod`, `pwd`), redirección (`>`, `>>`, `<`, `2>`), pipes (`|`), señales (`SIGINT`, `SIGTERM`, `SIGTSTP`), `ping`, `ps`, `kill`, `grep`, `cut`, `sort`, `uniq`, `head`, `basename`, scripting bash (shebang `#!/bin/bash`, variables `$var`, `$1`, `$?`), condicionales (`if`/`then`/`else`/`fi`), test (`[ condición ]`), while/for loops, comparación bash vs Python.

**Puntos importantes:**
- `$(comando)` ejecuta un comando y usa su salida como argumento.
- `*` glob coincide con cualquier número de caracteres; `?` coincide con un carácter.
- En bash no puede haber espacios alrededor de `=` en asignación de variables.
- `exit status` de comandos (0 = éxito) se usa en condicionales `if`.
- `test -e archivo` verifica si un archivo existe.
- `cut -d' ' -f3` extrae el campo 3 usando espacio como delimitador.

**Lo más difícil:**
- La sintaxis de bash es muy diferente a Python (sin indentación obligatoria, `fi` cierra `if`, `done` cierra loops).
- Recordar que las variables en bash usan `$` para leer pero no para asignar.
- Los operadores de comparación (`-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`).
- Decidir cuándo usar bash vs Python: bash para scripts simples de manipulación de archivos/comandos; Python para lógica compleja, estructuras de datos y tests.
- Señales de procesos (`Ctrl+C` = SIGINT, `Ctrl+Z` = SIGTSTP, `kill` = SIGTERM).

---

### Módulo 7: Proyecto final (2 archivos)

**Temas:** Análisis de logs con regex, diccionarios para conteo de errores por tipo y por usuario, `sorted()` con `key=lambda` y `operator.itemgetter()`, generación de reportes CSV, conversión CSV a HTML, automatización con script bash que orquesta Python + `csv_to_html.py`, permisos de archivos y directorios web.

**Puntos importantes:**
- Enfocar el proyecto por partes: entender el problema, investigar, planificar, codificar y probar.
- Usar regex para extraer campos: `r"ticky: (INFO|ERROR) .* \(([\w\.]+)\)"`.
- Dos reportes: (1) errores ordenados por frecuencia descendente, (2) usuarios con conteo INFO/ERROR ordenado alfabéticamente.
- `sorted(dict.items(), key=lambda x: x[1], reverse=True)` ordena por valor descendente.
- Script bash final: ejecuta Python → genera CSVs → convierte a HTML → mueve a `/var/www/html/`.

**Lo más difícil:**
- Integrar todos los conocimientos del curso en un solo script funcional.
- Construir la expresión regular correcta para parsear las líneas de log del servicio `ticky`.
- Manejar diccionarios anidados para estadísticas por usuario (`user_dict[username]['INFO']`).
- Asegurar permisos correctos (`chmod`) para que los scripts y el servidor web funcionen.