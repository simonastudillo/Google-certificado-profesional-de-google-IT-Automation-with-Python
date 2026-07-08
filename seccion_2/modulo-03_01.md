# Expresiones regulares

## Introducción al módulo 3: Expresiones regulares
- En este módulo, llevaremos ​nuestras capacidades de procesamiento de datos un paso más allá ​y aprenderemos sobre las expresiones regulares, ​que son una herramienta muy poderosa para agregar a su caja de herramientas de TI

---

## Qué es una expresión regular
- Una expresión regular (regex o regexp) es una secuencia de caracteres que define un patrón de búsqueda.
- Cuando se ejecuta una búsqueda en un fragmento de texto concreto, ​todo lo que coincida con un patrón de expresión regular especificado, ​se devuelve como resultado de la búsqueda
- Las expresiones regulares le permiten responder a preguntas como ¿cuáles son todas ​las palabras de cuatro letras en un archivo? ​¿ O cuántos tipos de error diferentes hay en este registro de errores?
- Las expresiones regulares se pueden usar en prácticamente cualquier lenguaje de programación, así como en muchos editores de texto y herramientas de línea de comandos.

---

## Reseña: Por qué usar expresiones regulares
- Los siguientes bloques de código se usarán en el próximo video:
```Python
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
```
- `r"\[(\d+)\]"`: El módulo `re` nos permite usar expresiones regulares en Python. 
- La expresión regular busca un patrón específico en el texto. En este caso, busca un número dentro de corchetes.
- `\[` y `\]` indican que estamos buscando los caracteres literales "[" y "]".
- `(\d+)` es un grupo de captura que busca uno o más dígitos

---

## Por qué usar expresiones regulares
- Las expresiones regulares son una herramienta poderosa para buscar y manipular texto.
- En el ejemplo anterior, usamos una expresión regular para extraer un número de un registro de log.
- Sin expresiones regulares, tendríamos que usar métodos más complicados y menos eficientes para lograr lo mismo como el uso de `index()` y `slice()`.
- Esto puede ser un problema si el `process id` cambia de longitud, ya que tendríamos que ajustar manualmente los índices de corte.
- Para mejorar y automatizar la búsqueda de patrones en el texto, las expresiones regulares son la mejor opción. 

---

## Coincidencia básica con grep
- Tambien podemos usar expresiones regulares en comandos de terminal como `grep` para buscar patrones en archivos de texto.
- `grep` es una herramienta de línea de comandos que busca patrones en archivos de texto y devuelve las líneas que coinciden con el patrón especificado.
- Probemos esto usando grep para encontrar palabras ​dentro del archivo /usr/share/dict/words, ​que es un archivo que ​algunos programas de revisión ortográfica usan para ​verificar si la palabra existe o no
- Buscamos la palabra `thon`: 
```bash
grep thon /usr/share/dict/words
```
- Obtenemos muchos resultados, tanto de palabras que comienzan con `thon` como de palabras que terminan con `thon`.
- `grep` es `case sensitive`, lo que significa que distingue entre mayúsculas y minúsculas. Para omitir esto usamos el parímetro `-i`:
```bash
grep -i python /usr/share/dict/words
``` 
- tenemos que conocer ​los caracteres reservados que dan ​un significado extra a los patrones que creamos
    - `.` Coincide con cualquier carácter excepto un salto de línea.
```bash
grep l.rts /usr/share/dict/words
# alerts
# blurts
# flirts
```
    - `^` Coincide con el inicio de una línea.
```bash
grep ^fruit /usr/share/dict/words
# fruit
# fruitful
# fruitless
```
    - `$` Coincide con el final de una línea.
```bash
grep cat$ /usr/share/dict/words
# bobcat
# wildcat
# tomcat
```