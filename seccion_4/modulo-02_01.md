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

---

## Posibles causas de la lentitud
- Primero buscamos ​las explicaciones más simples que sean las más fáciles de verificar.
- después de eliminar una posible causa raíz, ​volvemos al problema y encontramos la siguiente causa posible para verificar.
- Por lo tanto, al tratar de averiguar qué está haciendo que una computadora sea lenta, ​el primer paso es examinar cuándo la computadora es lenta. 
- Si es lento al iniciar, probablemente sea una señal de que hay ​demasiadas aplicaciones configuradas para iniciarse en el arranque. ​En este caso, solucionar el problema es solo una cuestión de revisar la lista de ​programas que se inician automáticamente y deshabilitar los que realmente no son necesarios
- Si en su lugar el equipo se vuelve lento después de días de funcionar bien, y ​el problema desaparece con un reinicio, significa que hay un programa que ​mantiene algún estado mientras se ejecuta que está haciendo que el equipo se ralentice.
- Si no tiene acceso al código, otra opción es programar un ​reinicio regular para mitigar tanto el programa lento como el equipo que se queda sin RAM.
- Un problema similar que puede desencadenarse después de mucho tiempo usando una aplicación, ​y que no se resuelve mediante un reinicio, ​es que los archivos que una aplicación está manejando han crecido demasiado. ​
- Si el archivo es un archivo de registro, puede usar un programa como logrotate para hacer esto por usted.
- `Logrotate` es un programa que puede rotar, comprimir y eliminar archivos de registro automáticamente. ​
- Si el disco duro tiene errores, es posible que el equipo pueda aplicar la ​corrección de errores para obtener los datos que necesita, ​pero afectará al rendimiento general. 
- ​Otra fuente de lentitud es el software malicioso. ​
- siempre queremos mantener su equipo limpio de cualquier software malicioso, ​pero podemos sentir los efectos del software malicioso incluso si no está instalado. ​
- Por ejemplo, podría haber encontrado un sitio web que incluye scripts, ​ya sea en el contenido del sitio web o en ​los anuncios mostrados, que utilizan nuestro procesador para extraer criptomonedas. ​

---

