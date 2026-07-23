# Lentitud

## Introducción al Módulo 2: Lentitud
- Un problema con el que tenemos que lidiar mucho cuando trabajamos en TI, es que las cosas son lentas.
- Esto podría ser nuestro ordenador, nuestros scripts, o incluso sistemas complejos. 
- Con las computadoras de hoy en día puede parecer que nuestros recursos son ilimitados, ​pero si nos esforzamos lo suficiente podemos alcanzar los límites.
- Hay un montón de cosas diferentes que podemos hacer si nuestro sistema es demasiado lento. ​La más obvia es cerrar cualquier aplicación que no necesitemos en este momento

---

## ¿Por qué va lento mi ordenador?
- Aún con miles de millones ​de instrucciones por segundo, ​hay muchas cosas que una computadora puede hacer en solo un segundo. ​
- Esto permite a nuestro ordenador ejecutar aparentemente ​una serie de cosas diferentes al mismo tiempo.
- Incluso si su computadora tiene ​un solo núcleo para ejecutar esas aplicaciones, ​parecerá que el equipo está ejecutando ​estos dos programas al mismo tiempo. ​
- Lo que está sucediendo bajo el capó es que ​cada aplicación obtiene una fracción del tiempo de CPU, ​y luego la siguiente aplicación obtiene un giro. 
- La mayoría de las veces esto funciona bien. ​Pero si ejecuta demasiadas aplicaciones o si una de ​estas aplicaciones se estaba ejecutando necesita ​más tiempo de CPU que la fracción que recibe, ​las cosas podrían volverse frustrantemente lentas. 
- La estrategia general para abordar la lentitud es identificar los `bottlenecks` (cuellos de botella) y luego tratar de eliminarlos.
- Ejemplos de cuellos de botella incluyen:
  - Un disco duro lento
  - Una CPU lenta
  - Una red lenta
  - Un programa que está usando demasiada memoria
- ¿ Qué pasa si el hardware que estamos usando no es ​lo suficientemente bueno para las aplicaciones que intentamos ejecutar en él? ​En casos como estos, ​tendrá que actualizar el hardware subyacente
- Pero para marcar la diferencia en el rendimiento resultante, ​tenemos que asegurarnos de que realmente estamos mejorando ​el cuello de botella y no solo desperdiciando ​nuestro dinero en hardware nuevo que no se utilizará. 
- En linux podemos usar el comando `top` para ver qué procesos están usando más recursos de CPU y memoria.
- En MacOS podemos usar el Monitor de Actividad para ver qué procesos están usando más recursos de CPU y memoria.
- En Windows podemos usar el Administrador de tareas para ver qué procesos están usando más recursos de CPU y memoria.

---

## Cómo utilizan los ordenadores los recursos
- cuando se piensa en hacer las cosas más rápidas, ​es importante comprender ​las diferentes velocidades de las piezas involucradas. ​
- Cuando una aplicación está accediendo a algunos datos, ​el tiempo dedicado a recuperar ​esos datos dependerá de dónde se encuentren.
- Si se trata de una variable que ​se está utilizando actualmente en una función, ​los datos estarán en la memoria interna de la CPU, ​y nuestro programa lo recuperará muy rápido. ​
- Si los datos están relacionados con un programa en ejecución, ​pero tal vez no con la función que se está ejecutando actualmente, ​es probable que esté en RAM, ​y nuestro programa todavía llegará a un bastante rápido.
- ​Si los datos están en un archivo, ​nuestro programa tendrá que leerlo desde el disco, ​que es mucho más lento que leerlo desde la RAM, ​y peor que leer desde el disco, ​es leer información desde la red. ​
- En este caso, tenemos una velocidad de transmisión más baja, ​y también necesitamos establecer la conexión con ​el otro punto final para hacer posible la transmisión, ​lo que aumenta el tiempo total necesario para llegar a los datos.
- una caché almacena datos en un formulario que es ​más rápido de acceder que su forma original.
- ecimos que estos contenidos se almacenan en caché en la memoria. ​Lo llamamos que si los datos ​son parte de un programa que ​se está ejecutando actualmente, estarán en RAM.
- Pero la RAM es limitada. ​Si ejecuta suficientes programas al mismo tiempo, ​lo llenará y se quedará sin espacio. ​
- ¿ Qué sucede cuando te quedas sin RAM? ​Al principio, el sistema operativo simplemente ​eliminará de la RAM todo lo que esté almacenado en caché, ​pero no estrictamente necesario. ​Si todavía no hay suficiente RAM después de eso, ​el sistema operativo pondrá ​las partes de la memoria que no están ​en uso actualmente en ​el disco duro en un espacio llamado swap. 
- Leer y escribir desde el disco es ​mucho más lento que leer y escribir desde la RAM. ​Por lo tanto, cuando ​una aplicación solicita la memoria intercambiada, ​tardará un tiempo en cargarla de nuevo. ​
- La información que no se necesita en este momento se ​elimina de la RAM y se coloca en el disco, ​mientras que la información que se necesita ahora se coloca en la RAM. 
- ¿qué haces si encuentras que tu máquina es ​lenta porque está pasando mucho tiempo intercambiando?
- Primero, si hay ​demasiadas aplicaciones abiertas y algunas se pueden ​cerrar, cierre las que no sean necesarias.
- Segundo, si la memoria disponible es ​demasiado pequeña para la cantidad que utiliza el equipo, ​agregue más RAM al equipo
- Tercero, uno de ​los programas en ejecución puede tener una pérdida de memoria, ​lo que hace que tome toda la memoria disponible. 
- Una pérdida de memoria significa que la memoria que ​ya no se necesita no se libera. 