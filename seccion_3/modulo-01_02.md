# Antes del control de versiones

## Introducción al módulo 1: Control de versiones
- ​Imagina que tu equipo ha agregado una nueva funcionalidad ​a un script que examina el bienestar ​de todas las computadoras de las que eres responsable.
- La nueva verificación examina que el firmware de tu computadora, ​conocido también como UEFI, ​este actualizado a la última versión
- Cuando despliegas esto, ​de repente te das cuenta que ​la mitad de las computadoras dicen estar dañadas.
- ​Después de algunas revisiones, descubres que ​la revisión necesita tener en cuenta ​los diferentes modelos de las computadoras
- Puede que te sientas tentado a hacer un arreglo rápido del código, ​enviarlo de inmediato a las máquinas que han sido afectadas, ​especialmente si el problema parece fácil de arreglar
- Pero es más habitual que ​los arreglos rápidos incluyan errores ​porque no nos tomamos el tiempo ​para probar el nuevo código correctamente
- Podemos usar VCS para revertir el código a una versión anterior estable
- Luego podemos arreglar el código y probarlo antes de enviarlo a las computadoras afectadas

---

## Conservación de copias históricas
- Si sentías que algunas de las cosas que se eliminaron un día, ​podrían tener que añadirse más adelante. ​Así que cada vez que estabas a punto eliminar una parte significativa, ​hacías una copia de todo, por si acaso. 
- Si algo de esto te suena familiar, ya has trabajado en la forma más primitiva ​de un control de versiones, manteniendo copias históricas.
- Decimos que esto es primitivo, porque es muy manual y no muy detallado
- Primero, necesitas recordar hacer la copia.
- ​Segundo, generalmente haces una copia de todo el archivo, ​incluso si sólo estas cambiando una pequeña parte. 
- Y tercero, incluso si envías los cambios por correo a tus colegas, ​puede ser difícil averiguar al final, quién hizo qué y, lo más importante, ​por qué lo hicieron. 

---

## Reseña: Comparación de archivos
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
cat rearrange1.py 
/usr/bin/env python3
import re
def reordenar_nombre(nombre):
    resultado = re.search(r"^([\w .]*), ([\w .]*)$", nombre)
    if resultado == None:
        return nombre
    return "{} {}".format(resultado[2], resultado[1])
```
```bash
cat rearrange2.py
/usr/bin/env python3

import re

def reordenar_nombre(nombre):
    resultado = re.search(r"^([\w .-]*), ([\w .-]*)$", nombre)
    if resultado == None:
        return nombre
    return "{} {}".format(resultado[2], resultado[1])
```
```bash
diff rearrange1.py rearrange2.py 
6c6

< resultado = re.search(r"^([\w .]*), ([\w .]*)$", nombre)

---

> resultado = re.search(r"^([\w .-]*), ([\w .-]*)$", nombre)
```
```bash
diff validations1.py validations2.py 
5c5,6

< assert (type(nombredeusuario) == str), "nombredeusuario debe ser una cadena"

--

> if type(nombreusuario != str:

> raise TypeError("el nombre de usuario debe ser una cadena")

11a13,15

> return False

> # Los nombres de usuario no pueden empezar por un número

> if nombredeusuario[0].isnumeric():
```
```bash
diff -u validations1.py validations2.py 
--- validaciones1.py 2019-06-06 14:28:49.639209499 +0200

+++ validaciones2.py 2019-06-06 14:30:48.019360890 +0200

@@ -2,7 +2,8 @@



def validar_usuario(nombre_usuario, minlen):

-assert type(nombre_usuario) == str, "nombre_usuario debe ser una cadena"

+ if type(nombre_usuario) != str:

+ raise TypeError("el nombre de usuario debe ser una cadena")

if minlen < 1:

raise ValueError("minlen debe ser al menos 1")


@@ -10,5 +11,8 @@

return False

if not nombredeusuario.isalnum():

return False

+ # Los nombres de usuario no pueden empezar por un número

+ if nombreusuario[0].isnumeric():

+ return False

return True
```

---

## Comparar archivos
- `diff` es un comando de Unix que compara dos archivos línea por línea y muestra las diferencias entre ellos.
    - El comando `diff` acepta dos archivos como argumentos y produce una salida que indica qué líneas son diferentes.
    - `<` indica que la línea proviene del primer archivo, mientras que `>` indica que la línea proviene del segundo archivo.
    - Tambien puede indicar el número de línea donde se encuentra la diferencia y el contenido de las líneas que difieren.
    - Ejemplo `5c5,6` significa que la línea 5 del primer archivo se reemplaza por las líneas 5 y 6 del segundo archivo.
    - `c` significa "cambiar"
    - `a` significa "añadir"
    - `d` significa "eliminar"
    - El comando `diff` tambien acepta el argumento `-u` para producir una salida unificada, que muestra las líneas que son iguales en ambos archivos, así como las líneas que difieren.
        - `-` indica que la línea proviene del primer archivo, mientras que `+` indica que la línea proviene del segundo archivo.
- `wdiff` es un comando que compara dos archivos palabra por palabra y muestra las diferencias entre ellos usando colores.
    - El comando `wdiff` acepta dos archivos como argumentos y produce una salida que indica qué palabras son diferentes.
    - Las palabras que se eliminan del primer archivo se muestran en rojo, mientras que las palabras que se agregan al segundo archivo se muestran en verde.

---

## Revisión: Aplicación de cambios
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
cat cpu_usage.py 
/usr/bin/env python3
import psutil

def comprobar_uso_cpu(porcentaje):
    usage = psutil.cpu_percent()

    return usage < porcentaje

if not comprobar_uso_cpu(75):
    print("¡ERROR! La CPU está sobrecargada")
else:
    print("Todo ok")
```
```bash
cat cpu_usage.diff 
```
```diff
--- cpu_usage.py 2019-06-23 08:16:04.666457429 -0700
+++ cpu_usage_fixed.py 2019-06-23 08:15:37.534370071 -0700

@@ -2,7 +2,8 @@
import psutil

def comprobar_uso_cpu(porciento):
-usage = psutil.cpu_percent()

+ usage = psutil.cpu_percent(1)
+ print("DEBUG: uso: {}".format(usage))
    return usage < porciento

if not comprobar_uso_cpu(75):
```