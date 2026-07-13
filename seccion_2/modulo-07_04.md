# Repaso del módulo

## Resumen del módulo 6: Programación en Bash
- Vimos porque Linux es uno de los sistemas operativos más usados en el mundo del IT
- Permite a los usuarios ejecutar comandos y scripts para automatizar tareas.
- Aprendimos sobre crear bash scripts, su diferencia con Python y cómo ejecutarlos.
- "Hay muchas máquinas en el laboratorio donde trabajo en ​Google que requieren configuración, ​y mi equipo tardará una eternidad en ​configurar cada máquina de una a la vez. ​Al automatizar algunas de estas tareas, ​puedo hacer el trabajo rápidamente y tener tiempo ​para trabajar en proyectos nuevos y más interesantes"

---

## Glosario de términos
- `bash script` (Script Bash): Un script que contiene varios comandos.
- `cut` (Cortar): Un comando que divide y toma solo partes de cada línea usando espacios.
- `Globs` (Comodines): Caracteres que crean listas de archivos, como el asterisco y el signo de interrogación.
- `Pipes` (Tuberías): Un proceso para conectar la salida de un programa con la entrada de otro.
- `Piping` (Enrutamiento de datos): Un proceso para conectar varios scripts, comandos u otros programas en una cadena de procesamiento de datos.
- `Redirection` (Redirección): Un proceso para enviar un flujo de datos a un destino diferente.
- `Signals` (Señales): Tokens que se envían a los procesos en ejecución para indicar una acción deseada.

---

## Qwiklabs assessment: Edit files using substrings
En este laboratorio, cambiarás el nombre de usuario de tu compañera Jane Doe de "jane" a "jdoe" para cumplir con la política de nombres de la empresa. El cambio de nombre de usuario ya se realizó. Sin embargo, algunos archivos que tenían el nombre anterior de Jane, "jane", aún no se han actualizado. Para solucionar esto, escribirás un script de Bash y un script de Python que se encargarán de las operaciones de cambio de nombre necesarias.
- Qué harás
- Practicarás el uso de los comandos `cat`, `grep` y `cut` para operaciones con archivos.
- Usarás los comandos `>` y `>>` para redirigir el flujo de entrada/salida.
- Reemplazarás una subcadena usando Python.
- Ejecutarás comandos de Bash en Python.
- Ten en cuenta que después de esta práctica hay un cuestionario calificado. Debes completar la práctica antes de realizar el cuestionario. El cuestionario evaluará tu comprensión de los conceptos y procedimientos clave vistos en la práctica.
- Aquí tienes algunas sugerencias para prepararte:
- Presta mucha atención a las instrucciones y explicaciones proporcionadas durante la sesión de práctica.
- Participa activamente en las actividades de la práctica y toma notas.
- Repasa tus notas de la práctica antes de realizar el cuestionario.
---
The Scenario
Your coworker Jane Doe currently has the username jane but she needs to it to jdoe to comply with your company's naming policy. This username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated. For example, jane_profile_07272018.doc needs to be updated to jdoe_profile_07272018.doc.

To view files in data directory, use the following command:

```bash
ls data
```

You can list the contents of the directory using the ls command. This directory contains a file named list.txt. You will also find some other files within this directory.

To view the contents of the file, use the following command:

```bash
cat ~/data/list.txt
# 001 jane /data/jane_profile_07272018.doc
# 002 kwood /data/kwood_profile_04022017.doc
# 003 pchow /data/pchow_profile_05152019.doc
# 004 janez /data/janez_profile_11042019.doc
# 005 jane /data/jane_pic_07282018.jpg
# 006 kwood /data/kwood_pic_04032017.jpg
# 007 pchow /data/pchow_pic_05162019.jpg
# 008 jane /data/jane_contact_07292018.csv
# 009 kwood /data/kwood_contact_04042017.csv
# 010 pchow /data/pchow_contact_05172019.csv
```

This file contains three columns: line number, username, and full path to the file.

Let's try out the commands we learned in the previous section to catch all the jane lines.

```bash
grep 'jane' ~/data/list.txt
```

This returns all the files with the pattern jane. It also matches the file that has string janez within it.

```bash
001 jane /data/jane_profile_07272018.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_07282018.jpg
008 jane /data/jane_contact_07292018.csv
```

Next, we'll use the cut command with grep command. For cut command, we'll use the whitespace character (' ') as a delimiter (denoted by -d) since the text strings are separated by spaces within the list.txt file. We'll also fetch results by specifying the fields using -f option.

Let's fetch the different fields (columns) using -f flag :

```bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 1
# 001
# 005
# 008
```

```bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 2
# jane
# jane
# jane
```

```bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 3
# /data/jane_profile_07272018.doc
# /data/jane_pic_07282018.jpg
# /data/jane_contact_07292018.csv
```

You can also return a range of fields together by using:

```bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 1-3
```

o return a set of fields together:

```bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 1,3
```

Test command
We'll now use the test command to test for the presence of a file. The command test is a command-line utility on Unix-like operating systems that evaluates conditional expressions.

The syntax for this command is:

```bash
test EXPRESSION
```

We'll use this command to check if a particular file is present in the file system. We do this by using the -e flag. This flag takes a filename as a parameter and returns True if the file exists.

We'll check the existence of a file named jane_profile_07272018.doc using the following command:

```bash
if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
# File exists
```

Create a file using a Redirection operator
We'll now use the redirection operator (>) to create an empty file simply by specifying the file name. The syntax for this is:

```bash
> [file-name]
```

Let's create a file named test.txt using the redirection operator and use ls command to list the files.

