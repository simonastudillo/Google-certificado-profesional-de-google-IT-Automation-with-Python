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

---

## Tu propio módulo Python
- Es común reutilizar código que escribimos en otros proyectos, para ello podemos crear nuestros propios módulos de Python.
- Debemos evitar duplicar código, ya que si el código está repetido 3 veces, cualquier cambio que hagamos en el código, debemos hacerlo en 3 lugares diferentes, lo que aumenta la probabilidad de errores y hace más difícil mantener el código.
- Para aislar ese código y poder reutilizarlo, podemos crear un módulo de Python.
- Esto es simple, el código repetido debe quedar en un archivo separado
- Luego para utilizarlo debemos importarlo en el archivo donde lo necesitamos, para ello usamos la palabra reservada `import` seguida del nombre del archivo sin la extensión `.py`.
- Para que una carpeta sea reconocida como un paquete de Python, debemos crear un archivo llamado `__init__.py` dentro de la carpeta.
- Este archivo puede estar vacío, pero su presencia indica a Python que la carpeta debe ser tratada como un paquete.

---

## Que es un IDE?
- Cada IDE (Integrated Development Environment) es un entorno de desarrollo que nos permite escribir, ejecutar y depurar nuestro código de manera más eficiente.
- Tienen funciones diferentes como resaltado de sintaxis, autocompletado de código, depuración paso a paso, integración con sistemas de control de versiones y muchas otras características que facilitan el desarrollo de software.
- Vim: Es un editor de texto muy potente y flexible, pero puede ser difícil de aprender para los principiantes debido a su interfaz basada en comandos.
- Atom: Es un editor de texto moderno y personalizable, desarrollado por GitHub. Tiene una interfaz amigable y muchas extensiones disponibles para mejorar la productividad.
- Es importante que aprendamos a usar un IDE de terminal, podría ser útil para trabajar en servidores remotos donde no tenemos acceso a un entorno gráfico.

---

## Configurando su entorno
- Editores comúnes para Python
    - [Eclipse](http://www.eclipse.org/)
    - [PyCharm](https://www.jetbrains.com/pycharm/)
    - [Sublime Text](http://www.sublimetext.com/)
    - [Visual Studio Code](https://code.visualstudio.com/)