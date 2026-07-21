# Entender el problema

## "No funciona"
- Cuando se trabaja con usuarios, ​es bastante común recibir informes de fallas ​que simplemente se reducen a: «No funciona». 
- Qué información es útil o ​no puede depender del problema
- Preguntas útiles:
    - ¿ Qué intentabas hacer?
    - ​¿ Qué pasos seguiste?
    - ¿ Cuál fue el resultado esperado?
    - ¿ Cuál fue el resultado real?
- Debemos considerar ​primero las explicaciones más simples y evitar ​saltar a soluciones complejas o que consumen mucho tiempo ​a menos que realmente tengamos que hacerlo
- Debemos identificar los pasos que permitan eliminar la mayor cantidad de causas posibles del problema, para poder centrarnos en la causa raíz.
- Es importante que antes de comenzar a intentar resolver el problema, nos aseguremos de que entendemos lo que el usuario estaba intentando hacer y cuál era el resultado esperado. Esto nos ayudará a identificar la causa raíz del problema y a encontrar una solución más rápidamente.

---

## Creación de una caja de reproducción
- `Reproduction case`: Es una forma de verificar si el problema está presente o no, y de aislar la causa raíz del problema.
- Hay casos donde el problema no se puede reproducir, y en esos casos debemos recopilar toda la información posible sobre el entorno del usuario y las condiciones en las que ocurrió el problema.
- Esto se logra mirando los registros: pueden ser de accesos, errores o de eventos, dependiendo del tipo de problema que estemos tratando de resolver.
- Directorios de errores:
    - Linux: /var/log/
    - MacOS: /Library/Logs/
    - Windows: Event Viewer
- Muchas veces los logs contienen información útil sobre el problema, como mensajes de error, advertencias o información sobre el estado del sistema en el momento en que ocurrió el problema.

---

## Encontrar la causa
- Entender la causa raíz del problema es escencial para poder encontrar una solución efectiva de largo plazo.
- Debemos generar una teoría sobre lo que podría estar causando el problema y luego probar esa teoría para ver si es correcta.
- En caso de que la teoría no sea correcta, debemos generar una nueva teoría y probarla nuevamente.
- Siempre que sea posible, debemos probar nuestras teorías en un entorno de prueba antes de aplicarlas en el entorno de producción, para evitar causar más problemas.
- `iotop`: Es una herramienta de depuración de procesos y memoria que permite ver qué procesos están utilizando más recursos del sistema, como CPU, memoria o disco. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en el sistema.
- `iostat`: Es una herramienta de depuración de procesos y memoria que permite ver qué procesos están utilizando más recursos del sistema, como CPU, memoria o disco. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en el sistema.
- `vmstat`: Es una herramienta de depuración de procesos y memoria que permite ver qué procesos están utilizando más recursos del sistema, como CPU, memoria o disco. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en el sistema.
- `iftop`: Es una herramienta de depuración de red que permite ver qué procesos están utilizando más ancho de banda de red. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en la red.
- `rsync`: Es una herramienta para sincronizar archivos y directorios entre dos ubicaciones. Podemos usar el flag `-bwlimit` para limitar el ancho de banda utilizado por `rsync`, lo que puede ayudarnos a evitar problemas de rendimiento o bloqueos en la red.
- `nice`: Es una herramienta que permite cambiar la prioridad de un proceso en ejecución. Podemos usar `nice` para aumentar o disminuir la prioridad de un proceso, lo que puede ayudarnos a evitar problemas de rendimiento o bloqueos en el sistema.