# Introducción a la depuración

## Introducción al Módulo 1: Conceptos de resolución de problemas
- Debemos asegurarnos de que las personas afectadas por el problema ​puedan volver a hacer su trabajo lo más rápido posible
- También tenemos que planificar cómo ​evitar que los mismos problemas ​vuelvan a ocurrir en el futuro
- Las técnicas que analizaremos son ​reutilizables y te permitiremos resolver ​casi cualquier problema técnico ​que puedas enfrentar en el futuro
- Encontrar la solución a un problema ​a veces puede llevar mucho tiempo.

---

## ¿Qué es la depuración?
- Depuración y solución de problemas:
    - `Troubleshooting` (solución de problemas): es el proceso de encontrar y resolver problemas en un sistema informático. Pueden ser problemas causados por el hardware, el sistema operativo o ​las aplicaciones que se ejecutan en el equipo. ​También podrían ser causados por el entorno y la ​configuración del software. 
    - `Debugging` (depuración): es el proceso de encontrar y corregir errores en un programa de software. 
- `tcpdump` y `wireshark` son herramientas de depuración de red que permiten capturar y analizar el tráfico de red.
- `ps`, `top` y `free` son herramientas de depuración de procesos y memoria que permiten ver qué procesos se están ejecutando y cuánta memoria están utilizando.
- `strace` es una herramienta de depuración de procesos que permite ver qué llamadas al sistema está haciendo un proceso y qué archivos está abriendo.
- `ltrace` es una herramienta de depuración de procesos que permite ver qué bibliotecas compartidas está utilizando un proceso y qué funciones está llamando.
- `Debuggers` son herramientas de depuración de programas que permiten ejecutar un programa paso a paso y ver qué está haciendo en cada momento. 
- Si podemos modificar el código fuente de un programa, podemos agregar instrucciones de depuración para imprimir información sobre lo que está haciendo el programa en un momento dado. Esto puede ayudarnos a encontrar errores en el código.
- Generalmente, descubrir el problema y su solución requiere algo de creatividad. ​Tenemos que idear nuevas ideas sobre lo que podría estar fallando, y ​maneras de comprobarlo. ​Y una vez que sepamos lo que está fallando, tenemos que imaginar cómo resolverlo.

---

## Pasos para la resolución de problemas
1. Obtener información: Esto significa reunir toda la información ​que necesitamos sobre el estado actual de las cosas, ​cuál es el problema, cuándo ocurre ​y cuáles son las consecuencias. Esto puede ser documentación interna, registros de errores, mensajes de error, capturas de pantalla, etc.
2. Reproducir el problema: Esto significa intentar hacer que el problema ocurra de nuevo, para que podamos observarlo y entenderlo mejor.
3. Encontrar la raíz del problema: Entender que causa el problema y como podemos cambiar eso.
4. Corrección del problema: Esto puede ser una solución inmediata para que el sistema vuelva a funcionar, una correción a medio o largo plazo para que el problema no vuelva a ocurrir, o una combinación de ambas.

- Es común que al ir adentrandonos en la resolución de problemas, tengamos que volver a los pasos anteriores para obtener más información, reproducir el problema de una manera diferente o encontrar una nueva causa raíz.
- Es importante documentar todo el proceso de resolución de problemas, para que podamos aprender de nuestros errores y mejorar nuestras habilidades de depuración.

---

## Aplicación que se bloquea silenciosamente
- Supongamos que un usuario se pone en contacto con nosotros para informarnos de que una determinada aplicación no se ​abre.
1. Obtener información: Debemos averiguar las condiciones que causaron la falla, cuál es el error que está recibiendo el usuario y reproducir el problema en nuestro propio entorno.
    1. Al solcitar la información se detecta que hubo una actualización recientemente
    2. Podemos reproducir el error ejecutando la aplicación Python `./archivo.py`
    3. Obtenemos más información ejecutando `strace ./archivo.py`
    4. Podemos guardar el log de strace añadiendo el flag `-o`: `strace -o log.txt ./archivo.py`
    5. Al leer el log se detecta error al abrir un directorio usando `openat(AT_FDCWD, "directorio", O_RDONLY|O_NONBLOCK|O_CLOEXEC) = -1 ENOENT (No such file or directory)`
        1. El indicador de directorio 0 nos indica que el programa está intentando ​abrir esta ruta como un directorio.
        2. El número después del signo igual nos muestra el código de retorno de la llamada al sistema.
        3. ​En este caso es negativo.
        4. Así que el programa está intentando abrir este directorio y resulta que no ​existe. Dado que esto ocurre poco antes de que finalice el programa, ​es probable que sea la causa principal del problema.
2. Reproducir el problema: Ya hemos reproducido el problema en nuestro propio entorno, así que podemos pasar al siguiente paso.
3. Creemos que la causa raíz del problema es que el programa está intentando abrir un directorio que no existe. Esto se puede solucionar creando el directorio, podemos hacer una prueba para ver si eso resuelve el problema. Al crear el directorio y ejecutar de nuevo el programa, vemos que ahora funciona correctamente.
4. Podemos decirle al usuario que cree el directorio que falta y que vuelva a ejecutar la aplicación, tambien podemos hablar con los desarrolladores para que modifiquen el programa para que cree el directorio si no existe, o para que muestre un mensaje de error más útil.
5. Documentamos el proceso de resolución de problemas, incluyendo la información que obtuvimos, cómo reproducimos el problema, cuál fue la causa raíz y cómo lo solucionamos, de esta forma los demás usuarios podrán aprender de nuestra experiencia y evitar problemas similares en el futuro.


>[!INFO]
> System calls: Son las llamadas que los programas que se ejecutan en nuestro ordenador hacen al núcleo en ejecución.

---

## Test your knowledge: Introduction to debugging
1. What is part of the final step when problem solving?
> Long-term remediation

2. Which tool can you use when debugging to look at library calls made by the software?
> ltrace

3. What is the first step of problem solving?
> Gather information

4. What software tools are used to analyze network traffic to isolate problems? (Check all that apply)
> tcpdump
> wireshark

5. The strace (in Linux) tool allows us to see all of the _____ our program has made.
> system calls