```bash
ls > test.txt
# data  scripts  test.txt
```

To append any string to the test.txt file, you can use another redirection operator (>>).

```bash
echo "I am appending text to this test file" >> test.txt
```

You can view the contents of the file at any time by using the cat command.

```bash
cat test.txt
# I am appending text to this test file
```

Iteration
Another important aspect of a scripting language is iteration. Iteration, in simple terms, is the repetition of a specific set of instructions. It's when a set of instructions is repeated a number of times or until a condition is met. And for this process, bash script allows three different iterative statements:

For: A for loop repeats the execution of a group of statements over a set of items.
While: A while loop executes a set of instructions as long as the control condition remains true.
Until: An until loop executes a set of instructions as long as the control condition remains false.
Let's now iterate over a set of items and print those items.

```bash
for i in 1 2 3; do echo $i; done
# 1
# 2
# 3
```

Find files using bash script
In this section, you are going to write a script named findJane.sh within the scripts directory.

This script should catch all jane lines and store them in another text file called oldFiles.txt. You will complete the script using the command we practiced in earlier sections. Don't worry, we'll guide you throughout the whole process.

Navigate to /scripts directory and create a new file named findJane.sh.

```bash
cd ~/scripts
```

```bash
nano findJane.sh
```

Now, add the shebang line.

```bash
#!/bin/bash
```

Create the text file oldFiles.txt and make sure it's empty. This oldFiles.txt file should save files with username jane.

```bash
grep " jane " ~/data/list.txt | cut -d ' ' -f 3 > oldFiles.txt
# /home/student/data/jane_profile_07272018.doc
# /home/student/data/jane_contact_07292018.csv
```

Rename files using Python script
In this section, you are going to write a Python script, changeJane.py, that takes oldFiles.txt as a command line argument and then renames files with the new username jdoe. You will be completing the script, but we will guide throughout the section.

Create a Python script changeJane.py under /scripts directory using nano editor.

```bash
nano changeJane.py
```

Now, import the necessary Python module to use in the Python script.

```python
#!/usr/bin/env python3
import sys
import subprocess
```

The sys (System-specific parameters and functions) module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter. The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and get their return codes.

Continue writing the script to achieve the goal!

Since oldFiles.txt is passed as a command line argument, it's stored in the variable sys.argv[1]. Open the file from the first argument to read its contents using open() method. You can either assign it to a variable or use a with block. Hint: traverse each line in the file using readlines() method. Use line.strip() to remove any whitespaces or newlines and fetch the old name.

Once you have the old name, use replace() function to replace jane with jdoe. This method replaces occurrences of any older substring with the new substring. The old and new substrings are passed as parameters to the function. Therefore, it returns a string where all occurrences of the old substring is replaced with the new substring.

```python
string.replace(old_substring, new_substring)
```

Now, invoke a subprocess by calling run() function. This function takes arguments used to launch the process. These arguments may be a list or a string.

In this case, you should pass a list consisting of the command to be executed, followed by arguments to the command.

Use the mv command to rename the files in the file system. This command moves a file or directory. It takes in source file/directory and destination file/directory as parameters. We'll move the file with old name to the same directory but with a new name.

```bash
mv source destination
```

Now it must be clear. You should pass a list consisting of the mv command, followed by the variable storing the old name and new name respectively to the run() function within the subprocess module.

Close the file that was opened at the beginning.

```python
f.close()
```

Once you have completed writing the bash script, save the file by clicking Ctrl-o, Enter key, and Ctrl-x.

Make the file executable using the following command:

```bash
chmod +x changeJane.py
```

Run the script and pass the file oldFiles.txt as a command line argument.

```bash
./changeJane.py oldFiles.txt
```

Navigate to the /data directory and use the ls command to view renamed files.

```bash
cd ~/data
ls
# janez_profile_11042019.doc  jdoe_profile_07272018.doc  kwood_profile_04022017.doc  pchow_pic_05162019.jpg
# jdoe_contact_07292018.csv   kwood_pic_04032017.jpg     list.txt
```

---

## Ejemplo: Editar archivos usando subcadenas
- En el ejercicio anterior usamos `grep " jane " ~/data/list.txt | cut -d ' ' -f 3` para obtener la lista de archivos que contienen el nombre de usuario "jane".
- Creamos el script de Bash `findJane.sh` para guardar la lista de archivos en un archivo llamado `oldFiles.txt`.
```bash
#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3);
for file in $files; do
    if test -e "..${file}"; then echo "..${file}" >> oldFiles.txt; fi
done
```
- Le damos el permiso y lo ejecutamos
```bash
chmod +x findJane.sh
./findJane.sh
cat oldFiles.txt
# /home/student/data/jane_profile_07272018.doc
# /home/student/data/jane_contact_07292018.csv
```
- Luego generamos un script que cambie el nombre de los archivos de "jane" a "jdoe" usando Python. Creamos el script `changeJane.py` y lo ejecutamos.
```python
#!/usr/bin/env python3
import sys
import subprocess
with open(sys.argv[1]) as file:
    lines = file.readlines()
    for line in lines:
        oldvalue = line.strip()
        newvalue = oldvalue.replace("jane", "jdoe")
        subprocess.run(["mv", oldvalue, newvalue])
file.close()
```
```bash
chmod +x changeJane.py
./changeJane.py oldFiles.txt
cd ~/data
ls
# janez_profile_11042019.doc  jdoe_profile_07272018.doc  kwood_profile_04022017.doc  pchow_pic_05162019.jpg jdoe_contact_07292018.csv   kwood_pic_04032017.jpg     list.txt
```