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

---

## Entornos virtuales
- Un entorno virtual en Python es una herramienta poderosa que permite crear entornos aislados para tus proyectos
- Esto significa que puedes tener varios proyectos con diferentes dependencias, asegurándote de que no interfieran entre sí
- En esencia, los entornos virtuales proporcionan un lienzo en blanco donde puedes trabajar en tus proyectos sin preocuparte por bibliotecas o versiones conflictivas
- ¿Por qué utilizar un entorno virtual en Python?
    - Imagina que trabajas en dos proyectos de Python distintos: uno requiere una versión específica de una biblioteca, mientras que el otro depende de una versión más reciente
    - permiten mantener los proyectos aislados, garantizando que los cambios en un entorno no afecten al otro.
    - Evita conflictos entre bibliotecas y dependencias.
    - Prueba diferentes versiones de bibliotecas sin afectar la instalación de Python en todo el sistema.
    - Mantén un entorno de desarrollo limpio y organizado.
    - Colabora con otros, asegurando la coherencia en las versiones de las bibliotecas.
- Utilizando un entorno virtual de Python
    - Para crear un entorno virtual, abre la terminal y navega hasta el directorio de tu proyecto. Luego, ejecuta el siguiente comando:
    - `python -m venv myenv`
    - Esto creará un directorio llamado `myenv` que contendrá una copia aislada del intérprete de Python y las bibliotecas necesarias.
    - Para activar el entorno virtual, ejecuta el siguiente comando:
    - En Windows: `myenv\Scripts\activate`
    - En macOS y Linux: `source myenv/bin/activate`
    - Una vez activado, el indicador de la terminal cambiará, indicando que ahora estás trabajando dentro del entorno virtual
    - Ahora puedes instalar paquetes usando pip como lo harías normalmente.
- Buenas prácticas y recomendaciones
    - Crea un entorno virtual para cada proyecto: Siempre que inicies un nuevo proyecto, crea un nuevo entorno virtual. Esto garantiza un espacio de trabajo limpio y aislado.
    - Usa archivos de requisitos: Para documentar y gestionar las dependencias de tu proyecto, crea un archivo requirements.txt. Este archivo enumera todas las bibliotecas y sus versiones. Puedes generarlo con `pip freeze > requirements.txt` y luego instalarlas en un nuevo entorno con `pip install -r requirements.txt`.
    - Activa y desactiva: Activa siempre el entorno virtual adecuado antes de trabajar en un proyecto y desactívalo cuando termines. Esto evita confusiones y posibles conflictos.
    - Control de versiones: Si colaboras con otros, incluye las instrucciones de configuración del entorno virtual en tu sistema de control de versiones. Esto garantiza que todos utilicen el mismo entorno.
    - Actualiza pip y setuptools: Cuando crees un nuevo entorno virtual, es recomendable actualizar pip y setuptools a la última versión. Esto garantiza que estés utilizando las herramientas más actualizadas.

---

## Test your knowledge: Running Python locally
1. When your IDE automatically creates an indent for you, this is known as what?
> Code completion

2. Can you identify the error in the following code?
```Python
#!/usr/bin/env python3
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())
```
> The y variable is not calling the numpy module properly.

3. Which type of programming language is read and converted to machine code before runtime, allowing for more efficient code?
> Compiled language

4. Which of the following is not an IDE or code editor?
> pip

5. What does the PATH variable do?
> Tells the operating system where to find executables