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
- Por eso siempre es importante detectar los cuellos de botella y optimizar el sistema para que funcione de manera eficiente.

---

## Utilizar hilos para acelerar las cosas
- Ejemplo
    - Debemos procesar cientos de imagenes para generar miniaturas y guardarlas en un disco.
    - Usando el comando `time` podemos medir el tiempo que tarda en procesar todas las imágenes.
    - Se detecta un tiempo de 2s, lo cual es demasiado lento.
    - Usaremos el módulo `concurrent.futures` para crear un `ThreadPoolExecutor` y procesar las imágenes en paralelo. 
    - `Executor` es una clase que nos permite ejecutar tareas en paralelo utilizando hilos o procesos.
    - `Futures modules` es un módulo que nos permite ejecutar tareas en paralelo y obtener los resultados de manera asíncrona.
    - Debemos crear un executor `executor = ThreadPoolExecutor()` 
    - Luego le indicamos que proceso enviar al thread pool con los parámetros que necesite `executor.submit(process_file, root, basename)`
    - Finalmente usamos `executor.shutdown(wait=True)` para esperar a que todos los hilos terminen antes de continuar con el script.
    - Ejecutamos una prueba con time y el script ahora demora 1.2s, lo cual es mucho mejor que los 2s iniciales.
    - Otra forma es usar `ProcessPool` esto nos permite ejecutar tareas en paralelo utilizando procesos en lugar de hilos, lo cual es útil cuando tenemos tareas que consumen mucha CPU.
    - Debemos crear un executor `executor = ProcessPoolExecutor()`, el resto del código es igual al ejemplo anterior.
    - Ejecutamos una prueba con time y el script ahora demora 0.9s, lo cual es mucho mejor que los 2s iniciales.
    - La diferencia es causada por la forma en que los hilos y procesos funcionan en Python. Los ​subprocesos usan un montón de características de seguridad para evitar tener dos hilos que intentan ​escribir en la misma variable. ​Y esto significa que al usar hilos, pueden terminar esperando ​su turno para escribir en variables durante unos milisegundos, lo ​que suma la pequeña diferencia entre los dos enfoques.

---

## Más sobre sistemas complejos lentos
- Concurrencia
    - En Python, puedes utilizar la concurrencia para permitir que varias tareas progresen al mismo tiempo, incluso si no se ejecutan simultáneamente
    - Esto es útil especialmente para las tareas de E/S.
    - La concurrencia te permite gestionar eficientemente estas tareas, asegurando que pueden avanzar sin problemas y sin ser frenadas por otras tareas.
- Paralelismo
    - Implica ejecutar múltiples procesadores o núcleos de CPU al mismo tiempo
    - Esto es ideal para tareas que hacen un uso intensivo de la CPU
    - Al dividir el trabajo entre varios núcleos, el paralelismo puede acelerar significativamente estas tareas y reducir el tiempo de procesamiento.
- Concurrencia para tareas de E/S
    - Python tiene dos enfoques principales para implementar la concurrencia: threading y asyncio.
    1. Threading es un método eficiente para solapar tiempos de espera. Es adecuado para tareas que implican muchas operaciones de E/S, como la E/S de archivos o las operaciones de red que pasan mucho tiempo esperando, hay algunas limitaciones con el threading en Python debido al Global Interpreter Lock (GIL), que puede limitar la utilización de múltiples núcleos.
    2. Asyncio proporciona un mayor grado de control, escalabilidad y potencia que los hilos para tareas vinculadas a E/S. Cualquier aplicación que implique la lectura y escritura de datos puede beneficiarse de ello, ya que acelera los programas basados en E/S. Además, asyncio opera de forma cooperativa y evita las limitaciones de GIL, lo que permite un mejor rendimiento para las tareas de E/S.
- Paralelismo para tareas vinculadas a la CPU
    - Es especialmente útil para tareas ligadas a la CPU como cálculos, simulaciones y procesamiento de datos.
    - En lugar de intercalar y ejecutar tareas de forma concurrente, el paralelismo permite que varias tareas se ejecuten simultáneamente en varios núcleos de la CPU. 
    - Garantiza el rendimiento proporcionando a cada proceso su propio intérprete de Python y espacio de memoria.
    - Permite a los programas Python vinculados a la CPU procesar datos de forma más eficiente al dar a cada proceso su propio intérprete Python y espacio de memoria; esto elimina conflictos y ralentizaciones causadas por compartir recursos.
    - Dicho esto, también debes recordar que cuando se ejecutan varias tareas simultáneamente, es necesario gestionar los recursos con cuidado.
- Combinar concurrencia y paralelismo
    - La combinación de concurrencia y paralelismo puede mejorar el rendimiento. En ciertas aplicaciones complejas con tareas tanto de E/S como de CPU, puedes utilizar asyncio para la concurrencia y multiprocesamiento para el paralelismo.
    - Con asyncio, las tareas de E/S son más eficientes, ya que el programa puede hacer otras cosas mientras espera las operaciones de archivo.
    - Por otro lado, el multiprocesamiento permite distribuir los cálculos ligados a la CPU, como los cálculos pesados, entre varios procesadores para una ejecución más rápida.
    - Combinando estas técnicas, puedes crear un programa bien optimizado y con capacidad de respuesta. Las tareas de E/S se benefician de la concurrencia, mientras que las de CPU aprovechan el paralelismo.
- Selección del enfoque adecuado
    - Antes de desarrollar su programa, es esencial determinar si desea incorporar la concurrencia, ya que generalmente es más fácil añadirla posteriormente que eliminarla.
    - Para tomar esta decisión, debe comprender las tareas que debe realizar su aplicación. Su enfoque dependerá de si su programa está ligado a la CPU (procesamiento) o a la E/S (comunicación).
    - Cuando necesites esperar por recursos externos, la concurrencia con asyncio o threading sería más apropiada. Aprovechar los tiempos muertos durante las operaciones de E/S permite a tu programa manejar múltiples tareas concurrentemente.
    - Por otro lado, si se trata de tareas que requieren un uso intensivo de la CPU, como la compresión, la renderización de vídeos de alta definición o la ejecución de simulaciones complejas, el multiprocesamiento es una buena opción. 
- Eventos asyncio y bucles de tareas
    - La librería asyncio de Python permite la ejecución concurrente de múltiples tareas a través de operaciones asíncronas utilizando bucles de eventos y coroutines
    - Una coroutine puede pausar la ejecución mientras espera una operación específica, como leer o guardar datos
    - Los bucles de eventos son esenciales para programar y gestionar tareas, permitiendo una ejecución fluida y reduciendo los tiempos de ejecución.
    - A diferencia de los hilos, este enfoque ligero evita que las tareas de larga ejecución bloqueen la aplicación principal.
    - Con Asyncio, puede gestionar eficazmente pequeñas tareas, como el envío de correos electrónicos o notificaciones, sin crear muchos hilos, lo que se traduce en respuestas de notificación más rápidas.
    - Cuando se combina con aiohttp, asyncio gestiona eficazmente múltiples llamadas a la API de forma concurrente. Asyncio ofrece una forma eficaz de gestionar las tareas de entrada/salida de datos, lo que permite a los desarrolladores crear aplicaciones de alto rendimiento mediante la ejecución simultánea de tareas.