## Servidor web lento
- Comencemos navegando ​al sitio web y cargando la página.
- Parece ser un poco lento ​, pero es difícil medir esto por nuestra cuenta
- Vamos a utilizar una herramienta llamada ab que significa ​herramienta Apache Benchmark para averiguar lo lento que es. 
- Ejecutaremos `ab -n ​500 <site>` para obtener el tiempo promedio de 500 solicitudes, ​y luego pasaremos nuestro sitio.example.com para la medición. 
- Esta herramienta es muy útil para comprobar si ​un sitio web se comporta como se esperaba o no.
- Hará un montón de solicitudes ​y resumirá los resultados una vez que esté hecho.
- Vemos que el tiempo medio por ​solicitudes fue de 155 milisegundos.
- Si bien este no es un número súper enorme, ​definitivamente es más de lo que ​esperaríamos para un sitio web tan simple.
- Parece que algo está pasando con ​el servidor web y tenemos que investigar más a fondo. 
- Empezaremos por mirar la salida de ​top y ver si hay algo sospechoso allí.
- Vemos que hay un montón de procesos `ffmpeg` en ejecución, ​que básicamente están usando toda la CPU disponible.
- Recuerde que el promedio de carga en ​Linux muestra cuánto tiempo está ​ocupado el procesador en un minuto determinado, ​lo que significa que estuvo ocupado durante todo el minuto
- Este equipo tiene dos procesadores. ​Así que cualquier número por encima de dos significa que está sobrecargado. ​
- Este programa ffmpeg se utiliza para la ​transcodificación de vídeo, lo que significa ​convertir archivos de un formato de vídeo a otro.
- Una cosa que podemos intentar es cambiar las ​prioridades de los procesos para que el servidor web tenga prioridad.
- Las prioridades del proceso en Linux ​son para que cuanto menor sea el número, ​mayor será la prioridad. ​Los números típicos van de 0 a 19
- vamos a utilizar el comando pidof que recibe ​el nombre del proceso y devuelve ​todos los ID de proceso que tienen ese nombre. ​Vamos a iterar sobre la salida del comando pidof con un ​bucle for y luego llamar a ​renice para cada uno de los ID de proceso. ​Renice toma la nueva prioridad como primer argumento, ​y el ID de proceso para cambiar como el segundo. 
```bash
for pid in $(pidof ffmpeg); do renice 19 $pid; done
```
- Esto cambiará la prioridad de todos los procesos ffmpeg a 19, lo que significa que tendrán la prioridad más baja posible. ​
- Esta vez, mientras tanto es de 153 milisegundos. ​No parece que nuestro Renice haya ayudado. ​Aparentemente, el sistema operativo todavía está dando a ​estos procesos ffmpeg demasiado tiempo del procesador.
- Así que una cosa que podríamos hacer es ​modificar lo que sea que los esté activando para ejecutarlos ​uno tras otro en lugar de todo al mismo tiempo. ​Para hacer eso, necesitaremos ​averiguar cómo se iniciaron estos procesos. 
- Primero, veremos la salida ​del comando `ps` para obtener ​más información sobre los procesos.
- ​Llamaremos a `ps ax` que ​nos muestra todos los procesos en ejecución en el ordenador, ​y conectaremos la salida del comando con `less`, ​para poder desplazarnos por él:
```bash
ps ax | less
```
- Luego podemos buscar ffmpeg escribiendo `/ffmpeg` y presionando enter. ​Esto nos llevará a la primera línea que contiene ffmpeg. ​
- Vemos que hay un montón ​de procesos ffmpeg que ​están convirtiendo videos ​del formato webm al formato mp4. 
- No sabemos dónde están estos videos en el disco duro. ​Podemos intentar usar ​el comando de `locate` para ver si podemos encontrarlos
```bash
locate static/001.webm
```
- Luego podemos usar el comando `grep ffmpeg *` para ver si podemos encontrar el archivo de registro que contiene la salida de ffmpeg. ​ 
- Vemos que este script está iniciando ​los procesos ffmpeg en paralelo ​usando una herramienta llamada Daemonize que ​ejecuta cada programa por separado como si fuera un demonio. 
- Esto podría estar bien si solo ​necesitamos convertir un par de videos, pero ​lanzar un proceso separado para cada uno de los ​videos en el directorio estático ​está sobrecargando nuestro servidor.
- Por lo tanto, queremos cambiar esto para ejecutar ​solo un proceso de conversión de vídeo a la vez
- Lo haremos simplemente eliminando ​la parte daemonizada y manteniendo ​la parte que llama ffmpeg
- Pero esto no cambiará los ​procesos que ya se están ejecutando. 
- Queremos detener estos procesos ​pero no cancelarlos por completo, ​ya que hacerlo significaría que los vídeos que se están ​convirtiendo en este momento estarán incompletos.
- Así que usaremos el comando killall con ​el indicador -STOP que envía ​una señal de parada pero no mata los procesos por completo.
```bash
killall -STOP ffmpeg
```
- Ahora queremos ejecutar estos procesos ​uno a la vez. ¿Cómo podemos hacer eso? ​Podríamos enviar la señal CONT a uno de ellos, ​esperar hasta que esté hecho, ​y luego enviarla a la siguiente. ​Pero eso es mucho trabajo manual. ​¿ Se puede automatizar? Sí. Pero es un poco complicado. 
- Podemos iterar a través de la lista de procesos usando el ​mismo bucle for con el pit ​of command que usamos anteriormente.
- Dentro del bucle for, ​queremos enviar la señal cont y ​luego esperar hasta que finalice el proceso. 
- Desafortunadamente, no hay ningún comando ​que esperar hasta que finalice el proceso. ​Pero podemos crear un bucle while que ​envíe la señal cont al proceso. ​Esto tendrá éxito mientras el proceso exista, ​y falla una vez que el proceso desaparezca. ​Dentro de este bucle while, ​simplemente agregaremos una llamada para dormir una, ​para esperar un segundo hasta la siguiente comprobación. 
```bash
for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done
```
- El tiempo medio es ahora de 33 milisegundos. ​Eso es mucho más bajo que antes.