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