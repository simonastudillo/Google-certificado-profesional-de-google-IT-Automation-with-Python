# Cuando los problemas de lentitud se vuelven complejos

## Paralelización de operaciones
- En los scripts típicos mientras ​esta operación está en marcha, no sucede nada más
- El script está bloqueado, ​esperando la entrada o salida mientras la CPU está inactiva.
- Una forma en que podemos mejorar esto ​es hacer operaciones en paralelo. ​De esa manera, mientras la computadora está esperando la E/S lenta, ​puede tener lugar otro trabajo
- En realidad hay todo un campo de ​ciencias de la computación llamado `concurrency`, ​dedicado a cómo escribimos ​programas que realizan operaciones en paralelo. 
- Nuestro sistema operativo maneja los muchos procesos ​que se ejecutan en nuestro ordenador. ​Si un equipo tiene más de un núcleo, ​el sistema operativo puede decidir ​qué procesos se ejecutan en qué núcleo, ​y no importa la división entre núcleos, ​todos estos procesos se ejecutarán en paralelo.
- Cada uno de ellos tiene su propia asignación de memoria ​y hace sus propias llamadas de E/S. ​El sistema operativo decidirá qué fracción de ​tiempo de CPU ​obtiene cada proceso y cambiará entre ellos según sea necesario
- Por lo tanto, una forma muy fácil de ejecutar operaciones en ​paralelo es ​dividirlas en diferentes procesos, ​llamando a su script muchas ​veces cada uno con un conjunto de entrada diferente, ​y simplemente dejar que el sistema operativo maneje la concurrencia. 
- Supongamos que desea recopilar ​estadísticas sobre la carga actual ​y el uso de memoria para todos los equipos de su red. ​Puede hacerlo escribiendo un script que se conecte a ​cada equipo en una lista y obtenga las estadísticas. ​Cada conexión tarda un tiempo en completarse, ​por lo que el tiempo total de ejecución del script sería ​la suma del tiempo que toman todas esas conexiones. 
- En su lugar, podría dividir ​la lista de equipos en grupos más pequeños ​y usar el sistema operativo para llamar al script ​muchas veces una vez para cada grupo. 
- De esta manera, las conexiones a ​los diferentes equipos se pueden iniciar en paralelo, ​lo que minimiza el tiempo pero ​la CPU no está haciendo nada.
- ​Si tiene un proceso que está usando mucha ​CPU mientras que un proceso diferente está usando ​mucha E/S de red y ​otro proceso está usando mucha E/S de disco, ​todos estos pueden ejecutarse en ​paralelo sin interferir entre sí.
- Cuando se utiliza el sistema operativo para dividir el trabajo y los procesos, ​estos procesos no comparten ninguna memoria ​y, a veces, es posible que necesitemos tener algunos datos compartidos. ​En ese caso, usaríamos hilos (Threads).
- Los hilos nos permiten ejecutar tareas paralelas dentro de un proceso. ​Esto permite que los hilos compartan parte de ​la memoria con otros subprocesos en el mismo proceso. ​
- Para eso, necesitaremos ver ​cómo el lenguaje de programación ​que estamos usando implementa el threading. 
- En Python podemos usar el módulo `threading` o `asyncio` para crear hilos y ejecutar tareas en paralelo.
- Una cosa a tener en cuenta es que, dependiendo de ​la implementación real de subprocesos ​para el lenguaje que está usando, ​puede suceder que todos los subprocesos ​se ejecuten en el mismo procesador de CPU
- En ese caso, si desea usar más procesadores, ​deberá dividir el código ​en procesos completamente separados
- Si su script está en su mayoría esperando la entrada o salida, ​también conocido como enlace de E/S, ​puede importar si se ​ejecuta en un procesador u ocho.
- Si estamos tratando de leer un montón de archivos del ​disco y hacer demasiadas operaciones en paralelo, ​el disco podría terminar gastando más tiempo pasando de ​una posición a ​otra y recuperando realmente los datos.
- O si estamos haciendo un montón de ​operaciones que usan mucha CPU, ​el sistema operativo podría pasar más tiempo cambiando entre ellos ​que progresando ​en los cálculos que estamos tratando de hacer.
- ​Por lo tanto, al realizar operaciones en paralelo, ​necesitamos encontrar el equilibrio adecuado de ​acciones simultáneas que permitan que ​nuestros ordenadores permanezcan ocupados ​sin privar de recursos a nuestro sistema

---

## Crece lentamente en complejidad
- Es importante saber que tecnología es la mejor para el caso que necesitamos
- Por ejemplo si almacenamos datos de usuarios en un CSV, a medida que crece la cantidad de usuarios, el tiempo de búsqueda de un usuario específico crecerá linealmente.
- En estos casos podría ser mejor usar una base de datos como SQLite.
- Y a medida que crece, podría ser necesario usar una base de datos más robusta como PostgreSQL o MySQL.
- Incluso si tenemos una base de datos, a medida que crece la cantidad de usuarios, el tiempo de búsqueda de un usuario específico crecerá linealmente.
- En esos casos podemos evaluar el uso de caché, como Redis o Memcached, para almacenar los datos más utilizados y así reducir el tiempo de búsqueda.
- Por muy tentador que pueda ser, no debemos intentar usar una solución para miles de usuarios si actualmente solo tenemos unos pocos cientos.
- A medida que nuestro software crece, debemos evaluar si necesitamos cambiar la tecnología que estamos usando para manejar la carga de trabajo.

---

## Sistemas complejos y lentos
- En sistemas grandes y complejos, las tareas suelen estar separadas en diferentes procesos y servicios, que se comunican entre sí a través de la red.
- Por ejemplo un e-commerce tiene un servicio web, otro servidor para la base de datos, otro para reportes, backup, etc.