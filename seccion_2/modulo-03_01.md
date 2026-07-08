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