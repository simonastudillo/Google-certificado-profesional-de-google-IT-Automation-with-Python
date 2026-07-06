# Ejecutando Python localmente

## Lenguaje Interpretado vs Compilado
- El lenguaje interpretado es aquel que se ejecuta línea por línea, mientras que el lenguaje compilado se traduce a código máquina antes de su ejecución.
- Esto hace los lenguajes compilados más rápidos en tiempo de ejecución, pero lentos en el proceso de desarrollo, ya que requiere un tiempo de compilación antes de ejecutar el programa.
- Existen lenguajes como C y Java con un efoque mixto, esto permite rapidéz pero deben compilarse teniendo en cuenta el sistema operativo y la arquitectura de la máquina donde se ejecutará el programa.
- Los lenguajes interpretados como Python, permiten ejecutar el código directamente sin necesidad de compilarlo, lo que facilita el desarrollo y la depuración del código.

---

## Como ejecutar un Script de Python
- Recuerda que usaremos Python 3, por lo que debemos usar el comando `python3` para ejecutar nuestros scripts.
- Los archivos Python tienen la extensión `.py`.
- Para ver el contenido de un archivo Python, podemos usar el comando `cat <nombre_del_archivo>.py` en la terminal.
- para ejecutar el archivo ejecuta `python3 <nombre_del_archivo>.py` en la terminal.
- Podemos indicar en el archivo que queremos siempre usar Python 3 agregando la siguiente línea al inicio del archivo:
```Python
#!/usr/bin/env python3
```
- Debemos revisar y asegurarnos que el archivo tiene permisos de ejecución, para ello ejecutamos el comando `chmod +x <nombre_del_archivo>.py` en la terminal.
- Ahora podemos ejecutarlo directamente con el comando `./<nombre_del_archivo>.py` en la terminal.